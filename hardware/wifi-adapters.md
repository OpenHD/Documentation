# WiFi Adapters

Pay attention to the version number of the WiFi adapter, manufacturers often use a completely different chipset with a different version number! We highly recommend at least 2 WiFi cards on the GroundPi. This will enable diversity and give you significant gains! The Pi3 can support 2-3 USB connections, and the Pi4 can support 4 or more.

When choosing between 2.4 and 5.8ghz, know that 2.4 will get better range, but is susceptible to more common sources of interference. 2.4ghz RC transmitters and many common WiFi signals will interfere with 2.4ghz OpenHD. 5.8 WiFi is less common, for now, and it also conflicts less with most popular RC transmitters. For those reasons, more people currently choose 5.8 for OpenHD.

Please use this [form](https://docs.google.com/forms/d/e/1FAIpQLSd_03vS1duD0oFZp42enOvZxElc2p3ghEwpEpJphieajb2lJQ/viewform) to submit any WiFi Dongles you may have tested. We will add them to the matrix below!

| Name | Band | TX Power | Chip | STBC/LDPC | RC | Need Heatsink | Antennas |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| ALFA AWUS036ACH | 5.8 | 500mw | RTL8812AU | X | X |  | 2x RP-SMA |
| ASUS USB-AC56 | 5.8 | 500mw | RTL8812AU | X | X |  | 2x RP-SMA |
| ALFA AWUS036NHA | 2.3-2.4 | 280mW | AR9271 |  | X |  | 1x RP-SMA |
| Ubiquiti Wifistation | 2.3-2.4 | 800mW+ | AR9271 |  | X |  | 1x RP-SMA |
| Ubiquiti Wifistation EXT | 2.3-2.4 | 800mW+ | AR9271 |  | X |  | 1x RP-SMA |
| TPLink TL-WN722N V1 | 2.3-2.4 | 60mW | AR9271 |  | X |  | 1x RP-SMA |
| AW-NU138 | 2.3-2.4 | 50mW | AR9271 |  | X | X | 1x Internal |
| AW-NU137 | 2.3-2.4 | 70mW | AR9271 |  | X |  | 1x u.fl |
| "[Blue Stick](https://www.aliexpress.com/item/4000051464939.html)" | 2.3-2.4 | 1200mW+ | AR9271 |  | X | X | 1x u.fl or  1x RP-SMA |
| "[Green Stick](https://www.aliexpress.com/item/32954949341.html?sku_id=66407945777)" | 2.3-2.4 | 50mW | AR9271 |  | X |  | 1x u.fl |
| "Taobao Card" | 5.8 | 500mW | RTL8812AU | X | X | X | 2x u.fl |
| re3332r0115 | 2.4 | 50mW | mt7601u | X |  |  | 1x u.fl |
| ALFA AWUS1900 | 5.8 | 500W | RTL8814AU | X | ? |  | 4x RP-SMA |

#### **ASUS AC56**

This adapter is currently the most popular for OpenHD. Its small size makes it easy to fit into many builds, it uses 5.8ghz, and it is widely available. The retail price can be high, but it can often be found used or on sale for $30 or less. One antenna is internal, the 2nd is optional, and connects with RP-SMA.

* [FCC info](https://fccid.io/MSQ-USBAC56)
* [WikiDevi](https://deviwiki.com/wiki/ASUS_USB-AC56)

#### **AWUS036NHA**

This adapter is highly recommended as it is easy to find and works well. Ideal for long range as it will provide around 280mW output power. Ranges of several kilometers have been reported \(with directional antennas though\).

* [FCC info](https://apps.fcc.gov/oetcf/eas/reports/ViewExhibitReport.cfm?mode=Exhibits&RequestTimeout=500&calledFromFrame=Y&application_id=G%2Bnb%2FcnfLEByfpIAnz2OrQ%3D%3D&fcc_id=UQ23668)
* [WikiDevi](https://deviwiki.com/wiki/ALFA_Network_AWUS036NHA)

#### **Ubiquit Wifistations**

This adapter is quite large, but seems to have a good quality amp on it. Useable TXPower is not yet determined, but should be slightly higher than the AWUSH036NHA.

* [FCC info](https://apps.fcc.gov/oetcf/eas/reports/ViewExhibitReport.cfm?mode=Exhibits&RequestTimeout=500&calledFromFrame=Y&application_id=KhauP%2FSwGKHZGHiW1vSYvA%3D%3D&fcc_id=SWX-M2USB)
* [WikiDevi](https://deviwiki.com/wiki/Ubiquiti_Networks_WiFiStation_EXT)

#### **TL-WN722N V1**

This adapter will provide around 60mW output power. Range should be roughly around 800-1000m with 2.1dbi stock antennas.

* [FCC info](https://apps.fcc.gov/oetcf/eas/reports/ViewExhibitReport.cfm?mode=Exhibits&RequestTimeout=500&calledFromFrame=Y&application_id=%2BnZ3HSATHmzb0LSclLcZxA%3D%3D&fcc_id=TE7WN722NV2)
* [WikiDevi](https://deviwiki.com/wiki/TP-LINK_TL-WN722N_v1.x)

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

{% hint style="warning" %}
They do not currently work with the Open.HD RC system but that should be resolved soon \(it's a bug not a problem with the card\).
{% endhint %}

### Finding alternatives

The following USB WiFi dongles with the following chipsets work and are actively supported:

* Atheros AR9271 \(2.3-2.6G ONLY!\)
* Realtek RTL8812AU \(5.8G ONLY!\)

For cheap alternatives check out the usual computer stores and maybe consider AliExpress. Be a little careful, some cards are of questionable quality. Generally, High-Quality/Brand Name modules from ALFA WIRELESS with the AR9271 or RTL8812 chipsets perform best.

A good way to find out more about WiFi sticks and modules offered online is to look for product numbers, chipsets, or even better an FCC ID. With those, try to find high-res internal photos of the cards, to find out the chipset and the amps used.

Search the web for those numbers and also these two very helpful sites:

* [https://fccid.io/](https://fccid.io/) \(FCC documents which contain internal photos\)
* [https://wikidevi.com/wiki/](https://wikidevi.com/wiki/) \(general info and sometimes photos\)

When you have found photos, google for the numbers on the amps to find a datasheet giving a rough estimate about the expectable output power.

It would be nice if you report back your findings in case you tried a WiFi card that is not listed here.

### External amp

Another way to increase output power is to use a low-power WiFi stick combined with an external amp like this "2W" amp:

#### Banggood amp

{% embed url="https://www.banggood.com/2\_4G-2W-Radio-Signal-Booster-Antenna-Feeder-For-DJI-Phantom-Multirotor-TX-Extend-Range-p-986756.html?rmmds=search" %}

Real output power is around 600mW with a low-power AR9271 stick.

#### AliExpress bi-directional amp

{% embed url="https://www.aliexpress.com/item/32865062382.html" %}

Allows for bi-directional communication and amplification, great in combination with a low power "Green Stick".

