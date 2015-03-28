---
title: Managing Long-Running Processes With Supervisor
---

[Supervisor](http://supervisord.org/) is a great tool to start and manage long-running processes and the log files associated with them. It offers a lot of helpful features and is easy to get up and running.


## Install &amp; Start Supervisor

Supervisor works out of the box, so this part is easy.

{% highlight bash %}
sudo apt-get install supervisor -y && sudo supervisord
{% endhighlight %}


## Our First Program

Supervisor looks for configuration files in **/etc/supervisor/conf.d/** and it is a good idea to keep a single conf file per process. To start, let's set up a simple long-running python script. Don't pay too much attention to the contents of the conf file, we'll go over that later.

_Create /etc/supervisor/conf.d/test_python.conf containing:_

{% highlight bash %}
[program:test_python]
command=python -u test.py
directory=/home/ubuntu
stdout_logfile=/home/ubuntu/test_python_output.txt
redirect_stderr=true
{% endhighlight %}

_Create ~/test.py containing:_

{% highlight bash %}
import time
while True:
	print(time.ctime())
	time.sleep(1)
{% endhighlight %}

When creating the conf file, be sure to replace **/home/ubuntu** both times with the path to your home directory (~ isn't allowed). If you run test.py manually you'll see it prints out the time once per second.


## Using SupervisorCTL

SupervisorCTL is the tool you will use to manage everything in Supervisor. Start by running **sudo supervisorctl** and then typing **reread**. The reread command goes through the conf.d directory and loads any new program conf files. Once you see the new test_python program available, you can use the add command to load and start it (**add test_python**). The **status** command shows you all running processes, their PID and how long they've been running. Here is a short list of my commonly used supervisorctl commands and what they do.

<dl class='dl-horizontal'>
	<dt>reread</dt>
	<dd>Reload all program conf files from the conf.d directory.</dd>
	
	<dt>add [program_name]</dt>
	<dd>Add a newly created conf file to Supervisor and start the process.</dd>
	
	<dt>status</dt>
	<dd>Check the status of all programs currently managed by Supervisor.</dd>
	
	<dt>start [program_name]</dt>
	<dd>Start the given program. Used often with one-time scripts.</dd>
	
	<dt>restart [program_name]</dt>
	<dd>Restart the given program.</dd>
	
	<dt>tail -f [program_name]</dt>
	<dd>Watch the log file in real-time (same as UNIX tail -f [filename]).</dd>
	
	<dt>help</dt>
	<dd>List all available commands.</dd>
</dl>

Exit supervisorctl and check your log file (~/test_python_output.txt) to see that it is still running. If it isn't, you may have missed a step.


## Program Configuration Files

There is a wide array of options you can use while setting up your program configuration file. I've listed my favorite options below. For a full list of commands and their parameters, check out [the settings documentation](http://supervisord.org/configuration.html#program-x-section-settings)

<dl class='dl-horizontal'>
	<dt>command</dt>
	<dd>The command to run.</dd>
	
	<dt>directory</dt>
	<dd>The directory to run the command in.</dd>
	
	<dt>numprocs</dt>
	<dd>Automatically start N instances of that process.</dd>
	
	<dt>autostart</dt>
	<dd>A boolean which tells whether to run automatically or not when Supervisor starts.</dd>
	
	<dt>autorestart</dt>
	<dd>Automatically restart a process that dies, under specific conditions (see docs).</dd>
	
	<dt>stdout_logfile</dt>
	<dd>Where to log the output of your program.</dd>
	
	<dt>redirect_stderr</dt>
	<dd>Tell supervisor whether to include stderr in your standard output file.</dd>
	
	<dt>stdout_logfile_maxbytes</dt>
	<dd>The size a log file is allowed to grow to until it is auto rotated.</dd>
	
	<dt>stdout_logfile_backups</dt>
	<dd>The number of rotated log files to keep.</dd>
</dl>


## Web Interface

Supervisor provides a really nifty web interface to monitor and restart your processes. Just update the following file, restart supervisor, and you'll see it on port 9001. Feel free to change the port and protect it using HTTP Auth or whatever you see fit.

_Add the following to /etc/supervisor/supervisord.conf_

{% highlight bash %}
[inet_http_server] 
port=*:9001
{% endhighlight %}


## One-Time Scripts

I've found that Supervisor also works great for running commonly used scripts that have multiple parameters or large log files. Be sure to set **autostart** and **autorestart** in the conf file to false, so your script doesn't end up running repeatedly.


## Examples

_MongoDB_
{% highlight bash %}
[program:mongod_member]
command=/home/ubuntu/mongodb-linux-x86_64-2.0.6/bin/mongod --dbpath /mnt/mongo/ --replSet mongo5 --nojournal
directory=/home/ubuntu
stdout_logfile=/mnt/log/mongod.log
redirect_stderr=true
{% endhighlight %}

