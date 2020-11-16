# SmartSync

* [ ] Rewrite this to be a little more first-time user friendly and current, no need to show our history

## What is SmartSync and why do i need it?

To understand the need for SmartSync we need to refresh the basics.

When Open.HD first started development we wanted to easily change settings as many people working with this project and other branches are interested in experimenting with various frequencies, settings and configurations. Others were primarily interested in using it just to fly and enjoy the beautiful HD video. So, we wanted to make sure we kept things as simple as possible to maintain the plug & play ease-of-use that EZ wifibroadcast for instance has.

We accomplished this with the open.HD android app for the most part but poses a few new problems...

1. By nature, this all-in-one fpv, telemetry and control system is primarily optimized to send video data from the air to ground with some Uplink capability for RC and Telemetry as well. So, the Open.HD app is able to save settings to both air and ground pretty well however, it can take quite a long time to upload a large number of changes and under some circumstances, settings can be lost in the process, then during reboot if your video or radio function was changed and not saved you no longer have your communication link in place to assign the correct settings. As such, this requires removing the SD cards... Not Ideal...
2. In the case where an FPV Pilot who goes to the field with 3 different "drones" i.e. a miniquad optimized for 720x480p low latency video on 5.8ghz ; A medium range drone set to high data rate for HQ video ; And a long range FPV Plane set to low data rate... Without identical settings on each side, The process of matching settings would include removing the SD card from at least one of the sides and manually changing the parameters.

**What is SmartSync?**

SmartSync is simply a program that guarantees synchronization between any two air/ground vehicles that you have Open.HD installed on by making the air and ground always briefly start with fixed settings on wifi channel 1 \(2412\) then automatically matches whatever settings happened to be applied on the ground.

**Can the Open.HD android app still be used as it was before?**

Yes! All of the functionality is basically the exact same however, SmartSync well ensure that your settings always match. A primary difference and advantage is that you do not have to keep remote settings enabled \(set to 1\) in order to change settings on the air. It is recommended to simply set the remote setting timer to a low number \(2-5 seconds\) especially if using a Raspberry Pi zero on the air because it has limited CPU usage and tends to spike when settings were uploaded only with the app. With SmartSync you can just change whatever settings from the app and save them to the ground side then reboot Ground/Air and they will automatically sync up.

**Basic Configuration**

If settings were changed with openHD app, restart ground first... then start air...

![OpenHD%20SmartSync%20and%20Profile%20Guide.png](https://github.com/HD-Fpv/Open.HD/raw/master/wiki-content/ProgramFlow/OpenHD%20SmartSync%20and%20Profile%20Guide.png)

Functions:

SmartSync\_StartupMode= Set "0" for off, the still gives you a few seconds to move joystick up to "remain ON" otherwise it goes directly to boot w/ previous settings. \*\*\*Use this if you always want the fastest possible start up on the ground without any joystick input.

Set "1" ON

> If joystick is not touched "middle dead zone" , it waits for incoming requests from drone for xx seconds set on SmartSyncGround\_countdown

> If Joystick is moved down within countdown timer goes directly to boot.

SmartSyncRC\_Channel=

> Recommended to be elevator or aelieron channel \(or any other joystick with middle start position\)

SmartSyncGround\_Countdown=

> Time in seconds it listens for requests from drone.  
> \*If pi zero air is used, 45 is recommended assuming both air and ground are powered up at about the same time.

> If timer is "0" then it stays on indefinitely until killed or receives incoming requests from air.

SmartSyncOFF\_RC\_Value=1700 SmartSyncStayON\_RC\_Value=1300

> PWM alues for rc channel above \(adjust if needed\)

