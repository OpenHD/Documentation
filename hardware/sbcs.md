# Single Board Computers

{% hint style="info" %}
Single Board Computers are little computer's like the Raspberry Pi, which are build to run computing tasks efficiently and without additional components. 
For the sake of simplicity we also include X86-Computers to that definition, even if they aren't sbc's at all.
{% endhint %}

With the 2.2-evo releases OpenHD managed the step to be less platform independend, which means that we not only support the RaspberryPi, but can be used on multiple platforms.
This step also complicates setup a little, because not every device is compatible with any sbc.

That's why we split our Wiki in multiple sub-menus.
Since the [RaspberryPi](../hardware/raspberry.md) is the most stable and most supported SBC we'll recommend starting with that platform.

We also support more advanced setups, which require much more work and have a lesser function set.
One of this Platforms is the [Nvidia Jetson](../hardware/jetson.md), which can only be used as Air, and has minimal camera support.

And [X86](../hardware/X86.md), which doesn't support custom channels and higher tx power on 2.4 cards.

In addition to that we are right now building our own [custom Hardware](../hardware/custom-hardware.md), which has very specific compatibilities. And allow custom builds based on our OpenHD code, which are compatible with the OpenHD-System.

{% hint style="danger" %}
Currently we only support RaspberryPi and X86 for the GroundSBC
{% endhint %}

### Latency considerations

Lowest latency can be achieved with OpenHD-Custom Hardware. Because of carefully selected SBC and Camera and a little "magic", which can't be reproduced on "normal" SBC's. This has the ability to cut the latency in half.

Second lowest latency can be archieved with an SBC, which can hardware encode in h265. Currently only Jetson Nano can do this, but other Hardware will follow.

For receiving lowest latency, currently the Pi4 or a X86 System with great performance is needed.