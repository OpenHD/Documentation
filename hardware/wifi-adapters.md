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
mt7601u


Recommended Wifi-Dongles:

| Name | Band | TX Power | Chip | STBC/LDPC | RC | Need Heatsink | Antennas |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| ALFA AWUS036ACH | 5.8 -2.4 *| 500mw | RTL8812AU | X | X |  | 2x RP-SMA |
| ASUS USB-AC56 | 5.8 -2.4 *| 500mw | RTL8812AU | X | X |  | 2x RP-SMA |
| "Taobao Card" | 5.8 -2.4 *| 500mW | RTL8812AU | X | X | X | 2x u.fl |
| ALFA AWUS1900 | 5.8 -2.4 *| 500W | RTL8814AU | X | ? |  | 4x RP-SMA |
| Tenda U12 | 5.8 -2.4 | ? *| RTL8812AU |  |  |  | 2x u.fl 2x internal |

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
| re3332r0115 | 2.4 | 50mW | mt7601u | X |  |  | 1x u.fl |
| Cudy AC 1300 | 5.8 | ? low power | RTL8812BU |  |  |  | internal |
| Aigital AC1200  | 5.8 | ? low power | RTL8812BU |  |  |  | internal |
| COMFAST 1300Mbps  | 5.8 | ? low power | RTL8812BU |  |  |  | internal |
| Netgear A6100 | 5.8 - 2.4 *| ? | RTL8811AU |  |  |  |1x internal |

*we recommend using this Chipset in 5.8Ghz mode

These devices are supported, but doesn't have all functions like 40MHZ mode or different MCS-Indexes

#### **ASUS AC56**

This adapter is currently the most popular for OpenHD. Its small size makes it easy to fit into many builds, it uses 5.8ghz, and it is widely available. The retail price can be high, but it can often be found used or on sale for $30 or less. One antenna is internal, the 2nd is optional, and connects with RP-SMA.

* [FCC info](https://fccid.io/MSQ-USBAC56)
* [WikiDevi](https://deviwiki.com/wiki/ASUS_USB-AC56)

#### **AWUS036NHA**

This adapter is highly recommended as it is easy to find and works well. Ideal for long range as it will provide around 280mW output power. Ranges of several kilometers have been reported \(with directional antennas though\).

* [FCC info](https://apps.fcc.gov/oetcf/eas/reports/ViewExhibitReport.cfm?mode=Exhibits&RequestTimeout=500&calledFromFrame=Y&application_id=G%2Bnb%2FcnfLEByfpIAnz2OrQ%3D%3D&fcc_id=UQ23668)
* [WikiDevi](https://wikidevi.com/wiki/ALFA_Network_AWUS036NHA)

#### **Ubiquit Wifistations**

This adapter is quite large, but seems to have a good quality amp on it. Useable TXPower is not yet determined, but should be slightly higher than the AWUSH036NHA.

* [FCC info](https://apps.fcc.gov/oetcf/eas/reports/ViewExhibitReport.cfm?mode=Exhibits&RequestTimeout=500&calledFromFrame=Y&application_id=KhauP%2FSwGKHZGHiW1vSYvA%3D%3D&fcc_id=SWX-M2USB)
* [WikiDevi](https://wikidevi.com/wiki/Ubiquiti_Networks_WiFiStation_EXT)

#### **TL-WN722N V1**

This adapter will provide around 60mW output power. Range should be roughly around 800-1000m with 2.1dbi stock antennas.

* [FCC info](https://apps.fcc.gov/oetcf/eas/reports/ViewExhibitReport.cfm?mode=Exhibits&RequestTimeout=500&calledFromFrame=Y&application_id=%2BnZ3HSATHmzb0LSclLcZxA%3D%3D&fcc_id=TE7WN722NV2)
* [WikiDevi](https://wikidevi.com/wiki/TP-LINK_TL-WN722N_v1.x)

_**NOTE:**_ There have been reports that the TL-WN722N V1 seems to be replaced by V2 and V3 versions. These new versions use a completely different chipset and are _not_ compatible. Consider asking the seller for the version, if it says "V2" or "V3" on the back of the dongle it's the wrong chipset!

_**NOTE:**_ The PCB antenna causes packetloss and bad reception under certain circumstances. It is recommended to disconnect the antenna by moving the SMD component as shown below: 

![TP-Link\_722N-mod.jpg](https://github.com/HD-Fpv/Open.HD/raw/master/wiki-content/Hardware_Supported%20WiFi%20adapters/TP-Link_722N-mod.jpg)

#### AW-NU138

This adapter is very small, output power about 50mW. The internal antenna can be de-soldered and replaced with an external antenna. Since it's very small it runs quite warm, good cooling is needed.

* [FCC info](https://apps.fcc.gov/oetcf/eas/reports/ViewExhibitReport.cfm?mode=Exhibits&RequestTimeout=500&calledFromFrame=Y&application_id=ykivyt9MWET01uFkCm0wFQ%3D%3D&fcc_id=TLZ-NU138)
* [WikiDevi](https://wikidevi.com/wiki/AzureWave_AW-NU138)

#### AW-NU137

Very similar to the NU138. Reported power is 70mW. I-PEX antenna connector allows for light weight build.

* [FCC info](https://apps.fcc.gov/oetcf/eas/reports/ViewExhibitReport.cfm?mode=Exhibits&RequestTimeout=500&calledFromFrame=Y&application_id=jytSwagyYGHU0hdXERQMgw%3D%3D&fcc_id=TLZ-NU137)
* [WikiDevi](https://wikidevi.com/wiki/AzureWave_AW-NU137)

#### Taobao Card

![taobaocard.jpg](https://github.com/HD-Fpv/Open.HD/raw/master/wiki-content/Hardware_Supported%20WiFi%20adapters/taobaocard.jpg)

[Store link](https://a.aliexpress.com/_rIjofM)

This is a generic RTL8812au card sold on Taobao, which is where the name comes from.

It is a widely used card and known to work well, but it does tend to get hot. Reported power output is 500mW. This card _requires_ soldered wiring or the USB connection may disconnect before or even during flight.

It supports 2x u.fl antenna connectors.

#### re3332r0115

![re3332r0115.jpg](https://github.com/HD-Fpv/Open.HD/raw/master/wiki-content/Hardware_Supported%20WiFi%20adapters/re3332r0115.jpg)

These are spare parts for an RCA smart television, and contain a Mediatek mt7601u chipset along with a single u.fl connector. They are extremely small, barely larger than a few microSD cards lined up, and only weigh 2.7 grams.

These are not high powered cards and should not require a heatsink, but do not produce anywhere near the power output of some of the other cards.

They do not currently work with the Open.HD RC system but that should be resolved soon \(it's a bug not a problem with the card\).

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
