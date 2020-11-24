# Bandwidth switching

This is an **experimental** functionality that allows you to switch the WiFi **channel width** being used for the **transmission** from the Air unit to the Ground. The available bandwidths are:

5 MHz, 10 MHz and 20 MHz

Using a **narrower** bandwidth will allow for **greater range,** using a **wider** bandwidth will allow for **higher quality** video but at the cost of **reduced range.**

{% hint style="warning" %}
This **experimental** feature only works with **Atheros** based cards.
{% endhint %}

To **enable** this functionality make the following changes to the settings file `openhd-settings-1.txt` in the `boot` partition.

```text
SecondaryCamera=No
RC=mavlink
PrimaryCardMAC=00126d726127
```

This will **enable** the bandwidth switching **feature**. Be aware that the **MAC** address of the most **powerful** WiFi card on the **Ground** unit needs to be **specified**. For example if you have one TP-Link and one Wifistation, use the mac address of the Wifistation card as this is **significantly** more powerful.

And **optionally** change the RC channel used to switch between the bandwidths:

```text
ChannelToListen2=8
```

You can also **adjust** the PWM values if they are **out of range** for your TX:

```text
Band5Below=1200
Band10ValueMin=1200
Band10ValueMax=1650
Band20After=1650
```

Also, it is recommended to change this in `joyconfig.txt`:

```text
#define AXIS7_INITIAL 1000
```

To

```text
#define AXIS7_INITIAL 1800
```

That will prevent bandwidth from changing at boot time.

