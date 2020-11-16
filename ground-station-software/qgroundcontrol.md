# QGroundControl

### Displaying the video stream via _**QGroundControl**_

{% hint style="info" %}
OpenHD has a custom QGC app available. Download the apk from the [here](https://drive.google.com/open?id=1sHjUKq0GJLkRrzAMFJs83avuvvMcVyQd). It will automatically configure and display our custom OSD.
{% endhint %}

Connect your device either via USB Tethering, Wifi-Hotspot or Ethernet-Hotspot to the GroundPi.

For WiFi connect to the OpenHD WiFi with your computer Default SSID is "Open.HD", default password is "wifiopenhd", channel is 1.

### Android Manual Setup

[QGroundControl App](https://play.google.com/store/apps/details?id=org.mavlink.qgroundcontrol) Set `FORWARD_STREAM=rtp` in openhd-settings-1.txt to send use a RTP encapsulated h264 video stream to the app. Set udp port to 5600

![Modified QGC APP with Open.HD Up/Down RSSI and system data overlay](https://github.com/HD-Fpv/Open.HD/raw/master/wiki-content/Screenshots/Screenshot_20190415-224121.jpg)

![Screenshot OSD overlay](https://github.com/HD-Fpv/Open.HD/raw/master/wiki-content/Screenshots/Screenshot_20190609-001044.jpg)

\(Modified QGC APP with Open.HD Up/Down RSSI and system data overlay\)

