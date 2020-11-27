# LTE Connection

### Fundamentals of LTE

An LTE stick connected to the Air unit is part of a ZeroTier \( ZT \) network. Any other devices connected to the ZeroTier network can receive data from the Air unit. Any device with a data connection can view video \(no telemetry or RC yet\) via QOpen.HD app. As of now only one ZeroTier connected device can receive LTE video.

Latency is variable depending on the quality of your 3g/4g/5g connection. Latency has been measured at about 350ms with a 3g connection and 1280x720 30fps raspberry pi camera v2 via _gstreamer_.

### LTE Hardware

* Air unit
* Open.HD compatible WiFi adapter for the Air unit
* 3g/4g/5g data stick. Must be Linux compatible [https://www.freedesktop.org/wiki/Software/ModemManager/SupportedDevices/](https://www.freedesktop.org/wiki/Software/ModemManager/SupportedDevices/) Hilink compatibility is good. Internal WiFi is probably bad. A good example LTE stick is a Huawei e3372h
* Possibly a sim adapter. Most phone sims are Nano size and many LTE sticks require a larger sim card/adapter
* Telecom provider that does not throttle or limit your data rate or connection speed
* Ground unit and associated hardware is recommended but not required. You could just view your Air unit video sent by LTE on any internet connected device which is also part of your ZeroTier network \(your smart phone running ZeroTier and [QOpen.HD app](../ground-station-software/qopen.hd-recommended.md)\)

### Setup LTE

{% hint style="warning" %}
This is still all experimental and lacks polish. I do not recommend trying this if you are new to Open.HD
{% endhint %}

* signup for a [ZeroTier](http://zerotier.com/) account and establish a network \(its free\)
* note your ZeroTier network ID
* setup your viewing device on the ZeroTier network. For phones you will need an app. Computers install a ZeroTier program for your platform.
* wherever you manage your ZeroTier network, confirm that your viewing device is connected \( you probably have to authorize the viewing device\). Note the IP address of the viewing device as shown on ZeroTier network manager
* in `openhd-settings-1.txt` under the LTE section:

```text
LTE=Y
ZT_NETWORK=<your ZeroTier network ID>
ZT_IP=<The ip of the device you want to VIEW the video on>
```

* install QOpen.HD app on your viewing device. On the QOpen.HD app "video" enable the LTE Video slider control
* plug your LTE stick, Open.HD compatible WiFi dongle, and camera, into your Air unit and power up install happens at runtime, so first time takes extra long \(like 1 extra minute, its hacky right now\). I highly recommend attaching a monitor to your Air unit and follow the install
* go to your ZeroTier network manager and you should see a new device trying to connect. You probably have to authorize the device with ZeroTier.
* at this point video data should be getting sent by the Air unit -&gt; LTE stick -&gt; ZeroTier -&gt; IP address of ZeroTier viewing device -&gt; QOpen.HD app. ZeroTier network manager will look like this. Note the Authorization check marks on left. Also note I have 3 devices however you can only send video to one IP at this time.

![](../.gitbook/assets/image%20%2826%29.png)



* Troubleshooting: If you do not see your LTE stick connecting to ZeroTier its probably a problem with the install on the Air unit. You can delete `ZeroTier tracker.txt` file created in `boot` partition of the Air unit SD card \(this will force a reinstall attempt\) and hook up a monitor to Air unit to see what's going on. The ZeroTier tracker file gets created upon every install attempt. If that fails you can look at an Open.HD image or in the GitHub repo within `wifibroadcast scripts` and the file `lte_functions.sh`. Within `lte_functions.sh` are the install steps- try those manually on a pi with your LTE stick and attempt a manual installation
* Some of these 3g/4g cards pull a lot of amps. **YOU MUST SUPPLY SUFFICIENT POWER TO AIR UNIT AND WiFi ADAPTERS!**

