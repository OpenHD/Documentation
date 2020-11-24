# Using an IP or USB Camera as second camera

This describes the case where you have a CSI camera connected AND want to connect a USB or IP camera as well. The Open.HD system allows you to view both streams simultaneously \(using Picture in Picture\) and to switch between both streams for the main display. This is often used with Thermal cameras or an extra rear facing camera on a plane.

{% hint style="warning" %}
If you have an `air.txt` file on your `boot` partition from **testing** the USB or IP camera in **single** mode, be sure to **remove** it. Leaving it will mess up the dual camera initialization.
{% endhint %}

Inside `openhd-settings-1.txt` set these settings:

```text
SecondaryCamera=IP
```

For a secondary IP camera **or** 

```text
SecondaryCamera=USB 
```

For a secondary USB camera. Then set:

```text
IsCamera1Enabled=1
IsCamera2Enabled=1
```

Now enable the band switcher:

```text
IsBandSwicherEnabled=1
```

And enable RC over Mavlink by setting:

```text
RC=mavlink
```

And optionally change the RC channel used to swap between the main video feeds:

```text
ChannelIPCamera=7
```

Please be aware you can switch between the feeds from the main QOpen.HD interface as well without the need of a joystick connected to the Ground SBC.



