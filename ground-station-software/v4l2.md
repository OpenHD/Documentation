# GStreamer

## Displaying the video stream via _**GStreamer**_

Connect your device either via USB Tethering, Wifi-Hotspot or Ethernet-Hotspot to the GroundPi.

### Windows:

[Gstreamer 32-Bit Windows](https://gstreamer.freedesktop.org/data/pkg/windows/1.10.2/gstreamer-1.0-x86-1.10.2.msi) [Gstreamer 64-Bit Windows](https://gstreamer.freedesktop.org/data/pkg/windows/1.10.2/gstreamer-1.0-x86_64-1.10.2.msi)

Use the following commandline: 

```bash
gst-launch-1.0.exe udpsrc port=5000 ! h264parse ! avdec_h264 ! autovideosink sync=false
```

Set `FORWARD_STREAM=raw` in openhd-settings-1.txt to send a raw h264 stream

Some people reported the necessity to add the gst-launch-1.0.exe application to their firewall exception list, see this video for more info: [https://www.youtube.com/watch?v=eHCfyWhEAvI](https://www.youtube.com/watch?v=eHCfyWhEAvI)

**GstreamerHUD:**

Another Option is GStreamerHUD, see Github page here: [https://github.com/MovLab2/GStreamerHUD](https://github.com/MovLab2/GStreamerHUD)

[Direct Setup Download](https://www.dropbox.com/sh/5ys4jbvdgxg09cb/AABCm-OIjh5NI4WTDnr6KNw4a?dl=0&preview=GStreamerHUD.msi)

In case you get an error message that "api-ms-win-crt-runtime-l1-1-0.dll" is missing see [here](https://support.microsoft.com/en-ph/help/2999226/update-for-universal-c-runtime-in-windows) and [here](https://answers.microsoft.com/en-us/windows/forum/windows8_1-performance/error-message-api-ms-win-crt-runtime-l1-10dll-is/3a72ff02-cf73-4536-baf7-bdfd2f132a9e)

See [here](https://www.youtube.com/watch?v=eHCfyWhEAvI) for a video:

### Linux:

Install gstreamer using the package management system of your linux distribution

Use the following commandline:

```bash
gst-launch-1.0 udpsrc port=5000 ! h264parse ! avdec_h264 ! autovideosink sync=false
```

