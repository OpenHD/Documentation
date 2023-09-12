# OpenHD Flight Recording Options

OpenHD offers two methods for recording your flight footage, whether for sharing on platforms like YouTube or for personal analysis.

## 1. Air Recording

Air recording involves capturing video locally on your Air unit. This method helps eliminate any potential breakups or interference that might occur during the flight, as it records directly from the transmitted video feed.

**Note 1:** The Raspberry Pi (RPI) hardware is not capable of recording video with an on-screen display (OSD). Please refer to option 2 for OSD recording.

**Note 2:** The bitrate of the air recording is the same as the bitrate used for video transmission.

## 2. Ground Recording

Due to hardware limitations of the Raspberry Pi, which cannot record both video and OSD simultaneously, we recommend the following user-proven alternative:

1. Use QOpenHD on a tablet or Android phone.
2. Employ a screen recorder (specific application to be determined) to capture the video feed along with OSD data.

If you have access to a (powerful) x86 laptop on the ground, you can also utilize its integrated screen recording capabilities, OBS is preinstalled on our images and recommended for perfect Hardware utilisation.

### Air Recording - Enable/Disable:

You can manage air recording by either manually enabling/disabling the recording of your primary or secondary camera via QOpenHD or by using the following recommended feature:

- **Automatically Start/Stop Recording When Arming/Disarming:**
  To enable this feature, follow these steps:
  1. Open QOpenHD.
  2. Go to the settings for CAMERA1 or CAMERA2.
  3. Set V_AIR_RECORDING to AUTO(armed).

With this setting, your air recording will automatically start when you arm your drone and stop when you disarm it. You can then download the recording after the flight. Note that when AUTO(armed) is enabled, it's best not to use the QOpenHD air recording widget; however, you can still check the remaining space counter to verify if air recording is functioning correctly.

**Note:** If there is insufficient free space on your Air unit's SD card, air recording will automatically stop.
