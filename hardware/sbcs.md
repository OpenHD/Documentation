# Single Board Computers

{% hint style="info" %}
Single Board Computers are little computer's like the Raspberry Pi, which are build to run computing tasks efficiently and without additional components. 
For the sake of simplicity we also include X86-Computers to that definition, even if they aren't sbc's at all.
{% endhint %}

With the 2.2-evo releases OpenHD managed the step to be less platform independend, which means that we not only support the RaspberryPi, but can add additional platforms in the future.
This step also complicates setup a little, because not every device is compatible with any sbc.

That's why we split our Wiki in multiple sub-menus.
Since the [RaspberryPi](../hardware/raspberry.md) is the most stable and most supported SBC we'll recommend starting with that platform.

We also support more advanced setups, which require much more work.
One of this Platforms is the Nvidia Jetson and X86, for which we also actively build images.

In addition to that we are right now building our own custom Hardware, which has very specific compatibilities. And allow custom builds based on our OpenHD code, which are compatible with the OpenHD-System.

{% hint style="danger" %}
Currently we only support RaspberryPi and X86 for the GroundSBC
{% endhint %}

