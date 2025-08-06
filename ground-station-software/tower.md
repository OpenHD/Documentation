# Tower

<!-- LEGACY DOCUMENTATION NOTICE -->
> ⚠️ **This documentation is outdated!** A current version is available at [openhdfpv.org](https://openhdfpv.org)
> 
> [📖 **View Updated Version of This Page** →](https://openhdfpv.org)

---


## Displaying the video stream via _**Tower**_

Connect your device either via USB Tethering, Wifi-Hotspot or Ethernet-Hotspot to the GroundPi.

### Android

[Tower app](https://github.com/DroidPlanner/Tower/releases)

* Set `FORWARD_STREAM=rtp` in openhd-settings-1.txt to send a RTP encapsulated h264 stream to the app.
* Set video port in Tower app settings to 5000. See [here](https://github.com/DroidPlanner/Tower/wiki/Custom-video-stream) for instructions.

#### Tower App settings

For telemetry, set protocol to "UDP" and leave default server port 14550. Click on "Connect".

For video, change settings according to the following screenshots. Please note, the Tower App will not display the video stream if it doesn't receive telemetry. First make sure that telemetry works, then configure video!

![Tower\_Settings\_Android\_2\_sm.png](../.gitbook/assets/Tower_Settings_Android_1_sm.png) 
![Tower\_Settings\_Android\_2\_sm.png](../.gitbook/assets/Tower_Settings_Android_2_sm.png)

