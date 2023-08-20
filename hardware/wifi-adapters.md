# WiFi Adapters

If you are new to OpenHD and not familiar with all the advantages/disadvantages of different wifi cards, get 2x ASUS USB-AC56 or a similar good quality adapter using the RTL8812AU chipset.
Pay attention to the version number of the WiFi adapter, manufacturers often use a completely different chipset with a different version number! Every letter in the number above matters, they are not the same !

When choosing between 2.4G and 5.8G, while 2.4G offers better penetration than 5.8G, it much more suspectible to common sources of interference and it can be hard to find a not polluted channel on 2.4G. 5.8G also allows you to use your existing 2.4G RC transmitters. For those reasons, more people currently choose 5.8 for OpenHD.

RX diversity:
You can use either a wifi card with multiple antennas or multiple wifi cards on your ground station for RX diversity. However, it is easy to mess up things by improper wiring and/or using wrong antennas when using more than one rx card. We therefore do not recommend more than one card for new users.
Also, while you can mix cards (given they support the same frequency) with different chipsets or even from different vendors, this is not recommended.

Since Version 2.3 various new Chipsets are supported, including:

RTL8812AU
RTL8812BU
RTL8811AU
AR9271


Recommended Wifi-Dongles:

| Name | Band | TX Power | Chip | STBC/LDPC | RC | Need Heatsink | Antennas |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| ALFA AWUS036ACH | 5.8 -2.4 *| 500mw | RTL8812AU | X | X |  | 2x RP-SMA |
| ASUS USB-AC56 | 5.8 -2.4 *| 500mw | RTL8812AU | X | X |  | 2x RP-SMA |
| "Taobao Card" | 5.8 -2.4 *| 500mW | RTL8812AU | X | X | X | 2x u.fl |
| ALFA AWUS1900 | 5.8 -2.4 *| 500mW | RTL8814AU | X | ? |  | 4x RP-SMA |
| Tenda U12 | 5.8 -2.4 *| 100mW | RTL8812AU | X | X |  | 2x u.fl 2x internal |
| Cudy AC 1300 | 5.8 | ? low power | RTL8812BU |  | X |  | internal |
| Aigital AC1200  | 5.8 | ? low power | RTL8812BU |  | X |  | internal |
| COMFAST 1300Mbps  | 5.8 | ? low power | RTL8812BU |  | X |  | internal |
| Netgear A6100 | 5.8 - 2.4 *| 50mw | RTL8811AU |  | X |  |1x internal |

*we recommend using this Chipset in 5.8Ghz mode

There are a lot more devices with are supported, this lists only show tested devices. 

Additional Wifi-Devices with reduced functions:

| Name | Band | TX Power | Chip | STBC/LDPC | RC | Need Heatsink | Antennas |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| ALFA AWUS036NHA | 2.3-2.4 | 280mW | AR9271 |  | X |  | 1x RP-SMA |
| Ubiquiti Wifistation | 2.3-2.4 | 800mW+ | AR9271 |  | X |  | 1x RP-SMA |
| Ubiquiti Wifistation EXT | 2.3-2.4 | 800mW+ | AR9271 |  | X |  | 1x RP-SMA |
| TPLink TL-WN722N V1 | 2.3-2.4 | 60mW | AR9271 |  | X |  | 1x RP-SMA |
| AW-NU138 | 2.3-2.4 | 50mW | AR9271 |  | X | X | 1x Internal |
| AW-NU137 | 2.3-2.4 | 70mW | AR9271 |  | X |  | 1x u.fl |


*we recommend using this Chipset in 5.8Ghz mode

These devices are supported, but doesn't have all functions like 40MHZ mode or different MCS-Indexes

#### **ASUS AC56**

This adapter is currently the most popular for OpenHD. Its small size makes it easy to fit into many builds, it uses 5.8ghz, and it is widely available. The retail price can be high, but it can often be found used or on sale for $30 or less. One antenna is internal, the 2nd is optional, and connects with RP-SMA.

* [FCC info](https://fccid.io/MSQ-USBAC56)
* [WikiDevi](https://deviwiki.com/wiki/ASUS_USB-AC56)

#### Taobao Card

![taobaocard.jpg](https://github.com/OpenHD/OpenHD/blob/2.3-evo/wiki-content/Hardware_Supported%20WiFi%20adapters/taobaocard.jpg?raw=true)

[Store link](https://a.aliexpress.com/_rIjofM)

This is a generic RTL8812au card sold on Taobao, which is where the name comes from.

It is a widely used card and known to work well, but it does tend to get hot. Reported power output is 500mW. This card _requires_ soldered wiring or the USB connection may disconnect before or even during flight.

It supports 2x u.fl antenna connectors.

### Finding alternatives

For cheap alternatives check out the usual computer stores and maybe consider Aliexpress. Be a little careful, some cards are of questionable quality. Generally, High-Quality/Brand Name modules with RTL8812au chipsets perform best.

A good way to find out more about wifi sticks and modules offered online is to look for product numbers, chipsets, or even better an FCC ID. With those, try to find high-res internal photos of the cards, to find out the chipset and the amps used.

Search the web for those numbers and also these two very helpful sites:

* [https://fccid.io/](https://fccid.io/) \(FCC documents which contain internal photos\)
* [https://wikidevi.com/wiki/](https://wikidevi.com/wiki/) \(general infos and sometimes photos\)

When you have found photos, google for the numbers on the amps to find a datasheet giving a rough estimate about the expectable output power.

It would be nice if you report back your findings in case you tried a wifi card that is not listed here.

### External amp

Another way to increase output power is to use a low-power wifi stick combined with an external amplifier.
