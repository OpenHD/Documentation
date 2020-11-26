# RC over MAVLink

{% hint style="info" %}
Follow the instructions for [general ](general.md)RC setup first.
{% endhint %}

### Fundamentals of RC Control via MAVLink

MAVLink defines certain **message** types one of which is "[RC\_CHANNELS\_OVERRIDE](https://mavlink.io/en/messages/common.html#RC_CHANNELS_OVERRIDE)" message. These messages are used to **command** the Flight Controller \(FC\) to **ignore** all **inputs** from the **regular** RC-**Receiver** \(SBUS, SUMD, CPPM, etc.\) and **instead** override the RC channels with the information that is sent as a **payload** with the MAVLink `RC_CHANNELS_OVERRIDE`messages. Thus this feature can be **used** to **override** the RC Transmitter and **control** the vehicle from a Ground Control Station but it can also be used as the **sole** way to **fly** the vehicle. There is **no** need to have a **standard** RC **receiver** connected to the FC.

{% hint style="info" %}
MAVLink **v1** supports **8** channels **maximum**. The new MAVLink **v2** standard supports **8 axis** channels and **16 button** \(on/off\) channels.
{% endhint %}

### Setting up RC over MAVLink

1. Duplicate the currently used Model in your transmitter \(if you use one, skip if using a joystick\) and assign a new name \(e.g.: "MyQuad" -&gt; "MyQuad Open.HD"\)
2. Switch to the new Model "MyQuad Open.HD"
3. Enter the "MODEL SETUP" Screen and turn `Internal RF Mode=OFF` and `External RF Mode=OFF`.

   This deactivates the internal and external RF module to not cause any HF-interference. For an external module it is good practice to even remove it physically from the radio. \(Some HF-modules do not respect the "OFF"-Setting and will transmit HF anyway\)

4. Edit the `openhd-settings-1.txt` in the `boot` partition of the SD card \(both Air unit and Ground unit\) and set:

   `TELEMETRY_TRANSMISSION=wbc`

   `TELEMETRY_UPLINK=mavlink`

   `RC=mavlink`

5. Unplug your regular RC-Receiver from your Flight Controller, also remove power to the receiver to prevent interference
6. Make sure the Air unit is properly connected to the Flight Controller \(See [General ](general.md)and [Wiring ](../hardware/wiring.md)-&gt; [Flight Controller](../hardware/wiring.md#flight-controller)\)
7. Connect to your Flight Controller via Mission Planner \(USB\) and open the Full-Parameter-Tree. Configure the parameters as described in the section below.
8. Save the parameters and power off your Flight Controller \(also cut USB connection to PC as it powers your FC as well\)
9. Now power everything up again: Flight Controller + Air unit and your Ground unit
10. Once up and running connect your joystick or transmitter via USB to the Ground unit
11. Connect your Flight Controller via USB to PC and connect via Mission Planner
12. Go the the RC Calibration dialog and happily see the RC Channels moving :-\)
13. Perform the RC Calibration
14. Check Failsafe Settings
15. Arm Arducopter/plane/rover **- remove any Props first!! -** and throttle up. This is essential since FailSafe won't kick-in when not in flight
16. Test the following scenarios and make sure FailSafe kicks in:
    1. Unplug USB Joystick -&gt; FailSafe should kick in
    2. Re-plug the USB Joystick -&gt; FailSafe can be disabled by the Joystick after several seconds
    3. Turn off Ground unit -&gt; FailSafe should kick in



