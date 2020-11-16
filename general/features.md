# Features

The features as per the latest [release ](https://github.com/OpenHD/Open.HD/releases)include:

* Supports Pi A+, Pi1B+, Pi2B, Pi3B, Pi3B+, Pi3A+, Pi4, Pi Zero, Pi Zero W, Odroid-W, Pi V1 and V2 cam  \(NOTE: Ground Pi should be Pi2B or higher\)
* Maximum possible resolutions \(depending on cam used\): 1280x720p 60fps 1296x972p 42fps 1640x922p 40fps 1920x1080p 30fps
* Maximum possible video bitrate about 12Mbit
* Latency ~125ms with 720p 48fps default settings, minimum possible latency roughly around 110ms
* Support for 2.3/2.4/2.5Ghz bands and 5.2Ghz to 5.8Ghz bands
* 2.4Ghz on 3dbi omni antennas: About 1-1.5km range with ~70mw wifi sticks, about 2-3km with ~300mW high-power cards \(with default settings, about 50% higher range is possible with lower bitrate "longrange mode"\)
* 5Ghz on 3dbi omni antennas: ~250m range with 25mW wifi sticks, about 1km range with ~300mW high-power cards
* Configuration can be done from Windows, no Linux knowledge required
* Supports different configuration profiles selectable on the field via jumpers or DIP switches
* Forwarding of video stream and telemetry data to 2nd display via: USB Tethering, Wifi Hotspot, Ethernet, Wifibroadcast relay mode
* Bi-directional mavlink telemetry support \(uplink not 100% compatible with all FCs yet\)
* Support for video and telemetry inside Tower App, QGroundcontrol, Mission Planner
* Fully dynamic and automatic detection of 2nd display, just plug it in or connect via Hotspot and it'll work
* 2 wifi sticks transmit diversity on two different frequencies for bulletproof videolink
* 3 wifi sticks receive diversity support for Atheros, 5 wifi sticks receive diversity support for Ralink \(or 2x Atheros and 2x Ralink\)
* Integrated high resolution fully customizeable OSD with support for Mavlink, Frsky, LTM, Smartport telemetry
* .AVI Ground recording, PNG screenshots and telemetry data automatically saved to USB stick
* Automatic graphing of RSSI, packetloss, video bitrate and other data
* No issues as with standard wifi, no disconnection, video freeze etc, video will quickly recover
* Live and responsive RSSI display with defective blocks and packetloss display
* Video reception is very stable even in difficult multipathing environments, no constant glitching as with analog
* OSD overlay rendered on the receiver will stay clear and functional even if video is too bad to fly
* Debug logs and screenshot will be saved to sdcard in case of errors
* Low-latency/high update-rate RC over wifibroadcast via Joystick \(Atheros only\)
* Encrypted RC
* Audio
* Settings controlled by android app
* Multi camera support
* Frequency Band switching ability
* Ability to designate strongest WiFi adapter for RC
* New OSD elements
* More WiFi adapter options
* Mavlink 2 support

