---
title: Running MongoDB on Amazon Web Services
---

I've spent the past few months managing and scaling multiple MongoDB clusters on AWS, and have picked up a few tricks along the way. They may help you as you are [setting up your first Mongo instance](http://docs.mongodb.org/manual/installation/#installation-guides), or trying to keep your existing instances running smoothly.

## Choosing an AMI

Whenever I'm starting an instance from scratch, rather than using one of my own AMIs, I will use an Ubuntu AMI from [Eric Hammond](http://alestic.com/). They make it very easy to get an instance up and running immediately. One thing to note with picking which AMI to use is that Ubuntu 10.04 does not play well with EBS. I had some weird problems like Mongo locking up entirely for 5 minutes at a time due to 100% disk utilization. After getting everything over to 11.10, disk utilization stayed down.


## Updating the file limit

A good practice when setting up a fresh instance for Mongo is to raise the limit of open files allowed by the system. Mongo likes to keep a lot of files open for writing, so as your db grows past a few hundred GB, you may find yourself hitting the default limits. You can also update this after a machine has been running, but the change still requires a restart. To raise the limit, you'll need to modify the config files listed below.

_Overwrite /etc/sysctl.conf with_

{% highlight bash %}
fs.file-max = 360000
net.ipv4.ip_local_port_range = 1024 65000
net.ipv4.tcp_max_syn_backlog = 2048
{% endhighlight %}

_Overwrite /etc/security/limits.conf with_

{% highlight bash %}
ubuntu     soft     nofile     350000
ubuntu     hard     nofile     350000
{% endhighlight %}

Once those changes are made, restart the system and you're good to go. You can run <em>ulimit -a</em> to make sure the limit has been updated properly.


## Log file location

When you get around to starting Mongo, you're going to need to make some decisions such as where the log file is located (--logpath). I found that putting the log file on a separate disk from the DB data itself is a good idea. Since it will get unruly over time, valuable resources will be taken from your primary DB disk, slowing things down. I have yet to come up with an elegant solution to auto rotating these logs, but will probably end up using the logrotate tool in linux. If you have any other solutions, I'd be interested in hearing them.


## Backing up your data

Backing up a running Mongo instance can be tricky. There are ways to lock the database while copying the files, to ensure no data corruption, but that downtime can be painful. The best way I've found to go about this is to use a script created by Eric Hammond called [ec2-consistent-snapshot](http://alestic.com/2009/09/ec2-consistent-snapshot) which has been modified by Eric Lubow to [include mongo support](http://eric.lubow.org/2011/databases/mongodb/ec2-consistent-snapshot-with-mongo/). This script will freeze Mongo, freeze XFS if you're using it, and take a point in time snapshot of your data drive. This causes your database to be locked for a total of about 5 seconds, which is not bad at all compared to other methods. To install the script, there are a few packages you'll need to install. I've listed the sequence commands below that worked best for me.

{% highlight bash %}
sudo add-apt-repository ppa:alestic
sudo apt-get update
sudo apt-get install -y ec2-consistent-snapshot build-essential libio-socket-ssl-perl libdatetime-perl

sudo PERL_MM_USE_DEFAULT=1 cpan -fi MongoDB MongoDB::Admin

cd /usr/bin/
sudo wget https://raw.github.com/elubow/ec2-consistent-snapshot/master/ec2-consistent-snapshot -O ec2-consistent-snapshot
sudo chmod +x ec2-consistent-snapshot
{% endhighlight %}

Once installed, you can start snapshotting your drive(s). In the command below, you're going to need to replace the AWS access key and secret key with your own. You'll also need to set the filesystem path if you are using XFS (otherwise remove it), and the volume ID(s) at the end.

{% highlight bash %}
ec2-consistent-snapshot --debug --mongo --aws-access-key-id=ABCDEFGHI --aws-secret-access-key=ABCDEFG --xfs-filesystem=/ebs_disk/ --region us-east-1 --description "MongoDB Manual Snapshot" vol-VOLID
{% endhighlight %}


## Munin graphs

To monitor my servers, I use [Munin Monitoring](http://munin-monitoring.org/) software. It helps me keep an eye on memory usage and disk latency (important to watch) on my Mongo servers, among many other things. I use the official [MongoDB Munin plugins](https://github.com/erh/mongo-munin) for standard things like ops/sec and lock percentage, but found myself constantly needing a graph showing the replication delay between replica set members. I eventually wrote this [Mongo replication delay plugin](https://github.com/reustle/munin-mongo-replication), which adds itself to the same group as the other mongo plugins on the overview page.

Hopefully you've picked up a thing or two from this post that you can use. If you are having second thoughts about managing your own Mongo instances, you should definitely check out [Compose.io](https://www.compose.io/mongodb/). Feel free to contact me if you have any other questions. Enjoy!

