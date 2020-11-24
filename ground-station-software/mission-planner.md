# Mission Planner

## Introduction

Mission Planner \(MP\) is a Ground Control Station \(GCS\) software for all types of vehicles based upon the [ArduPilot](http://ardupilot.org/) open source autopilot system, e.g. [ArduPlane](http://ardupilot.org/plane/index.html), [ArduCopter](http://ardupilot.org/copter/index.html), [ArduRover](http://ardupilot.org/rover/index.html) or newest to the family [ArduSub](https://www.ardusub.com/). It is compatible with Windows only. It can be used as a configuration utility or as a dynamic control supplement for your autonomous vehicle. Here are just a few things you can do with MP:

* Flash firmware \(the software\) into the autopilot board \(i.e. Pixhawk series\) that controls your vehicle.
* Setup, configure, and tune your vehicle for optimum performance.
* Plan, save and load autonomous missions into the autopilot with simple point-and-click way-point entry on Google or other maps.
* Download and analyze mission logs created by the autopilot.
* Interface with a PC flight simulator to create a full hardware-in-the-loop UAV simulator.
* Monitor your vehicle’s status while in operation.
* Record telemetry logs which contain much more information than the on-board autopilot logs.
* View and analyze the telemetry logs.
* Operate your vehicle in FPV \(first person view\)

## Setting up bi-directional telemetry with OpenHD.

In order to use MP in conjunction with OpenHD it is necessary to forward all telemetry to the PC. In the course of this walk-through we will choose to do it the most convenient way, namely using the Wifi-Hotspot feature running off the OpenHD GroundPi \(of course you can alternatively connect your PC also via USB Tethering, or Ethernet-Hotspot\).

**!!! Before we start make sure you have read and followed the section on how to setup** [**RC with Ardupilot**](https://github.com/HD-Fpv/Open.HD/wiki/RC-~-RC-with-Ardupilot)**. Those things are prerequisites for the following to work properly !!!**

Now, Let's gets get started:

1. Enable the WiFi-Hotspot on your GroundPi by editing the openhd-settings-1.txt. Set the following parameters: `TELEMETRY_UPLINK=mavlink` `ENABLE_RC=mavlink` `WIFI_HOTSPOT=Y`
2. Next power on your Air- and GroundPi
3. Connect to the OpenHD WiFi with your computer Default SSID is "Open.HD", default password is "wifiopenhd", channel is 1. 

   ![MissionPlanner\_BiTelem\_01.JPG](https://github.com/HD-Fpv/Open.HD/raw/master/wiki-content/GCS_Mission%20Planner/MissionPlanner_BiTelem_01.JPG)

4. Next open up a Command Prompt \(press **Win+R** -&gt; type: `cmd.exe` -&gt; Press **Enter**\)
5. Next we are going to find out the IP of our GroundPi. Type `ipconfig` -&gt; press **Ente**r Watch out for the IP-v4 address of your PC's Wifi adapter. It should read something like: `IPv4 address.....: 192.168.2.2` - Awesome! This address -1 on the last address block is the IP address of your GroundPi: i.e. `192.168.2.1` ![MissionPlanner\_BiTelem\_02.JPG](https://github.com/HD-Fpv/Open.HD/raw/master/wiki-content/GCS_Mission%20Planner/MissionPlanner_BiTelem_02.JPG)
6. Let's see if we can Ping that thing. Type `ping 192.168.2.1` -&gt; **Press Enter**. Are you getting a reply? Perfect! ![MissionPlanner\_BiTelem\_03.JPG](https://github.com/HD-Fpv/Open.HD/raw/master/wiki-content/GCS_Mission%20Planner/MissionPlanner_BiTelem_03.JPG)
7. Now start MP and choose `TCP`as the method to connect. Press the **Connect Button** ![MissionPlanner\_BiTelem\_04.JPG](https://github.com/HD-Fpv/Open.HD/raw/master/wiki-content/GCS_Mission%20Planner/MissionPlanner_BiTelem_04.JPG) and enter the IP of your GroundPi in the upcomming dialogue window: `192.168.2.1`. ![MissionPlanner\_BiTelem\_05.JPG](https://github.com/HD-Fpv/Open.HD/raw/master/wiki-content/GCS_Mission%20Planner/MissionPlanner_BiTelem_05.JPG) Next select the port \(nothing needs to be changed - the default is: `5760`\) ![MissionPlanner\_BiTelem\_06.JPG](https://github.com/HD-Fpv/Open.HD/raw/master/wiki-content/GCS_Mission%20Planner/MissionPlanner_BiTelem_06.JPG)
8. Now! Here we are! - Your MP should now happily connect to your Flight Controller \(FC\) through the OpenHD radio link. Once the initial parameter set has been transferred you can either enjoy your fancy real time telemetry or go ahead and configure your autonomous vehicle in-style. ![MissionPlanner\_BiTelem\_07.JPG](https://github.com/HD-Fpv/Open.HD/raw/master/wiki-content/GCS_Mission%20Planner/MissionPlanner_BiTelem_07.JPG)

## Injecting HD-Video into Mission Planner Heads Up Display \(HUD\)

Forwarding the HD-Video stream to MP is a little bit tricky and does not work right out of the box \(other than e.g. for QGroundControl\). However once you succeed you will have some neat benefits such as stacking the MP HUD on top of your live video.

Now, Let's do it:

1. In order to display the HD-video we need a third party software named [Gstreamer](https://gstreamer.freedesktop.org/). \(Download the 32bit version, since the 64bit version is known to cause issues\). You can download it [here](https://gstreamer.freedesktop.org/data/pkg/windows/1.9.1/gstreamer-1.0-x86-1.9.1.msi)
2. Now install Gstreamer by choosing the "Complete Install" option. Most preferably install it to `C:\gstreamer` since it is the default path and some programs depend on the binaries to be found exactly there.
3. Now edit your GroundPi's openhd-settings-1.txt and alter the following parameter: `VIDEO_UDP_PORT=5600` --&gt; `VIDEO_UDP_PORT=5500` `FORWARD_STREAM=raw`
4. Put the MicroSD card back into GroundPi and power it on.
5. Connect to the "OpenHD" Hotspot.
6. Once connected, open up a Command Prompt \(press **Win+R** -&gt; type: `cmd.exe` -&gt; Press **Enter**\)
7. Change to the `C:\gstreamer\1.0\x86\bin` directory and type the following command \(you can put this in a \*.bat batch-file later on\): `gst-launch-1.0.exe udpsrc port=5500 ! h264parse ! rtph264pay ! udpsink host=127.0.0.1 port=5600` ![MissionPlanner\_VideoHUD\_01.JPG](https://github.com/HD-Fpv/Open.HD/raw/master/wiki-content/GCS_Mission%20Planner/MissionPlanner_VideoHUD_01.JPG)
8. Now start MP. Upon first start it should notify you that a video-stream was detected and advice you to install a missing Addon. Please follow the dialog and install the component. After the install MP will automatically restart.
9. After the restart your live HD-video stream should show in the HUD window. ![MissionPlanner\_VideoHUD\_03.JPG](https://github.com/HD-Fpv/Open.HD/raw/master/wiki-content/GCS_Mission%20Planner/MissionPlanner_VideoHUD_03.JPG)
10. Go ahead and connect the telemetry link by choosing the `TCP` connect option and proceed as described above.

