---
description: Dual camera setup process
---

# Dual Camera

Dual camera refers to the usage of a primary camera (recommended: RPI CSI) and a secondary camera, e.g. a thermal Camera (recommended: USB Thermal camera).

To use this configuration, your hardware should fulfill the following prerequisites:

**AIR:** Use a Raspberry Pi 4 or at least a Raspberry Pi 3 - the USB thermal image needs to be scaled and encoded in software, which results in more CPU load.

**GROUND:** Similar to the air unit, the secondary video is decoded and displayed in a software-accelerated path. Use a Raspberry Pi 4 or x86-based hardware.

## Setup:

1. Configure QOpenHD (your Ground Control Station) to display 2 video feeds simultaneously. Your primary video is always full-screen, and your secondary video (previously called PIP) is in the lower left corner and can be maximized, minimized, or scaled to your liking:

   - Go to QOpenHD -> General -> N Cameras to control and set it to 2.
   - Restart QOpenHD.

2. Configure OpenHD for dual-camera usage. After performing these steps, your air unit will wait for up to 12 seconds at boot for exactly 2 auto-detectable cameras to become available (default is 1). With variable bitrate enabled, it will automatically recommend a matching bitrate to the secondary and primary cameras (default split: 60%:40%).

   2.1. Boot up your air and ground unit; you can do that without any or only one camera connected.
   
   2.2. Inside QOpenHD, go to OpenHD -> Air and set V_N_CAMERAS to "DUAL."
   
   2.3. Reboot your air and ground unit.
   
   2.4. Validate by using the dummy camera feature: Reboot the air and ground without any cameras connected; you should now see 2 dummy camera streams and statistics for 2 streams in QOpenHD.
   
   2.5. Power off your air unit and connect your 2 cameras, then reboot. OpenHD should now display your primary and secondary camera feeds coming from your 2 cameras.

**Troubleshooting:** In case any of your cameras are not automatically detected at boot, OpenHD will create dummy cameras for them to avoid holding up the boot process indefinitely waiting for cameras. Read the setup pages specific to your cameras if they are not detected (e.g., a dummy camera is created instead).
