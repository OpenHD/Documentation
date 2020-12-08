# SmartSync

## What is SmartSync and why do I need it?

To understand the need for SmartSync we need to refresh the basics.

When Open.HD first started development we wanted to easily change settings as many people working with this project and other branches are interested in experimenting with various frequencies, settings and configurations. Others were primarily interested in using it to just fly and enjoy the beautiful HD video. So, we wanted to make sure we kept things as simple as possible to maintain the plug & play ease-of-use that we want the project to have.

We accomplished a lot by using a dedicated settings and OSD [application ](../ground-station-software/qopen.hd-recommended.md)which makes it easy to change settings on the fly. This left us with two issues:

1. This all-in-one fpv, telemetry and control system is primarily **optimized** to send video data from the **air to ground** with some **up-link** capability for **RC and Telemetry** as well. So, the [QOpen.HD app](../ground-station-software/qopen.hd-recommended.md) is able to **save** **settings to both air and ground** pretty well however, it can take quite a long time to upload a large number of changes. Under some circumstances, **settings can be lost** in the process, then during reboot if your video or radio function was changed and not saved you no longer have your communication link in place to assign the correct settings. As such, this requires removing the SD cards and manually editing the configuration.
2. In the case where an FPV Pilot who goes to the field with **3 different vehicles** i.e. a mini quad optimized for 720x480p low latency video on 5.8ghz ; A medium range drone set to high data rate for HQ video ; And a long range FPV Plane set to low data rate... Without **identical settings** on both **Ground and Air**, the process of matching settings would include **removing the SD** card from at least one of the sides and **manually** changing the parameters when switching between drones.

**What is SmartSync?**

SmartSync is a program that **guarantees synchronization** between **any vehicle** and the **ground station** that you have Open.HD installed on by making the air and ground always briefly start with fixed settings on a specific wifi channel \(settable in [QOpen.HD](../ground-station-software/qopen.hd-recommended.md)\) then automatically matches whatever settings happened to be applied on the ground.

{% hint style="warning" %}
Be aware that the settings of the **GROUND** station are applied to the **AIR** vehicle. Make sure you **save** your _profiles_ on the Ground Station and **load** the appropriate one before connecting to the AIR vehicle.
{% endhint %}

## **Basic Configuration**

If you change any setting in QOpen.HD and save them with the AIR vehicle connected, they will be persisted automatically. SmartSync comes into play at boot, by default you don't have to worry about it.

{% hint style="danger" %}
if you every have trouble, remember that **GROUND** has to be started **before AIR** and by default SmartSync is **disabled**!
{% endhint %}

## Advanced scenario's

If you want or need more control over SmartSync there are several options to prevent the default behavior. You can use GPIO 26 with a switch to disable SmartSync, or you can use a connected Joystick's Elevator channel during startup.

![The different methods of overriding default SmartSync behavior.](https://github.com/HD-Fpv/Open.HD/raw/master/wiki-content/ProgramFlow/OpenHD%20SmartSync%20and%20Profile%20Guide.png)

Aside from the methods mentioned to prevent SmartSync, we also have complete control over the system in the settings. Again, all settings are best modified through the [QOpen.HD app](../ground-station-software/qopen.hd-recommended.md).

{% tabs %}
{% tab title="SmartSync\_StartupMode" %}
| Value | Description |
| :--- | :--- |
| 0 _\(default\)_ | Disable SmartSync, this actually still gives you a couple of seconds to use either the joystick or the GPIO connected switch to force SmartSync. Otherwise it boots with the last know settings. This is the fastest way to start Open.HD. |
| 1 | Unless overridden by either the Joystick or the GPIO switch the Ground will wait for an incoming connection from the Air for a specified period of time \(see _SmartSyncGround\_Countdown_\) and perform SmartSync if a connection is established within that time. |
{% endtab %}

{% tab title="SmartSyncRC\_Channel" %}
| Value | Description |
| :--- | :--- |
| 0~12 | The RC channel to observe for enabling or disabling SmartSync during boot. Defaults to 2, which tends to be the Elevator channel on most setups. |
{% endtab %}

{% tab title="SmartSyncGround\_Countdown" %}
| Value | Description |
| :--- | :--- |
| 0~999 | The duration in seconds to wait for the Air unit to become available. |
| _45_ | _Recommended when using a Raspberry Pi as an Air unit._ |
| 0 | Wait indefinitely for the Air unit to become available |
{% endtab %}

{% tab title="SmartSyncON/OFF\_RC\_Value" %}
| Value | Description |
| :--- | :--- |
| 0~2500 | The PWM value above or below which the desired action \(On or OFF\) is triggered. |
| 1700 | The default value above which SmartSync is considered ON |
| 1300 | The default value below which SmartSync is considered OFF |
{% endtab %}
{% endtabs %}



