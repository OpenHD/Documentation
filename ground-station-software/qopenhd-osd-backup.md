---
description: Backup your QOpenHD OSD Settings
---

# QOpenHD OSD backup

<!-- LEGACY DOCUMENTATION NOTICE -->
> ⚠️ **This documentation is outdated!** A current version is available at [openhdfpv.org](https://openhdfpv.org)
> 
> [📖 **View Updated Version of This Page** →](https://openhdfpv.org)

---


Re-flashing the OpenHD Image will overwrite all previous Settings. However, you can backup your QOpenHD settings to a file and load this backup file after a re-flash.\
NOTE: This only includes your QOpenHD specific settings, like color and position of OSD elements. It does not include OpenHD settings, like camera resolution, framerate, bandwidth, channel.\
\
1\) Create the backup file:\
Go to QOpenHD ->  Dev -> Save settings to file\
This will create a file called "QOpenHD.conf" inside your RPI SD Card\
\
2\) Save the backup file locally, e.g on a USB drive:\
2.1) Power down your ground unit, remove the SD card, and insert it into your PC card reader\
2.2) Using windows / linux file explorer, save the file locally to your USB drive. It can be found in the "openhd" folder in the root of your SD card.\
\
3\) Use a backup file after a image re-flash:\
3.1) Insert ground unit SD card into your PC\
3.2) Copy your local backup (e.g. from your USB drive) to the "openhd" folder on your SD card\
3.3) Insert your SD card into your ground station (e.g. RPI)\
3.3) Go to QOpenHD -> DEV -> Load Settings from file. QOpenHD will prompt you to restart after a successfull load.\
