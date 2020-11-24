# General

Open.HD is capable of direct control of your model by transmitting your control data alongside the HD video stream. This potentially means that only a single HF-Link between ground and aircraft is required for all your needs. Essentially there are two ways in which Open.HD facilitates RC control, RC via mavlink \(Ardupilot\) or RC via a serial protocol \(iNAV, Betaflight, Cleanflight\).

* If you have a flight controller which **can** be controlled by **MAVLink** RC\_CHANNELS\_OVERRIDE messages then that is the **recommended** solution. Since the RC\_CHANNELS\_OVERRIDE is an implementation of the bi-directional MAVLink telemetry protocol both Telemetry and RC can happily co-exist on the very same transmission medium. \(See [RC over MAVLink](rc-over-mavlink.md)\)
* If your flight controller **cannot** be controlled by **MAVLink** RC\_CHANNELS\_OVERRIDE messages you can **still** use Open.HD for RC control. You must have a flight controller that **accepts** one of the following **uninverted** serial receiver protocols: MSP, SUMD \(Graupner/JR\), IBUS \(FlySky\), SRXL / XBUS Mode B \(Multiplex\). \(See [RC over Serial](rc-over-serial.md)\)

If you meet **any** of these requirements you can **eliminate** your old radio receiver. As described in this documentation you will configure software and hardware and then plug-in a supported USB joystick \(or transmitter\) into the Ground unit. The inputs will be sent to the Air unit and forwarded on to your flight controller.

**One HF-Link for all aspects of operations: Video + Telemetry + Control**

* Only single HF-Link \(WiFi\) required
* weight savings
* cost savings
* simplicity
* Open.HD RC control has longer range than video

### Input Devices / Joysticks

In order to allow control of your model the user needs some sort of USB joystick which will provide input to the Ground unit. For this HID-compatible USB-Joysticks and traditional RC transmitters \(with USB/hid ability\) can be used as input device. For the sake of simplicity this input device will be referred to as joystick from now on. The joystick simply connects via USB to the Ground unit and gets recognized automatically by the system. All standard HID-compatible joysticks can be used, however we recommend using a decent quality joystick with good quality gimbals and a narrow stick dead-band. Best results have been reported using RC transmitters with a USB-port \(normally used for flight simulators\). 

{% hint style="info" %}
If possible disable the RF transmission function on your RC transmitter so that it does not interfere with Open.HD.
{% endhint %}

The following joysticks are known to work well with Open.HD:

* FrSky Taranis X9D
* FrSky Taranis X9D+
* FrSky Taranis X9E
* iRangeX IR8M
* Radiomaster T16S
* [GeeekPi Raspberry Pi USB-Joystick controller](https://www.robotshop.com/en/joystick-controller-board-raspberry-pi.html)

### Basic setup

{% hint style="danger" %}
Make sure you have **proper RTH** functionality **enabled** on your Flight Controller **before** using RC over Open.HD. Nothing is **worse** than seeing your model fly **away**. Failures **can** and **will** happen, plan for **redundancy**!
{% endhint %}

#### Configure RC general parameters

Please make the following modifications to the `openhd-settings-1.txt` file in the `boot` partition of both SD cards or use the [QOpen.HD app](../ground-station-software/qopen.hd-recommended.md) to modify the settings.

{% tabs %}
{% tab title="When using Atheros cards" %}
```text
EncryptionOrRange=Range
CTS_PROTECTION=Y
RC=mavlink or other option
```
{% endtab %}

{% tab title="Any other card" %}
```text
EncryptionOrRange=Encryption
CTS_PROTECTION=N
RC=mavlink or other option
```
{% endtab %}
{% endtabs %}

Optionally you can lock the transmission from the Ground unit to the Air unit to one specific WiFi card on the Ground by setting the MAC address of this card in the config file:

```text
PrimaryCardMac=(MAC ADDRESS)
```

#### Configure joystick related settings

Next edit the `joyconfig.txt` file in the `boot` partition of both SD cards \(same content\):

Axis mapping to ROLL, PITCH, THROTTLE, etc. USSUALLY NOT needed to be changed.

```text
#define AXIS0_INITIAL=<value>
```

sets the initial values for the controls. This is necessary, as it is currently not possible to detect the stick positions until they have been moved. For yaw, roll, pitch you probably want 1500, for throttle 1000.

#### Wiring

In order for any of this to work, the Air unit needs to be able to talk to the Flight Controller in a proper manner. Please refer to [Wiring ](../hardware/wiring.md)-&gt; [Flight Controller](../hardware/wiring.md#flight-controller) for an explanation on this.

If you use the builtin Serial of the Raspberry Pi leave default `RC_FC_SERIALPORT=/dev/serial0`, if using an external USB2Serial adapter, set `RC_SERIALPORT=/dev/ttyUSB0`

#### Testing

Depending on your Flight Controller make **sure** you followed **either** [RC over MAVLink](rc-over-mavlink.md) or [RC over Serial](rc-over-serial.md).

**Connect** Joystick or Transmitter in **Joystick** mode \(Taranis needs to be powered before connecting\).

 Do a **ground** test for **correct** packet **reception** and signal:

{% hint style="info" %}
Increase **distance** to the aircraft until you are at the **end** of the **video** range. R/C control should now **still** work, you should _**not**_ ****see lots of Lost **packets** in the RSSI display in the upper right corner.
{% endhint %}



