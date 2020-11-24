# WiFi Hotspot

To make it easy to connect a Phone or Tablet to your Ground SBC in order to view the video or change settings or even run your Ground Control software the system allows for a WiFi Hotspot by default.

You can change the way the Hotspot behaves by changing the `WIFI_HOTSPOT` parameter. It takes the following values:

| Value | Description |
| :--- | :--- |
| auto | Automatically selects a WiFi Band and channel that allows for the least amount of interference with the 'main' WiFi reception of the Air SBC |
| y | Uses the static Band and Channel settings for manual control |
| n | Disables the WiFi Hotspot functionality altogether |

### Default SSID an Password

The default SSID is `Open.HD` and the default password is `wifiopenhd`. Both values can be changed by editing the `apconfig.txt` file in the `BOOT` partition of the SD card. No settings for this have been exposed yet in the app.

### Custom Band and channel settings

When selecting the `y` option you can set the Band and Channel on which the system starts the WiFi Hotspot.

TODO

