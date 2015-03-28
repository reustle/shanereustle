---
title: Force Screen Resolutions On Ubuntu
---

I was recently trying to change the resolution of an external monitor on Ubuntu 10.10 and found that the usual xorg.conf file no longer existed. You are able to create one by running **X -configure** in recovery mode, but that seems like a bit of a pain. Here is a simpler way to add screen resolution options in Ubuntu 10.10.

First, you will need to generate a new modeline to use in the configuration by passing your desired resolution and rate to cvt. I will use 1920x1080 throughout this tutorial.

{% highlight bash %}
cvt 1920 1080 60
{% endhighlight %}

That should return something that looks like this

{% highlight bash %}
# 1920x1080 59.96 Hz (CVT 2.07M9) hsync: 67.16 kHz; pclk: 173.00 MHz
Modeline "1920x1080_60.00"  173.00  1920 2048 2248 2576  1080 1083 1088 1120 -hsync +vsync
{% endhighlight %}

Copy everything on the second line after "Modeline " and then add that as a new mode like this

{% highlight bash %}
xrandr --newmode "1920x1080_60.00"  173.00  1920 2048 2248 2576  1080 1083 1088 1120 -hsync +vsync
{% endhighlight %}

Now that the mode has been added, we need to move it to the proper monitor. If you are trying to add this resolution to your main display, then you can skip the next step.

You can use the **xrandr** command to see the names of each attached monitor. If you are on a laptop that has a VGA port, that is probably called VGA1, but check to make sure.

Next we will move the mode we just created to VGA1 using the name of the new mode from the previous command (the text in double quotes). If you cannot find the VGA1 device, it may be called CRT1.

{% highlight bash %}
xrandr --addmode VGA1 "1920x1080_60.00"
{% endhighlight %}

You will now see the new resolution listed in the display options. You can read more on [configuring X here](https://wiki.ubuntu.com/X/Config/Resolution).

Update 2 May 2011: Seems to work fine on 11.04 as well.

