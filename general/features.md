# Features

The features as per the latest [release ](https://github.com/OpenHD/Open.HD/releases)include:

* [x] Supports Pi A+, Pi1B+, Pi2B, Pi3B, Pi3B+, Pi3A+, Pi4, Pi Zero, Pi Zero W, Odroid-W, Pi V1 and V2 cam  \(NOTE: Ground Pi should be Pi2B or higher\)
* [x] Maximum possible resolutions \(depending on cam used\): 1280x720p 60fps 1296x972p 42fps 1640x922p 40fps 1920x1080p 30fps
* [x] Maximum possible video bitrate about 12Mbit
* [x] Latency ~125ms with 720p 48fps default settings, minimum possible latency roughly around 110ms
* [x] Support for 2.3/2.4/2.5Ghz bands and 5.2Ghz to 5.8Ghz bands
* [x] 2.4Ghz on 3dbi omni antennas: About 1-1.5km range with ~70mw wifi sticks, about 2-3km with ~300mW high-power cards \(with default settings, about 50% higher range is possible with lower bitrate "longrange mode"\)
* [x] 5Ghz on 3dbi omni antennas: ~250m range with 25mW wifi sticks, about 1km range with ~300mW high-power cards
* [x] Configuration can be done from Windows, no Linux knowledge required
* [x] Supports different configuration profiles selectable on the field via jumpers or DIP switches
* [x] Forwarding of video stream and telemetry data to 2nd display via: USB Tethering, Wifi Hotspot, Ethernet, Wifibroadcast relay mode
* [x] Bi-directional mavlink telemetry support \(uplink not 100% compatible with all FCs yet\)
* [x] Support for video and telemetry inside Tower App, QGroundcontrol, Mission Planner
* [x] Fully dynamic and automatic detection of 2nd display, just plug it in or connect via Hotspot and it'll work
* [x] 2 wifi sticks transmit diversity on two different frequencies for bulletproof videolink
* [x] 3 wifi sticks receive diversity support for Atheros, 5 wifi sticks receive diversity support for Ralink \(or 2x Atheros and 2x Ralink\)
* [x] Integrated high resolution fully customizeable OSD with support for Mavlink, Frsky, LTM, Smartport telemetry
* [x] .AVI Ground recording, PNG screenshots and telemetry data automatically saved to USB stick
* [x] Automatic graphing of RSSI, packetloss, video bitrate and other data
* [x] No issues as with standard wifi, no disconnection, video freeze etc, video will quickly recover
* [x] Live and responsive RSSI display with defective blocks and packetloss display
* [x] Video reception is very stable even in difficult multipathing environments, no constant glitching as with analog
* [x] OSD overlay rendered on the receiver will stay clear and functional even if video is too bad to fly
* [x] Debug logs and screenshot will be saved to sdcard in case of errors
* [x] Low-latency/high update-rate RC over wifibroadcast via Joystick \(Atheros only\)
* [x] Encrypted RC
* [x] Audio
* [x] Settings controlled by android app
* [x] Multi camera support
* [x] Frequency Band switching ability
* [x] Ability to designate strongest WiFi adapter for RC
* [x] New OSD elements
* [x] More WiFi adapter options
* [x] Mavlink 2 support

