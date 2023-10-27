# Wiring

### Wiring OpenHD

While it may seem like you could just connect the wifi adapter to one of the USB ports, supply power to the raspberry pi and go fly, it's not quite that simple. The success of your project depends on **proper wiring and power supply**.

Some lower power wifi adapter such as the TPLink 722n may work out that way, but others may not. If your wifi adapter needs more power than it is able to draw from the Raspberry Pi USB port, you will see "interference" that isn't really interference, dropped video frames, and potentially sudden video blackout. **That could happen** _**during flight**_ **if you don't take some simple steps to avoid it**.

In addition, if the USB connection is briefly moved or subjected to vibration, it may cause the wifi adapter to reset or disconnect from the system, just long enough to completely stop the connection between ground and air.

The solution for those kinds of problems is to solder power from a BEC or other 5v power supply, to the wifi adapter(s).

It is also strongly recommended that you solder the USB data lines. On some wifi adapters this is easy because they have ready to use solder pads, or have a mini-USB connector on the adapter (in which case you don't have to solder anything to the adapter itself, just the other end of the cable).

### Example:

<figure><img src="../.gitbook/assets/Connection Diagram.png" alt=""><figcaption></figcaption></figure>

### Some tips to keep in mind

* use short wires
* use wires with at least 20AWG gauge (0.5mm²)
* solder _everything_, avoid any USB cables or plugs
  * An exception is the 036NHA wifi adapter, you should solder the end of the cable that goes to the Pi but the adapter side can be plugged in normally
* use a quality BEC with at least 3A
* consider adding low-ESR electrolytic caps near the wifi adapters and the raspberry pi
* **do not** use USB power banks
* **do not** use the micro USB connection on the raspberry pi for power
* **do** power the raspberry pi through the GPIO pins or by soldering power to the underside of the board
* **do** make sure the camera cable is properly seated on both ends
  * On the raspberry pi zero, the camera connection is not very secure, especially if you have connected and disconnected it many times
  * You can secure the camera cable with some tape or a drop of hot glue
* **do** make sure the raspberry pi and wifi adapters don't get hot
  * Consider adding small heatsinks, but be sure they will remain firmly attached with strong thermal tape
* Keep the antenna away from the camera and camera cable
* If you see straight vertical lines in the video, you may need to use a shorter camera cable or shield it with foil
* The system can potentially interfere with 433Mhz, 868Mhz LRS, or GPS
  * If you encounter problems like this, consider separating, shielding or changing some of the components (ask us for help)

![Wiring-Pi0\_sm.jpg](.gitbook/assets/Wiring-Pi0\_sm.jpg) ![Wiring-Pi3\_sm.jpg](.gitbook/assets/Wiring-Pi3\_sm.jpg) ![Wiring-052nh.jpg](.gitbook/assets/Wiring-052nh.jpg) ![Wiring-Pi1B.jpg](.gitbook/assets/Wiring-Pi1B.jpg)

Example of a raspberry pi powered through the GPIO pins (+ 5V -> pin 4 / ground -> pin 6) :

![groundPi\_power\_wiring.jpg](.gitbook/assets/Yes21\_groundPi\_power\_wiring.jpg)

The 3A BEC can also power a 7" HDMI screen with a micro USB connector.
