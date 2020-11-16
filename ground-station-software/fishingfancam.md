# FishingFanCam

## Displaying the video stream via _**Fishing Fan Cam App**_

Connect your device either via USB Tethering, Wifi-Hotspot or Ethernet-Hotspot to the GroundPi.

### iPhone/iPad

[Fishing FanCam app](https://itunes.apple.com/us/app/fishing-fancam/id1187600031)

#### Fishing Fan Cam App Settings

* Click on the eye icon \(on the bottom right\)
* Now a debug screen appears, select all on the upper bar, delete all parameters and set:

```text
udpsrc port=5000 ! h264parse ! avdec_h264 ! autovideosink sync=false
```

Set `FORWARD_STREAM=raw` in openhd-settings-1.txt to send a raw h264 stream

