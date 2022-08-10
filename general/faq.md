# FAQ

#### What is the minimum hardware I need to try this?

Two Raspberry Pi, two supported WiFi adapters, one Pi cam \(Or CSI-HDMI Adapter\), and 2 good quality \(preferably Industrial micro SD Cards\). 

{% hint style="warning" %}
Please read the rest of the documentation and do your homework when you make your purchases! Only specific WiFi cards will work due to the unique requirements of the system.
{% endhint %}

#### What is the lowest latency I can achieve?

On a Raspberry Pi, 110ms “glass to glass”. Although most setups are in the 125ms range.

On other boards it can be significantly lower, as low as NOOFFICIALNUMBER has been demonstrated with the Jetson Nano and a carefully selected camera.

The lowest latency can be archieved with Custom Hardware, which is currently in development. (https://www.patreon.com/OpenHD)

#### What kind of range can I expect?

It depends, 1-3KM is easy to achieve even with low power WiFi cards and the antennas that come with them.

Carefully chosen WiFi cards, antennas, and optionally an antenna tracker should put 20KM+ within reach, and the current record is 75KM on 5.8Ghz frequency with a 30dbi gain panel antenna.

[60Km Flight](https://youtu.be/bcYOgW3WmS4)

How long does OpenHD take to regain a lost “connection”?

#Needs Testing
<!-- It depends on the kind of camera you are using, if it is a Raspberry Pi camera and the settings are still left on the defaults, the system should recover from serious interference within 300ms at most, more likely the interference will only partially disrupt the video and you will see momentary noise that will clear up rapidly.  -->

#### When I lose connection will I see a “blue screen”?

OpenHD does not generate a solid blue screen when interference is encountered. If experiencing a loss of signal you will see progressive artifacts and pixilation, finally the image typically freezes. The telemetry and/or RC link is more robust and will often continue to operate well beyond the loss of the video stream.

#### Does OpenHD interfere with my RC transmitter?

You can use 2 different bands, 5.8Ghz for OpenHD, and 2.4Ghz for RC. You can also send RC control through OpenHD itself, and avoid using 2 different transmitters. There are tradeoffs however, control latency may be slightly higher than a dedicated RC system, and there are currently some limitations on the channel count.

If you're planning a long range flight and have the "best" setup for range, we advise to use the OpenHD ControlLink, because even with carefully seperated frequencies the range can be affected by any radio signal, because it "increases the noise floor".

#### What is a Raspberry Pi?

A computer on a single circuit board. In this case running a derivative of Linux. Don't worry you do not need to know anything about the software side, we have that covered!

#### Do I need a WiFi adapters for video, another for telemetry, and another for RC control?

No, just one for ground and one for air.

You can optionally use 2x WiFi adapters on the ground side for "diversity", which improves signal reception.

#### Can I run OpenHD on this other board \(Orange Pi, Banana Pi, BeagleBoard\)?

In OpenHD 2.0, no. The system is designed around the Raspberry Pi as it is cheap, widely available, and the video encoder/decoder hardware works properly.

In OpenHD 2.2, most of the code has been rewritten, this means that we're much less hardware bound.
We support the Nvidia Jetson Platform, which will inprove latency a lot. We've also opend up the possibility to add other platforms, but those need long testing and evaluation and development work before being supported. This progress is quite a lot of work, so most boards will not get support ever. 


#### Which WiFi adapters do I need?

See the wiki: [Supported WiFi Adapters](link of the wifi-card-page)

#### Can I use this other WiFi adapter that’s not on the list?

Only a few WiFi adapters are able to work the way OpenHD needs them to, which limits the selection of WiFi adapters you can use.
We use a custom Kernel, which needs drivers for each new card. Basic requierements are Monitor Mode and Package injection.
If the card is stable in both and the injection rate is high enough we can potentionally integrate it.

#### Why can’t I just use the Raspberry Pi onboard WiFi?

The built-in WiFi chip on the Raspberry Pi does not work the way OpenHD needs it to for video broadcast, however it can still be used for "hotspot" purposes, the you can connect Android and other devices to the ground station over normal WiFi to receive the video signal.

#### Why can’t I use the wifi-hotspot on Nvidia Jetson?

The Jetson does not have an included wifi-card, so it can't be used to make a hotspot. But you can use usb-tethering or Ethernet.

#### Why am I seeing noise or interference in the video?

There are many possibilities.

You might be experiencing interference from normal WiFi devices. If that is the case, try another frequency or change location. In most cases if you are outside in a suitable location for flying, there are not many normal WiFi devices around.

If you have a long CSI camera cable attached, it may be generating or receiving interference. You can test this by wrapping it in foil or getting a shorter cable. The kind of interference you will see in this case is very specific, it will look like perfectly straight vertical lines.

The AirPi and GroundPi may also be too close together if you are testing on the ground, this can cause the receiving WiFi card to be overloaded.

It is generally necessary to solder power wires and even the USB data wires directly to the WiFi adapters. The Raspberry Pi USB ports are not capable of supplying enough power to cards that require a lot of it, and in some cases the USB connectors can briefly disconnect during flight which may lead to total video loss. if you are still seeing interference or even video freezes, this should be the next thing you address.

#### Why do I get a low power warning?

In OpenHD 2.2 you can get low poer warnings, when your BEC is not able to supply enough power. Please change it to a more powerfull one.
In addition to that carefully check and wire the WiFi cards correctly to avoid power issues.

#### How many WiFi adapters can I use?

Currently only one Wifi adapter is usable, but this will change in later releases.
<!-- 2x on the air side, 3x on the ground with a Pi3b+. If you are going to connect this many WiFi adapters you are strongly encouraged to use a Pi4b instead of a Pi3b+ for stability. -->

You can use 4x with a Pi4b, but this is overkill.

#### Where can I buy the hardware I need for OpenHD?

* eBay
* Amazon
* banggood.com
* AliExpress
* TaoBao \(chinese marketplace\)

Currently it's not that easy to buy all the hardware you need, just because of the Global Chip Shortage.
Try to use https://rpilocator.com/ or buy used Hardware

Keep in mind that OpenHD2.2 dropped support for Pi-Zero, Pi1, Pi2 (lower than 1.2)

#### Is OpenHD legal to use?

OpenHD uses normal WiFi hardware, which is perfectly legal to buy and use.

OpenHD can be disruptive to nearby WiFi networks due to the continuous broadcast, OpenHD starts with 25mw, which is allowed in every part of the world. But it can be set up to use power levels and frequencies, which might not be legal in your location.

You are responsible for your use of the system, but please ask us for advice if you are concerned about a particular setting or use case.

#### Can someone else watch my video stream?

Yes, you can receive the video with any GroundPi that is configured to the same frequency as your AirPi.

The system is not encrypted in OpenHD 2.2, encryption is currently not on the ToDo list, because we do not want any affiliation with military usage.

#### Where did my recorded video go?

See the wiki: [Ground Recording](https://github.com/OpenHD/Open.HD/wiki/Software-~-Advanced-~-Ground-Recording)

#### Why is the OSD not on the video recording?

Since the Video-Stream does not include the OSD, because it is overlayed by QOpenHD, it can not be directly recorded on the ground. However you can use a tethered device and record it's screen via e.g. OBS.

#### What is diversity?

A way to improve the reliability and quality of video reception.

Diversity is currently not enabled in 2.2 but will be added in later versions.

If you connect 2 or more WiFi adapters to the GroundPi, whichever adapter is currently receiving the best signal will be used. This is entirely automatic and occurs in realtime, you do not have to change any settings or monitor anything.

Some OpenHD users connect different kinds of antennas to the 2+ WiFi adapters, such as a directional antenna and a normal omnidirectional antenna. This allows for automatic switching from long range to short range, so that you don't have to keep your directional antenna pointed toward the UAV when it is nearby.

#### What is FEC/Forward Error Correction?

FEC is a way to add redundancy to the video stream.

Because the latency must be kept to a minimum, there is no opportunity to retransmit parts of the video that were distorted by interference. Instead the system will process the video in a way that allows for some of it to be lost in transmission, without affecting the received video on the GroundPi.

There is a cost to using FEC, the radio bandwidth is a little bit higher \(or viewed another way, the maximum video bitrate/quality is a little bit lower\). However it is mandatory for safe flight, without it the video would be very easily distorted.

#### Is latency going to improve in future updates?

Latency is almost entirely a result of the kind of video encoder and decoder hardware being used on the AirPi and GroundPi. And the latency of the HDMI-Screen.
With the Raspberry Pi, as encoder there is a lower limit to the minimum latency that can be achieved. 
h265 can lower the latency a lot, but there is no raspberrySBC which is able to encode h265, but the Nvidia jetson will reduce latency.

With custom Hardware we are able to reduce the latency even more, but NDA's forbid us to release how.

#### What do these numbers mean on the OSD display?

See  [Telemetry and OSD](../software-setup/telemetry-and-osd.md)

#### Which RC protocols are supported?

We reduced the RC protocols down to only MAVlink, because nearly every hardware supports Mavlink.

#### Which telemetry protocols are supported?

We reduced the telemetry protocols down to only MAVlink, because nearly every hardware supports Mavlink Telemetry.

#### What is an AirPi / GroundPi?

This is a shorter way to refer to which SBC is transmitting video and which one is transmitting RC and/or uplink telemetry.
Both are using the same images.

#### How about Circular vs. Linear polarized antennas?

Circular antennas are known to be very effective in suppressing signal reflections \(multi-pathing\), which degrades the quality of analogue transmission.

Digital systems are not affected by multi-pathing though \(and often can take advantage of it\). Circular antennas are not as important like they would be with an analog video system.

However, circular antennas still have some advantages compared to linear antennas:

* They work independent of angle to each other, almost no polarization losses
* Typically circular antennas have a lower gain, and thus higher opening angle than linear antennas
* Less susceptible to signal blocking from nearby solid objects

#### How can I support this project?

Use the system! There are a _lot_ of different features and settings and possible hardware combinations, it can be very difficult to test everything each time we release an update. As a result, we depend on users to tell use when something is wrong, or whether something should be improved.

We also frequently need translators who can read/write both english and another language, as the system supports translation in the OSD.

And of course if you have an idea for something you would like to see use add or change, let us know in Github Issues, on the Forum, Discord, or on Telegram.

If you want to support the project financially, you can do so via [OpenCollective](https://opencollective.com/openhd).

