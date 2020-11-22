# Wiring

## Wiring the system for stability

While it may seem like you could just connect the WiFi adapter to one of the USB ports, supply power to the raspberry pi and go fly, it's not quite that simple.

Some lower power WiFi adapter such as the _TPLink 722n_ may work out that way, but others may not. If your WiFi adapter needs more power than it is able to draw from the Raspberry Pi USB port, you will see "interference" that isn't really interference, dropped video frames, and potentially sudden video blackout. **That could happen** _**during flight**_ **if you don't take some simple steps to avoid it**.

In addition, if the USB connection is briefly moved or subjected to vibration, it may cause the WiFi adapter to reset or disconnect from the system, just long enough to completely stop the connection between ground and air.

The solution for those kinds of problems is to solder power from a BEC or other 5v power supply, to the WiFi adapter\(s\).

It is also strongly recommended that you solder the USB data lines. On some WiFi adapters this is easy because they have ready to use solder pads, or have a mini-USB connector on the adapter \(in which case you don't have to solder anything to the adapter itself, just the other end of the cable\).

### General tips and guidelines

* use short wires
* use wires with at least 20AWG gauge \(0.5mm²\)
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

   

![Powering the Raspberry Pi and the WiFi card from the ESC](../.gitbook/assets/image%20%283%29.png)

Example of a raspberry pi powered through the GPIO pins \(+ 5V -&gt; pin 4 / ground -&gt; pin 6\) :

![Raspberry Pi powered from ESC](https://github.com/OpenHD/Open.HD/raw/master/wiki-content/Hardware_Propper%20Wiring/Yes21_groundPi_power_wiring.jpg)

The 3A BEC can also power a 7" HDMI screen with a micro USB connector.

