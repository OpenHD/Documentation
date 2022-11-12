---
description: Setup Joystick RC
---

# Joystick RC

WARNING: Beta Beta for now !!\
\
OpenHD supports RC over MAVLINK. This means you can connect a Joystick (e.g. your RC controller in joystick mode) to your ground station via USB and controll your drone directly via the OpenHD wifibroadcast link.\
\
NOTE: WiFi is not best suited for many small packets, as needed for RC. For the best experience, we recommend using a standard RC link on a different frequency than your OpenHD wifibroadcast link (e.g. 2.4G ELRS and 5.8G wifibroadcast).\
\
NOTE2: RC over MAVLINK is supported by INAV, Ardupilot and Pixhawk. It is not supported on betaflight.\
\
NOTE3: The RC data is always sent over the same UART telemetry connection between OpenHD and your FC as required for mavlink telemetry.\
\
Step 1: Enable joystick on your ground unit. In QOpenHD, go to the OpenHD settings page, GROUND (TMP) and set ENABLE\__JOY_\_RC to true. Reboot your ground station.\
<img src="../.gitbook/assets/Screenshot from 2022-11-12 17-42-46.png" alt="" data-size="original">\
\
Step 2: Connect your Joystick to the ground station (For RC controllers, connect via USB and select Joystick mode.\
\
Step 3: Make sure OpenHD detects and properly reads values from your joystick. In QOpenHD / RC you can see the current readouts. Example TX16s connected with AETR and 18 channels:\
![](<../.gitbook/assets/Screenshot from 2022-11-12 17-45-44.png>)\
\
Step 4: Validate Failsafe: OpenHD always sends RC joystick data as long as JOY_RC is eabled and a Joystick is connected. It stops sending data if you disconnect your Joystick, resulting in a failsafe on the supported FCs (TODO validate)._\
__\
_Step 5: You can adjust the update rate in the same settings screen as JOY\_RC. Note that his setting is only available if you JOY\_RC is enabled. The update rate controlls how many_&#x20;

```
MAVLINK_MSG_ID_RC_CHANNELS_OVERRIDE
```

packets are broadcasted per second. \
