---
description: Guide for Air Recording without OSD for YouTube or similar platforms.
---

# Air Recording Guide

Record your flights locally on your air unit with minimal performance impact. The recorded video maintains the same bitrate as the transmitted video but is free from breakups due to packet loss since it's stored locally on your air unit, not the ground unit.

To enable this feature:

1. Enable video recording for a connected camera. In QOpenHD, navigate to **OpenHD Settings** > **Camera** and, using the parameter editor, set:

V_AIR_RECORDING=Enabled

QOpenHD will now automatically start recording your camera's video during operation.

2. To access and view the recordings, you have two options:

- **Option a**: After a flight, remove the SD card from your air unit and insert it into a card reader. You can find the recordings in the following directory: `SD_CARD/home/openhd/videos`.

  If you are using Windows, you may need to use a tool like "diskinternals Linux reader."

- **Option b**: After a flight, enable the "Wi-Fi hotspot" on your air Pi (requires a Pi with integrated Wi-Fi). Connect your phone or PC to the Pi's Wi-Fi network, open a web browser, enter the Pi's IP address. You will access its web interface, where you can find the video files.

# Recording Widget

You can now initiate recordings using the recording widget, which also displays the available space on your SD card.
