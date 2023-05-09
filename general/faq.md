# FAQ



#### What is the minimum hardware I need to try this?

Two Raspberry Pis, two supported WiFi adapters, one Pi cam (Or CSI-HDMI adapter), and 2 good quality (preferably industrial micro SD cards).

{% hint style="warning" %}
Please read the rest of the documentation and do your homework when you make your purchases! Only specific WiFi cards will work due to the unique system requirements. Good results are only achieved with proper power supply and wiring!
{% endhint %}

#### What is the lowest latency I can achieve?

On a Raspberry Pi, 100ms “glass to glass”. Although most setups are in the 125ms range.

The easiest way to reduce latency is to use OpenHD on a "potent" X86 Laptop, it'll reduce the latency a lot. (This was tested on a "hp omen en1179ng" )

On a Jetson Nano as Air-SBC you can expect to lower the latency, but no official numbers are published yet.

The lowest latency can be achieved on our custom hardware combined with a X86-Ground. There are no official numbers yet, but you can expect to cut your latency in half, which makes OpenHD repsonsive enough to fly on race/freestyle-setups. It's not released yet, but you can follow our progress [on the OpenHD Hardware Patreon page](https://www.patreon.com/OpenHD).

#### What kind of range can I expect?

It depends. 1-3KM is easy to achieve, even with low power WiFi cards and the antennas that come with them.

Carefully chosen WiFi cards, antennas, and optionally an antenna tracker should put 20km+ within reach. The current record is 75km on 5.8GHz frequency with a 30dbi gain panel antenna.

- YouTube video of [60km flight](https://youtu.be/bcYOgW3WmS4)

- YouTube video of [75km flight](https://youtu.be/IVSJwuuuo7o?t=78)

#### How long does OpenHD take to regain a lost “connection”?

OpenHD is optimized to regain the connection fast and without interaction, the time it needs to reconnect is very low (can be counted in ms).

#### Will I see a blue screen when I lose connection?

OpenHD does not generate a solid blue screen when interference is encountered. When experiencing a loss of signal, you will see progressive artifacts and pixilation, finally the image freezes. The telemetry and/or RC link is more robust and will often continue to operate well beyond the loss of the video stream.

#### Does OpenHD interfere with my RC transmitter?

OpenHD generally operates in 5.8GHZ, but can also use the 2.4GHZ band (depending on your setup), which should allow you to choose a band your RC transmitter isn't using. You can also send RC control commands through OpenHD itself and thus avoid using 2 different transmitters. There are tradeoffs however. Control latency might be slightly higher than a dedicated RC system and there are currently some limitations on the channel count (16channels maximum).

If you're planning a long range flight and want to have the "best" setup for range, we advise you to use the OpenHD control link, since even with carefully seperated frequencies the range can be affected by any radio signal due to the increased noise floor.

#### What is a Raspberry Pi?

A computer on a single circuit board. In this case running a derivative of Linux. Don't worry, you do not need to know anything about the software side. We have that covered!

#### Do I need a WiFi adapter for video, another for telemetry and another for RC control?

No, just one adapter for ground and one for air. You can optionally use 2 WiFi adapters on the ground side for diversity, which improves signal reception.

#### Can I run OpenHD on different platforms ? (Orange Pi, Banana Pi, BeagleBone)?

In OpenHD > 2.2 most of the code has been rewritten. This means that we're much less hardware bound and support for new SBCs could be added in the future. Officially we currently differentiate between air and ground.

Ground:

The most optimized Platform on the ground is the Raspberry Pi, but if you have quite capable hardware, x86 will give you even better latency than the Pi.

{% hint style="warning" %}
Not every USB-port is able to supply the Wifi-Adapter with enough power. Please ensure enough power is supplied to the WiFi adapter before flying. The standard 500mA isn't enough. Also, if you do any PowerMods, we're not responsible for any potential damage.
{% endhint %}

{% hint style="warning" %}
Older computers or SBCs may not be fast enough to run OpenHD.
{% endhint %}

Air:

The lowest latency platform is our custom hardware. The second best latency will be achieved with on Jetson Nano (which as limited camera support). The most flexible platform will be the Pi, but it can only encode h.264 video, which will result in increased latency.

#### What about Orange Pi, Banana Pi, BeagleBone ?

Officially we can not support every platform, but we optimized OpenHD to be enable being ported to different SBCs.

{% hint style="warning" %}
Most SBC's have very limited camera support (since cameras need to be specifically adapted to the ISP) and doesn't make sense using as Air, which is a shame.
{% endhint %}

You can also run the groundstation (including QOpenHD) on different platforms, but since every SBC handles decoding/compositing/rendering differently, we can't really optimize everything and the workload for our devteam is limited. Therefore we only officially support Pi and x86 on the ground.

#### Which WiFi adapters do I need?

See [Supported WiFi Adapters](../hardware/wifi-adapters.md).

#### Can I use this other WiFi adapter that's not on the list?

Only a few WiFi adapters are able to work the way OpenHD needs them to, which limits the selection of WiFi adapters you can use. We use a custom kernel, which requires drivers for each new card. Basic requierements are monitor mode and packet injection. If the card is stable in both modes and the injection rate is high enough, we can potentionally integrate it.

#### Why can't I just use the Raspberry Pi onboard WiFi?

The built-in WiFi chip on the Raspberry Pi does not work the way OpenHD needs it to for video broadcast, however it can still be used for hotspot purposes, which allows you to connect Android and other devices to the ground station over normal WiFi in order to receive the video signal.

#### Why can't I use the WiFi-hotspot on Jetson Nano?

Jetson Nano does not have an included WiFi-card, so it can't be used to create a hotspot. You can use usb-tethering or ethernet though.

#### Why am I seeing noise or interference in the video?

There are many possible causes of interference.

You might be experiencing interference from normal WiFi devices nearby. If that is the case, try another frequency or change your physical location. In most cases if you are outside in a suitable location for flying, there are not many normal WiFi devices around.

If you have a long CSI camera cable attached, it may be generating or receiving interference. You can test this by wrapping it in copper foil or getting a shorter cable. The kind of interference you will see in this case is very specific, it will look like perfectly straight vertical lines.

The AirPi and GroundPi may also be too close to each other, if you are testing on the ground. This can cause the receiving WiFi card to be overloaded.

It is generally necessary to solder power wires and even the USB data wires directly to the WiFi adapters and Raspberry Pi. The Raspberry Pi's USB ports are not capable of supplying enough power to power hungry WiFi cards. In some cases the USB connectors can briefly disconnect during flight, which might lead to total video loss. If you are still seeing interference or even video freezes, this should be the next thing for you to address.

#### Why do I get a low power warning?

In OpenHD 2.3 you can get low power warnings when your BEC is not able to supply enough power. Please change it to a more powerful one. In addition to that, carefully check and wire the WiFi cards correctly in order to avoid power issues.

#### How many WiFi adapters can I use?

Two WiFi adapters on the Ground are supported.

#### Where can I buy the hardware I need for OpenHD?

* eBay
* Amazon
* banggood.com
* AliExpress
* TaoBao (chinese marketplace)

Due to the global chip shortage it is currently not that easy to buy all the required hardware. Try to use [rpilocator](https://rpilocator.com/) or buy used hardware.

Keep in mind that OpenHD 2.3 dropped support for Pi-Zero, Pi1 and Pi2 (lower than 1.2).

#### Is OpenHD legal to use?

OpenHD uses normal WiFi hardware, which is perfectly legal to buy and use.

OpenHD can be disruptive to nearby WiFi networks due to the continuous broadcast though. OpenHD starts at 25mW transmit power, which is allowed in every part of the world. It can be configured to use power levels and frequencies which might not be legal in your location, so please check your local regulations before use.

You are responsible for your use of the system, but please ask us for advice if you are concerned about a particular setting or use case.

#### Can someone else watch my video stream?

Yes, you can receive the video with any GroundPi that is configured to the same frequency as your AirPi.

In future releases we'll add a "BindMode" which will only allow people with a passphrase to view your video.

#### What is diversity?

A way to improve the reliability and quality of video reception.

Diversity is currently not enabled in 2.2, but will be added in later versions.

If you connect 2 or more WiFi adapters to the GroundPi, whichever adapter is currently receiving the best signal will be used. This is entirely automatic and occurs in realtime. You do not have to change any settings or monitor anything.

Some OpenHD users connect different kinds of antennas to the 2+ WiFi adapters, such as a directional antenna and a normal omnidirectional antenna. This allows for automatic switching from long range to short range, so that you don't have to keep your directional antenna pointed towards the UAV when it is nearby.

#### What is FEC/Forward Error Correction?

FEC is a way to add redundancy to the video stream.

Since the latency must be kept to a minimum, there is no opportunity to retransmit parts of the video that were distorted by interference. Instead, the system will process the video in a way that allows for some of the data to be lost in transmission, without affecting the received video on the GroundPi.

There is a cost to using FEC. The radio bandwidth is a little bit higher (or viewed another way, the maximum video bitrate/quality is a little bit lower). However it is mandatory for safe flight. Without FEC, the video would be very easily distorted.

#### Is latency going to improve in future updates?

In OpenHD 2.2 we started to highly focus on latency. The first releases will have a pretty average latency, but currently we're saving every ms we can. With 2.3 we returned to the same latency, which ez-wifibroadcast had, which was significantly lower than previous OpenHD releases. Thanks to the use of h.265 video encoding (not available on Raspberry Pi) and custom hardware we are able to reduce the latency even more.

#### What do these numbers mean on the OSD display?

See [Telemetry and OSD](../software-setup/telemetry-and-osd.md)

#### Which RC protocols are supported?

We reduced the RC protocols down to only MAVlink, since nearly every FC firmware supports MAVLink.

#### Which telemetry protocols are supported?

We reduced the telemetry protocols down to only MAVlink, since nearly every FC firmware supports MAVLink telemetry.

#### What is an AirSBC / GroundSBC?

This is a shorter way to refer to which SBC is transmitting video from the UAV and which SBC is transmitting RC and/or uplink telemetry. Both are using the same OS images.

#### How about Circular vs. Linear polarized antennas?

Circular antennas are known to be very effective in suppressing signal reflections (multi-pathing), which degrades the quality of analogue transmission.

Digital systems are not affected by multi-pathing though (and often can take advantage of it). Circular antennas are not as important as they would be with an analog video system.

However, circular antennas still have some advantages compared to linear antennas:

* They work independent of angle to each other, almost no polarization losses.
* Typically circular antennas have a lower gain, and thus higher opening angle than linear antennas.
* Less susceptible to signal blocking from nearby solid objects.

#### How can I support this project?

Use the system! There are a _lot_ of different features, settings and possible hardware combinations, it can be very difficult to test everything each time we release an update. As a result, we depend on users to tell us when something is wrong or if something should be improved.

If you have any development experiences and time, we're always open to new developers which want to help improve and extend our codebase.

We also frequently need translators who can read/write both english and another languages, as the system supports translation in the OSD.

And of course if you have an idea for something you would like to see us add or change, let us know in Github issues, on the Forum, Discord or on Telegram.

If you want to support the project financially, you can do so via [OpenCollective](https://opencollective.com/openhd).
