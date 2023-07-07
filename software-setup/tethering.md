# Tethering (and other modes of connecting to OpenHD)

Different to the working procedure of 2.0 in OpenHD evo is a lot more versatile. But some advanced features are not exposed in QOpenHD or not automatically enabled.

We differenciate a little in the way that we do not automatically enable the wifi-hotspot. And we also do not stream Video/Telemetry over wifi, but use it mostly for our Webinterface to download Recordings, or debug and SSH-Access.

| Mode                           |  Webinterface  | SSH | Video | Telemetry | Internet |
| ------------------------------ | ---------------| --- | ----- | --------- | -------- |
| Ethernet-Tethering (Active)    |       YES      | YES |  YES  |    YES    |    NO    |
| Ethernet-Tethering (Passive)   |       YES      | YES |  YES  |    YES    |    YES   |
| USB-Tethering (Passive)        |       YES      | YES |  YES  |    YES    |    YES   |
| Wifi-Hotspot                   |       YES      | Yes |  NO   |    NO     |    NO    |

# SSH

The username is openhd
The password is openhd


# Wifi-Hotspot

To enable the Wifi-Hotspot you need to enable it in Air(TMP) or Ground(TMP) 
The standart IP for the SBC is 192.168.3.1.
The password is openhdopenhd
