# Antennas

The antennas are a key component for any radio link solution and the same for radio waves are applicable here. The right combination depends on the objectives, like short-range \(all-around flight\) or long-range flight for more advanced pilots. A good starting point is the default antennas for the wifi cards at the workbench \(omnidirectional\), once you get confident with the system during a line of sight and short flights, you can move with directional antennas.

As nothing is free, changing your antennas is a trade-off, while omnidirectional antennas give you autonomy to fly around your position, these antennas offer limited range, on the other side directional antennas concentrate the radiated pattern and allow a long-range at the cost of the need of pointing the antennas precisely, in other words, more antenna gains more directional. For the high directive antenna, add components like trackers are recommended to keep always pointing the main antenna pattern lobule to the aircraft.

####  

#### 5 TIPs for Antennas

1. Make sure you have proper wiring and you have followed all previous sections, wrong connections can lower your range or destroy your radio link.
2. Start simple using Omni antennas, and move with directional ones as you get more experience.
3. Make sure you use the same polarization on both sides, Vertical/Vertical, Horizontal/Horizontal. The cross-polarization can work but you will lose 3dB \(half of the power\).
4. Lower bands like 2.4GHz can benefit the range, however, in some areas, this band is highly polluted and you may consider 5.8GHz. Try changing also the channels in the selected band.
5. When using directional antennas \(meant for ground side\), always aligned with the airside, consider using ATT \(automatic antenna tracker\). Omnidirectional antennas are always recommended in the Airside.

The below link explains how the video quality is impacted under different scenarios. [https://www.youtube.com/watch?v=T78JRAELjec](https://www.youtube.com/watch?v=T78JRAELjec)

####  

#### Antenna Hardware

| Brand | Antenna | Polarization | Frequency GHz | Link \* |
| :--- | :--- | :--- | :--- | :--- |
| DYI | PCB Maple | Omni Vertical | 5.2-5.3 | [OpenHD maple leaf PCB 3dB](https://forum.openhdfpv.org/t/maple-leaf-pcb-antenna/460) |
| Maple | Flat Panel FY-05A | Directional Vertical | 5.8 | [Maple leaf 14dB](https://aliexpress.com/item/1005002007469173.html) |
| Maple | Planar Antenna | Directional Vertical | 5.8 | [Planar 17dB - Aliexpress](https://aliexpress.com/item/32989509234.html) |
| Interline | Panel | Directional Vertical | 5.8 | [IP-G23-F5258-HV](https://interline.pl/antennas/PANEL-23-5.2-5.8GHz) |
| uuustore | Flat Panel Antenna | Directional Vertical | 5.8 | [23dB Flat Panel Antenna - Aliexpress](https://de.aliexpress.com/item/2020415914.html?spm=a2g0o.productlist.0.0.39846db3fR96Ke&algo_pvid=8beb6030-48f5-490c-b558-2b6aec776e76&algo_exp_id=8beb6030-48f5-490c-b558-2b6aec776e76-1) |
| Aomway | Biquad | Directional Vertical | 5.8 | [Biquad Dual Diamond - Getfpv](https://www.getfpv.com/aomway-biquad-sma-5-8ghz-dual-diamond-directional-antenna.html) |
| DYI | Biquad Yagi Antenna | Directional | 2.4 |  [Thingiverse](https://www.thingiverse.com/thing:1720696) - [Diquad antenna calculator](https://www.changpuak.ch/electronics/bi_quad_antenna_designer.php) |
| DYI | PCB patch array | Directional | 2.4 / 5.8 | [Kent Electronics](http://www.wa5vjb.com/products6.html) |

\*Links are only for reference purposes. It will be added more as users report, check the connector type in order to make sure it will fit to your wifi card.

####  

#### Range Calculation

A typical question is related to the maximum range, link budget or system range have relation to three main elements: Transmitter power, Antenna gains, and Receiver sensitivity. The next formula can be used to calculate this:

`R = 10^( (Lfs-LM-32.44-20*Log(f)) / 20)`

`Lfs = Ptx + Gtx + Grx – Srx`

where,

* `R = range in Km`
* `f = frequency used MHz`
* `LM = Link Margin dB`
* `Lfs = free space path loss dB`
* `Gtx = Tx antenna gain dBi`
* `Grx = Rx antenna gain dBi`
* `Ptx = Tx power dBm`
* `Srx = Sensitivity Rx`

| Ground Side antenna / Gain | Air Side antenna / Gain | Frequency GHz | Power TX mW | Theoretical range Km \* | Notes |
| :--- | :--- | :--- | :--- | :--- | :--- |
| Maple 5dB Omni / 5dBi | Maple 5dBi Omni / 5dBi | 5.2GHz | 200 | 2.9 | Excellent upgrade for default antennas |
| Flat Panel Direct / 14dBi | Maple 5dBi / 5dBi | 5.2GHz | 200 | 8.2 | Directional antenna with ATT |
| Planar Direct / 17dBi | Omni / 5dBi | 5.8GHz | 500 | 16.37 | Directional antenna high range ATT |

\*Network card receiving sensitivity approx. -93dBm. Link margin assumed 10 dB

To understand the impact in range against the transmitter power, the below logarithmic graph shows some calculations using different antenna sets:

![range vs power graph](https://github.com/Andres-160/Open.HD/raw/master/wiki-content/Community_Pictures/FPV%20range.png)

