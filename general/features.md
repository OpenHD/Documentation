# Features

## Supported Devices:
* [Raspberry Pi](hardware/raspberry.md)
* [Radxa Rock 5]

The features as per the latest evo [release ](https://github.com/OpenHD/OpenHD/releases)include:

* We officially support Pi2B (version 1.2+) , Pi3B, Pi3B+, Pi3A+, Pi4,CM4 , Pi Zero 2, Nvidia Jetson Nano, Nvidia Jetson Nano 2GB,X86 as AIR and Pi3B, Pi3B+, Pi3A+, Pi4,CM4 ,X86 as Ground
* Latency values are different with EVO and are currently changing a lot,and depend on the hardware choices, official numbers will follow later.
* Support for 2.3/2.4/2.5GHz bands and 5.2-5.8GHz bands.
* Range values could have changed with EVO, official numbers will follow later.
* Configuration can be done from QOpenHD and the [OpenHD-ImageWriter](https://openhdfpv.org/downloads/), no config files are needed anymore.
* Flashing can and should be done with the [OpenHD-ImageWriter](https://openhdfpv.org/downloads/)
* Forwarding of video stream and telemetry data to 2nd device via: USB tethering, ethernet. Hotspot will follow later.
* Bi-directional MAVLink telemetry support, compatible with most flight controllers.
* FC-settings, video and telemetry are compatible with QGroundcontrol and don't need any modification.
* Integrated high resolution fully customizeable OSD with support for MAVLink telemetry.
* Realtime view of RSSI, packetloss, video bitrate and other important data in the OSD.
* No issues as with standard WiFi, no disconnection, video freeze etc, video will recover quickly.
* Live and responsive RSSI display with defective blocks and packetloss display.
* Video reception is very stable even in difficult multipathing environments, no constant glitching as seen with analog FPV.
* OSD overlay rendered on the receiver will stay clear and functional even if video is too bad to fly.
* Low-latency/high update-rate RC over wifibroadcast via USB-Joystick
* Optimised FEC for most stable connection.
