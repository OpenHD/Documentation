# Wiring

## Wiring the system for stability

{% hint style="danger" %}
Without exaggeration, over **80%** of the **issues** raised on the support forum and Telegram group can be traced back to improper **wiring and/or shielding**. To reduce the load on the team, please make sure you have followed the instructions in this chapter, we will point you here **without** much explanation if we suspect your problem is power or shielding related.
{% endhint %}

While it may seem like you could just connect the WiFi adapter to one of the USB ports, supply power to the raspberry pi and go fly, it's not quite that simple.

Some lower power WiFi adapter such as the _TPLink 722n V1_ may work out that way, but others may not. If your WiFi adapter needs more power than it is able to draw from the Raspberry Pi USB port, you will see "interference" that isn't really interference, dropped video frames, and potentially sudden video blackout. **That could happen** _**during flight**_ **if you don't take some simple steps to avoid it**.

In addition, if the USB connection is briefly moved or subjected to vibration, it may cause the WiFi adapter to reset or disconnect from the system. This disruption might be just long enough to completely stop the connection between ground and air.

The solution for those kinds of problems is to solder power from a BEC or other 5v power supply, to the WiFi adapter\(s\).

It is also **strongly recommended** that you solder the USB data lines. On some WiFi adapters this is easy because they have ready to use solder pads, or have a mini-USB connector on the adapter \(in which case you don't have to solder anything to the adapter itself, just the other end of the cable\).

### General tips and guidelines

* use short wires
* use wires with at least 20AWG gauge \(0.5mm²\) for any **power** wires. **Signal** wires can be a lot **thinner**.
* use a shielded USB cable with the shield soldered to ground. If you use unshielded cables, twist the signal wires.
* solder _**everything**_, avoid any USB cables or plugs without a latching mechanism
* use a quality **BEC** with at least **3A**
* consider adding low-ESR electrolytic **capacitors** near the **WiFi** adapters and the raspberry pi
* **do not** use USB power banks
* **do not** use the micro USB connection on the raspberry pi for power
* **do** power the raspberry pi through the GPIO pins or by soldering power to the underside of the board
* **do** make sure the camera cable is properly seated on both ends
  * On the raspberry pi zero, the camera connection is not very secure, especially if you have connected and disconnected it many times
  * You can secure the camera cable with some tape or a drop of hot glue
* **do** make sure the raspberry pi and WiFi adapters don't get hot
  * Consider adding small heat sinks, but be sure they will remain firmly attached with strong thermal tape
* Keep the antenna away from the camera and camera cable
* If you see **straight vertical** **lines** in the video, you may need to use a **shorter** camera cable or **shield** it with foil
* The system can potentially interfere with 433Mhz, 868Mhz LRS, or GPS
  * If you encounter problems like this, consider separating, shielding or changing some of the components \(ask us for help\)

## Power wiring

### Ground

Much like the Air SBC, the Ground SBC will likely be powered by a LiPo battery. The Raspberry Pi and the WiFi cards all use 5V, which is what most BEC's produce. So hook up one of your SBC's to a LiPo battery and use a multi meter to double-check the output is +5V.

{% hint style="info" %}
The Raspberry Pi and most WiFi adapters actually like the voltage to be slightly higher than +5V, along the lines of 5.2V ~ 5.4V. If you have a variable output, best set it to +5.3V. Do not go higher than +5.4V or you will damage your Raspberry Pi and/or WiFi cards!
{% endhint %}

When you have verified the output of the BEC, you can connect it to the Raspberry Pi, to do this, you have two options. Soldering or using the GPIO Pin Header, for the Ground SBC it's OK to use the GPIO Pin Header, for the Air unit we recommend soldering. Connect the output from the BEC to the PI on pins 2 and 6 \(or 4 and 6\) according to this diagram:

![The Raspberry Pi GPIO Pin Header](../.gitbook/assets/image%20%2824%29%20%282%29.png)

This can be done easily by just plugging in the Servo header that comes with most BEC's into the Raspberry Pi Pin Header. Make sure the RED wire is connecting to Pin 2 or 4 and the BLACK wire is connecting to PIN 6. Now when you connect power to the BEC, the Raspberry Pi will power up!

The 3A BEC can also power a 7" HDMI screen with a micro USB connector.

![Raspberry Pi Powered from Pin Header](../.gitbook/assets/image%20%281%29.png)

Now that we have power going to the Raspberry Pi it's time to power the WiFi adapter\(s\). Due to the way the Raspberry Pi is designed the USB ports do not receive enough power to drive the WiFi cards, especially when connecting more than one WiFi card as is often the case on a ground station.

To mitigate this problem it is necessary to power the WiFi card\(s\) directly from the BEC as well. Please refer to the diagram below to see how. Please note that **5V** and **GND** are **NOT** connected to the Raspberry Pi USB Port.

![Powering the Raspberry Pi and the WiFi card from the BEC](../.gitbook/assets/image%20%284%29.png)

Soldering as much of these connections as possible will prevent accidental disconnects. On the Ground side, soldering might be optional, on the Air side it is mandatory as it is subjected to greater vibrations.

To monitor the power on the ground unit, please take a look at the [Ground Power Monitoring](../advanced-setup/ground-power-monitoring.md) section.

### Air

Much of the explanation for the Ground wiring also applies to the Air, except that where it is likely no problem to use USB adapters on the Ground, using them in the Air will absolutely cause problems. It is therefore absolutely recommended to solder as much as possible in the Air setup and if you want to use connectors, please use connectors that can withstand the vibrations and stresses of being in a vehicle. 

{% hint style="success" %}
JST connectors can be used as they lock into place and these can be had for quite cheap. The 4 pin variant can be used to replace the standard USB cords. 
{% endhint %}

When using the Raspberry Pi Zero as an Air SBC you can solder the power and USB data lines to the points shown in this diagram:

![Proper Power and USB wiring for the Raspberry Pi Zero](../.gitbook/assets/image%20%288%29%20%281%29.png)

## Other connections

### Flight Controller

With Power and WiFi connected the system basics should work, in most cases  however, you will want to hook up some form of flight controller. While the setup of such a controller is covered in [Software Setup](../software-setup/telemetry-and-osd.md), the physical connection also requires some special attention.

{% hint style="danger" %}
Several users are a member of the **'I fried my serial port and now I'm using a USB to Serial Adapter**'-club. To prevent membership, please read how to properly connect your Flight Controller.
{% endhint %}

Most Flight Controllers will allow for Serial \(UART\) connections, while some may only output Telemetry, most modern Flight Controllers will allow true bi-directional communication, allowing the system to send commands to the Flight Controller as well. 

In order to connect via Serial to a Flight Controller the following pins must be connected:

| Raspberry Pi | Flight Controller |
| :--- | :--- |
| TX \(Pin 8\) | RX |
| RX \(Pin 10\) | TX |
| GND \(Any Ground\) | GND |

![Correctly wiring the Flight Controller](../.gitbook/assets/image%20%283%29.png)

Refer to the schematics of your specific Flight Controller to find the right connections for the UART you want to use. Most Flight Controllers have more than one UART, so pay attention!

The Raspberry Pi uses **3.3V** for it's UART, while most Flight Controllers and Micro controllers such as the Arduino use **5V**. Directly connecting these to the Raspberry Pi will ensure membership of the aforementioned club. As with most issues there are two ways around this, a nice way and a cheap and easy way.

#### Cheap

Use two resistors to create a voltage divider circuit on the INCOMING \(RX\) connection to the Raspberry Pi. This will scale the incoming 5V to a safer 3.3V\(-ish\). The **outgoing** 3.3V from the Pi's TX will in most cases still be recognized by the Flight controller. See the diagram below from [OscarLiang.net](http://OscarLiang.net) for an example.

![Using a voltage divider](../.gitbook/assets/image%20%287%29.png)

#### Good

A better solution with more guarantees, but slightly more expensive and slightly more complex to wire up is an actual Logic Level Converter. These come in many forms, but in principle they all do the same. Make sure only 3.3V shows up at the Pi and making sure 5V is sent to the connected Flight- or Micro controller.

There are many different types of logic level converters out there, they are mostly very cheap and come with easy enough manuals. You don't need bi-directional logic level converters for serial communication since the flow only goes one way through the wires.

To see some background, please check this [Sparkfun](https://learn.sparkfun.com/tutorials/bi-directional-logic-level-converter-hookup-guide/all) link.

### Antenna tracker

On the ground SBC you might want to attach an Antenna Tracker, most of these units require us to output the Mavlink data via Serial communication. When only connecting the TX from the Raspberry Pi to the RX of the Ground station no special consideration needs to be given to the voltage levels. Most Micro controllers will allow the 3.3V of the Raspberry Pi as a logic signal.

When connecting the RX on the Raspberry Pi as well, however, earlier warnings mentioned for the [Flight Controller](wiring.md#flight-controller) come into play. The Raspberry Pi uses **3.3V** Serial, while most Micro controllers use **5V**. Putting **5V** on the Raspberry Pi RX pin will **permanently damage** the Serial controller. Please refer to the '[cheap](wiring.md#cheap)' and '[good](wiring.md#good)' solutions mentioned under the Flight Controller section.

