---
title: Friendly Server Connection Names
---

Keeping track of which machines you're SSHed into can be a pain, especially when you're dealing with a large number of connections. At one point, I was connecting to 30+ machines every morning to monitor things like htop, mongostat, iostat and misc log files. Looking at 30 tabs in terminal named _ubuntu@ip-10-95-85-205:~$_ was not very helpful.

Below is a snippet of code I wrote at the end of my **~/.bashrc** file which sets the command prefix to _MachineName:~$_ and attempts to set the title of the terminal tab to _MachineName_. Be sure to update the variable in the first line.

{% highlight bash %}
export machine_name='MachineName'
PS1='$machine_name:\[\033[01;34m\]\w\[\033[00m\]\$ '
echo -n -e "\033]0;$machine_name\007"
{% endhighlight %}

Hopefully this makes managing your connections a little bit easier. Enjoy!

