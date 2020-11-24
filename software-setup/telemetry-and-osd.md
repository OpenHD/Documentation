# Telemetry and OSD

{% hint style="warning" %}
With Ardupilot you may need to enable certain "stream rate" parameters on the flight controller. More information is available on the rc with mavlink page
{% endhint %}

### Configure general OSD and telemetry parameters in openhd-settings-1.txt \(both on AirPi and GroundPi\)

* Set the Pi's serial port baudrate to the same baudrate as the serial telemetry data stream coming from the flight control. E.g. `FC_TELEMETRY_BAUDRATE=57600` if your flightcontrol sends it's telemetry data using 57600 baud.
* For the onboard Pi serial port leave default `FC_TELEMETRY_SERIALPORT=/dev/serial0`, if using an external USB2Serial adapter, set `FC_TELEMETRY_SERIALPORT=/dev/ttyUSB0`
* If you want to connect your flight controller to the AirPi and use wifibroadcast for telemetry transmission, leave `TELEMETRY_TRANSMISSION=wbc`
* If you have some other means of transmitting the telemetry to the ground \(e.g. an LRS with serial downlink or 3DR dongles\) choose `TELEMETRY_TRANSMISSION=external` to receive the telemetry stream on the ground Pi serial port. If using external telemetry transmission, also configure `EXTERNAL_TELEMETRY_SERIALPORT_GROUND=` and `EXTERNAL_TELEMETRY_SERIALPORT_GROUND_BAUDRATE=`

### Configure telemetry protocol and OSD options in osdconfig.txt \(only on the Ground SBC\)

* Choose the telemetry protocol used, Mavlink is default, other options supported are Frky and Lightweight telemetry \(LTM\). E.g.: `#define LTM`
* Choose graphical OSD options you would like to have enabled in osdconfig.txt. Should be self-explanatory.

Note: INav users must enable the Compass by settings COMPASS\_INAV=true

Generally, try to configure your flight control so that it does not send out unnecessary large amounts of data to keep the packet rate as low as possible.

The received telemetry data stream will also be saved in text and raw form to an USB memory stick automatically for later review.

###  Wiring

Please refer to the [Flight Controller](../hardware/wiring.md#flight-controller) section of the [Wiring ](../hardware/wiring.md)chapter.

