---
description: WiFi Adapters for OpenHD Evo
---

# WiFi Adapters

If you are new to OpenHD and not familiar with all the advantages and disadvantages of different WiFi cards, consider getting 2x ASUS USB-AC56 or a similar high-quality adapter using the RTL8812AU chipset. Pay close attention to the version number of the WiFi adapter, as manufacturers often use different chipsets with varying version numbers. Each letter and number in the version matters; they are not the same.

When choosing between 2.4GHz and 5.8GHz, keep in mind that while 2.4GHz offers better penetration, it is more susceptible to common sources of interference, and finding a clean channel on 2.4GHz can be challenging. 5.8GHz also allows you to use your existing 2.4GHz RC transmitters. For these reasons, many users currently prefer 5.8GHz for OpenHD.

## RX Diversity

You can achieve RX diversity by using either a WiFi card with multiple antennas or multiple WiFi cards on your ground station. However, it's easy to make mistakes with improper wiring or using the wrong antennas when using more than one RX card. Therefore, we do not recommend using more than one card for new users. Mixing cards with different chipsets or from different vendors, even if they support the same frequency, is also not recommended.

## Supported Chipsets (Since Version 2.3)

- RTL8812AU
- RTL8812BU
- RTL8811AU
- AR9271

## Recommended WiFi Dongles

| Name               | Band       | TX Power | Chip      | STBC/LDPC | RC  | Need Heatsink | Antennas   |
| :----------------- | :--------- | :------- | :-------- | :-------- | :-- | :------------ | :--------- |
| ALFA AWUS036ACH    | 5.8 - 2.4* | 500mW    | RTL8812AU | X         | X   |               | 2x RP-SMA  |
| ASUS USB-AC56      | 5.8 - 2.4* | 500mW    | RTL8812AU | X         | X   |               | 2x RP-SMA  |
| "Taobao Card"      | 5.8 - 2.4* | 500mW    | RTL8812AU | X         | X   | X             | 2x u.fl    |
| ALFA AWUS1900      | 5.8 - 2.4* | 500mW    | RTL8814AU | X         | ?   |               | 4x RP-SMA  |
| Tenda U12          | 5.8 - 2.4* | 100mW    | RTL8812AU | X         | X   |               | 2x u.fl 2x internal |
| Cudy AC 1300       | 5.8        | ? low power | RTL8812BU |           | X   |               | internal   |
| Aigital AC1200     | 5.8        | ? low power | RTL8812BU |           | X   |               | internal   |
| COMFAST 1300Mbps   | 5.8        | ? low power | RTL8812BU |           | X   |               | internal   |
| Netgear A6100      | 5.8 - 2.4* | 50mW     | RTL8811AU |           | X   |               | 1x internal|

*We recommend using this chipset in 5.8GHz mode.

Please note that this list includes tested devices, but there are many more supported devices.

## Additional WiFi Devices with Reduced Functions

| Name               | Band  | TX Power | Chip     | STBC/LDPC | RC  | Need Heatsink | Antennas   |
| :----------------- | :---- | :------- | :------- | :-------- | :-- | :------------ | :--------- |
| ALFA AWUS036NHA    | 2.3-2.4 | 280mW | AR9271 |           | X   |               | 1x RP-SMA  |
| Ubiquiti Wifistation | 2.3-2.4 | 800mW+ | AR9271 |         | X   |               | 1x RP-SMA  |
| TPLink TL-WN722N V1 | 2.3-2.4 | 60mW  | AR9271 |           | X   |               | 1x RP-SMA  |
| AW-NU138           | 2.3-2.4 | 50mW   | AR9271 |           | X   | X             | 1x Internal |
| AW-NU137           | 2.3-2.4 | 70mW   | AR9271 |           | X   |               | 1x u.fl    |

*We recommend using this chipset in 5.8GHz mode.

These devices are supported but do not have all functions like 40MHz mode or different MCS-Indexes.

## ASUS AC56

The ASUS AC56 adapter is currently the most popular choice for OpenHD. Its small size makes it easy to fit into many builds, it uses 5.8GHz, and it is widely available. While the retail price can be high, it is often available used or on sale for $30 or less. It has one internal antenna, and the second antenna is optional, connecting with RP-SMA.

- [FCC info](https://fccid.io/MSQ-USBAC56)
- [WikiDevi](https://deviwiki.com/wiki/ASUS_USB-AC56)
- [Modification Page](https://forum.openhdfpv.org/t/asus-usb-ac56-wiring-antennas-etc/103)

## Taobao Card

![Taobao Card](https://github.com/OpenHD/OpenHD/blob/2.3-evo/wiki-content/Hardware_Supported%20WiFi%20adapters/taobaocard.jpg?raw=true)

[Store link](https://a.aliexpress.com/_rIjofM)

The Taobao Card is a generic RTL8812AU card sold on Taobao, from which it gets its name. It is widely used and known to work well, but it tends to get hot. The reported power output is 500mW. This card requires soldered wiring, or the USB connection may disconnect before or even during flight. It supports 2x u.fl antenna connectors.

## Finding Alternatives

For affordable alternatives, check out computer stores and consider Aliexpress. Exercise caution, as some cards may have questionable quality. Generally, high-quality or brand-name modules with RTL8812AU chipsets perform best.

To discover more about WiFi sticks and modules offered online, look for product numbers, chipsets, or FCC IDs. Search for high-resolution internal photos of the cards to identify the chipset and amplifiers used. You can also use helpful websites like:

- [FCC ID](https://fccid.io/) (FCC documents with internal photos)
- [WikiDevi](https://wikidevi.com/wiki/) (General information and sometimes photos)

When you find photos, search for the amplifier numbers to find datasheets that provide rough estimates of the expected output power.

Please consider reporting your findings if you've tried a WiFi card that is not listed here.

## External Amplifiers

Another way to increase output power is to use a low-power WiFi stick combined with an external amplifier.
