# Ethernet

Different to the working procedure of 2.0 in OpenHD evo there are two modes of operation:

1.Passive (recommended)
2.Active

# Passive

OpenHD has it's ethernet standardly activated as Client mode, this means you can connect it to a router or anything that provices a DHCP server and use it like that.

## Setup on Ubuntu

## Setup on Windows

## Setup on Android

### USB

{% hint style="warning" %}
This mode charges your mobile phone from the SBC, keep in mind, that Raspberries often can not boot when a phone is connected.
{% endhint %}

1. Connect a suitable cable to your SBC, keep in mind, not every usb cable that can charge your device can carry data, so please use a data-capable cable.
2. Go to your network settings, hotspot and enable USB-Tethering.
3. You're good to go everything else is done on the SBC itself.
4. For the best experience use the original QOpenHD evo app, which can be found on the playstore.

{% hint style="information" %}
Some carriers and manufacturers hide the tethering setting, also it's sometimes hidden if the device does not have a SIM-card. Here you sometimes can trigger the setting from a third party app. (suggested app will be added later)
{% endhint %}

### Ethernet

1. Connect a suitable Ethernet-Adapter to your Android device.
2. Go to your network settings, hotspot and enable Ethernet-Tethering.
3. You're good to go everything else is done on the SBC itself.
4. For the best experience use the original QOpenHD evo app, which can be found on the playstore.

{% hint style="information" %}
Some carriers and manufacturers hide the tethering setting, also it's sometimes hidden if the device does not have a SIM-card. Here you sometimes can trigger the setting from a third party app. (suggested app will be added later)
{% endhint %}

# Active
This mode is made for IP cameras or connecting perifials to the ethernet Port which do not have a DHCP server.
The SBC will start it's on DHCP server and let's device connect to it.

{% hint style="warning" %}
This removes the ability to share internet with the SBC.
{% endhint %}
