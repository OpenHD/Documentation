---
description: Dual camera setup process
---

# Dual Camera

Dual camera refers to the usage of a primary camera (recommended: RPI CSI) and a secondary camera, e.g. a thermal Camera (recommended: USB Thermal camera).\
\
To use this configuration, your hardware should fulfill the following prerequisites:\
\
AIR: Use a rpi 4 or at least a rpi 3 - the USB thermal image needs to be scaled and encoded in SW, which results in more CPU load.\
\
GROUND: Similar to air, the secondary video is decoded and displayed in a SW accelerated path, use pi4 or x86.\
\
Setup:\
Step 1: Configure QOpenHD (your Ground controll station) to display 2 video feeds simultaneously - your primary video is always full screen, your secondary video (previously called pip) is in the lower right corner and can be maximized / minimzed / scaled to your liking:\
\
Go to QOpenHD -> General -> N Cameras to control and set it to 2\
Restart QOpenHD.\
\
Step 2: Configure OpenHD for dualcam usage - after preforming these steps, your air unit will wait for up to 12 seconds at boot for exactly 2 auto-detectable cameras to become available (default 1). With variable bitrate enabled, it will automatically recommend a matching bitrate to the secondary and primary camera (default split: 60% : 40%)\
Step 2.1: Boot up your air and ground unit, you can do that without any / only one camera connected.\
Step 2.2: Inside QOpenHD, go to OpenHD -> Air -> and set V\_N\_CAMERAS to "DUAL"\
Step 2.3: Reboot your air and ground unit.\
Step 2.4: Validate by using the dummy camera feature: Reboot air and ground without any camera(s) connected - you should now see 2 dummy camera stream(s) and statistics for 2 streams in QOpenHD\
Step 2.5: Power off your air unit and connect your 2 cameras, then reboot - OpenHD should now display your primary and secondary camera feeds coming from your 2 cameras.\
\
Troubleshooting: In case any of your camera(s) are not automatically detected at boot, OpenHD will create dummy camera(s) for them to not infinitely hold up the boot process waiting for camera(s) - read the setup pages specific for your camera(s) if they are not detected (e.g. a dummy camera is created instead).\
