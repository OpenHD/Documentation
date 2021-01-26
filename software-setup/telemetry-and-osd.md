# Telemetry and OSD

{% hint style="warning" %}
With Ardupilot you may need to enable certain "stream rate" parameters on the flight controller. More information is available on the rc with mavlink page
{% endhint %}

### General

By default the Open.HD system will use it's own transmission system to send the Telemetry for the Air unit to the Ground unit. This is controlled by the `TELEMETRY_TRANSMISSION` parameter in the `openhd-settings-1.txt` file in the `boot` partition of the SD card.

* If you want to connect your flight controller to the Air unit and use Open.HD for telemetry transmission, leave `TELEMETRY_TRANSMISSION=wbc`
* If you have some other means of transmitting the telemetry to the ground \(e.g. a Long Range System with serial downlink or 3DR dongles\) choose `TELEMETRY_TRANSMISSION=external` to receive the telemetry stream on the Ground unit serial port.  If using external telemetry transmission, also configure `EXTERNAL_TELEMETRY_SERIALPORT_GROUND=` and `EXTERNAL_TELEMETRY_SERIALPORT_GROUND_BAUDRATE=`

The most common ports used are:

* `/dev/serial0` for the internal UART of the Raspberry PI
* `/dev/ttyUSB0` for a USB 2 Serial adapter

### Wiring

Please refer to the [Flight Controller](../hardware/wiring.md#flight-controller) section of the [Wiring ](../hardware/wiring.md)chapter.

### Baud rate and port setting

When connecting a Flight Controller with Ardupilot installed, it is important to also set the correct baud rate both in the FC and in Open.HD. You can use QOpen.HD to modify this setting or directly edit the `openhd-settings-1.txt` file in the `boot` partition of the SD card for the Air unit.

Make sure to keep both references to the Flight Controller in sync:

```text
FC_RC_SERIALPORT=/dev/serial0
FC_RC_BAUDRATE=115200

FC_TELEMETRY_SERIALPORT=/dev/serial0
FC_TELEMETRY_BAUDRATE=115200
```

In the above \(default\) config we use the Raspberry Pi internal UART to connect to the Flight Controller with a baud rate of 115200. These are pretty default settings. Don't go below 9600 for the baud rate.

The most common ports used are:

* `/dev/serial0` for the internal UART of the Raspberry PI
* `/dev/ttyUSB0` for a USB 2 Serial adapter

Now connect a PC to the Flight Controller using USB and start [Mission Planner](../ground-station-software/mission-planner.md).

Using the Config/Tuning -&gt; Full Parameter Tree menu items change the following settings:

![](../.gitbook/assets/image%20%2820%29.png)

Make sure the baud setting matches what you set in Open.HD and for the best performance use MAVLink protocol 2.

Save the settings and disconnect the Flight Controller.

### Stream rates settings

When connecting a Flight Controller with Ardupilot installed, it is important to also set the correct Stream rates. Else nothing will be shown on the OSD.

You can choose from different subsets of telemetry information and how often you want the Flight Controller \(FC\) to stream that particular set of data per second \(defined in Hz\). These parameters are the so called `SRx_Parameters` where x represents the serial ports using Mavlink in an ascending order. (If SERIAL0, SERIAL2, SERIAL6 are using Mavlink, the corresponding Paramaters are SR0_, SR1_ and SR2_).

In order to avoid transmitting telemetry data too often over our radio link, we have to select just the necessary data \(the right subsets of information\) and at the same time find a good compromise on how often this data should be send and thus be updated. The following parameters have to be found working very reliably:

```text
SR1_ADSB=5
SR1_EXT_STAT=2
SR1_EXTRA1=4
SR1_EXTRA2=4
SR1_EXTRA3=2
SR1_PARAMS=10
SR1_POSITION=2
SR1_RAW_CTRL=0
SR1_RAW_SENS=2
SR1_RC_CHAN=2
```

Connect a PC to the Flight Controller using USB and start [Mission Planner](../ground-station-software/mission-planner.md).

Using the Config/Tuning -&gt; Full Parameter Tree menu items change the mentioned settings:

![Where to find the stream rate settings](../.gitbook/assets/image%20%2819%29.png)

Save the settings and disconnect the Flight Controller.

### Using the 'old' OSD

By default Open.HD starts the QOpen.HD app on the Ground unit as it contains both an OSD and the full menu system to change the configuration. Some people prefer the older OSD and it is still included in the Open.HD distributions!

To change to the original OSD system, please make the following modification in th`openhd-settings-1.txt` file in the `boot` partition of the SD card for the Ground unit.

```text
ENABLE_QOPENHD=N
```

#### Configure telemetry protocol and OSD options in osdconfig.txt \(only on the Ground SBC\)

* Choose the telemetry protocol used, Mavlink is default, other options supported are Frky and Lightweight telemetry \(LTM\). E.g.: `#define LTM`
* Choose graphical OSD options you would like to have enabled in osdconfig.txt. Should be self-explanatory.

Note: INav users must enable the Compass by settings `COMPASS_INAV=true`



