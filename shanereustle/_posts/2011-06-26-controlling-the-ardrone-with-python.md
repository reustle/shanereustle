---
title: Controlling The ARDrone With Python
---

This past weekend I helped out with [GameHackDay](http://gamehackday.org) and spent most of my time hacking on one of the 12 [ARDrone Parrots](http://ardrone.parrot.com). After spending some time fighting with the open [ARDrone API](https://projects.ardrone.org/) which was written in C, I was relieved to discover a [Python ARDrone API](https://github.com/venthur/python-ardrone).

The Python API is fairly easy to get up and running as it has no dependencies, unless you plan on running the included demo which uses [PyGame](http://pygame.org/). I found that it was easiest to install pygame on ubuntu using **sudo apt-get install python-pygame**.

Once you have cloned the python-ardrone project, turn on the drone and connect to its network. You're now able to run **demo.py** and take it for a spin! If you open up **demo.py**, you'll see that the commands are fairly straight forward. One you've become familiar with the drones commands, let's make the drone fly by itself. To start, create a new file and copy this in.

{% highlight python %}
import libardrone
from time import sleep

drone = libardrone.ARDrone()

drone.takeoff()
sleep(3)
drone.move_forward()
sleep(2)
drone.land()
sleep(3)
drone.halt()
{% endhighlight %}

This code is pretty self explanatory. Connect to the drone, takeoff, move forward, land and disconnect. You can start to imagine all of the different things you can do with this.

One thing we discovered at the event was that the latest firmware update seems to help with the stability. You can download that [ARDrone Firmware Update](http://www.parrot.com/catalog/downloads/ar-drone/) here. Installation of the update is easy. While connected to the drones network, connect via FTP into 192.168.1.1 over port 5551. After a few minutes, the connection will succeed and you'll see an empty directory. Drop the downloaded **ardrone_update.plf** file there and disconnect. Disconnect from the wifi as well, then reboot the drone by unplugging the battery and reconnecting it. Don't press any buttons, and allow the drone to install the update. After some time, you'll see all of the green lights come back on which means you're done!.

The next step in controlling the drone is to read in the sensor data. The drone provides altitude, gyros, trim, and so on. There are also two on-board cameras you can monitor using an image library. Look into the navdata objects for more details. I plan on covering navdata in a future blog entry.

I have not decided if I want to continue controlling the drone using Python or move over to NodeJS. I feel the event loop in JavaScript is a better fit for this kind of scripting. I found a rudimentary [NodeJS ARDrone API](https://github.com/timjb/node-ardrone) here, which should get me started. For now, I will continue to learn more about it using Python.

**Side Note**: If you're in the NYC area, join the [ARDrone Meetup Group](http://www.meetup.com/ardrone/).

