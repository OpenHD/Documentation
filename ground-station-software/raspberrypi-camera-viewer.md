# RaspberryPi Camera Viewer

## Displaying the video stream via _**RaspberryPi Camera Viewer**_

Connect your device either via USB Tethering, Wifi-Hotspot or Ethernet-Hotspot to the GroundPi.

### Android

[RaspberryPi Camera Viewer](https://play.google.com/store/apps/details?id=pl.effisoft.rpicamviewer2&hl=de)

#### App Settings

* Click on the "+" Icon to create a new camera preset \(on the bottom right\)
* Next choose "Enable advanced mode" and enter the following gstreamer pipeline:

  `udpsrc port=5600 ! application/x-rtp, payload=96 ! rtpjitterbuffer ! rtph264depay ! avdec_h264 ! autovideosink sync=false`

Set `FORWARD_STREAM=rtp` in openhd-settings-1.txt

![RaspberryPiCameraViewer\_01.jpg](https://github.com/HD-Fpv/Open.HD/raw/master/wiki-content/GCS_RaspberryPiCameraViewer/RaspberryPiCameraViewer_01.jpg)

![RaspberryPiCameraViewer\_02.jpg](https://github.com/HD-Fpv/Open.HD/raw/master/wiki-content/GCS_RaspberryPiCameraViewer/RaspberryPiCameraViewer_02.jpg)

![RaspberryPiCameraViewer\_03.jpg](https://github.com/HD-Fpv/Open.HD/raw/master/wiki-content/GCS_RaspberryPiCameraViewer/RaspberryPiCameraViewer_03.jpg)

