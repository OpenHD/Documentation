# SBC's

{% hint style="info" %}
Single Board Computers are little computer's like the Raspberry Pi, which are build to run computing tasks efficiently and without additional components. For the sake of simplicity we also include X86-Computers to that definition, even if they aren't sbc's at all.
{% endhint %}

Starting with the evo releases OpenHD managed the step to be less platform independend, which means that we not only support the RaspberryPi, but can be used on multiple platforms. 

Currently OpenHD supports : X86,RPI,Rock5 and our Custom Hardware.

Our [custom Hardware](custom-hardware.md) will allow the low latency features so many users requested, while also giving superb image quality and size.

### Latency considerations

Lowest latency can be achieved with OpenHD-Custom Hardware. Because of carefully selected SBC and Camera and a little "magic", which can't be reproduced on "normal" SBC's. This has the ability to cut the latency in half.

Second lowest latency can be archieved with Rock5, which can hardware encode in realtime h265.

For receiving lowest latency, currently the Rock5 or a X86 System with great performance is needed.
