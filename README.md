---
description: Welcome to OpenHD
---

# Introduction

&#x20;

<figure><img src=".gitbook/assets/plain_openhd_logo.jpg" alt=""><figcaption></figcaption></figure>

OpenHD is a suite of software designed for long-range video transmission, telemetry, and RC control. While we originally designed it with hobbyist drones in mind, it can be adapted to a wide range of other applications as well.

## What OpenHD Can Do

Our suite can transmit:


* High definition video (with multiple cameras)
* Two-way UAV telemetry
* Audio
* RC control signals


All of these signals can be sent over a single transmission channel.



## How OpenHD Works



We use off-the-shelf Wi-Fi adapters that are available for purchase online. However, we don't use standard Wi-Fi, which isn't well-suited for low-latency or long-distance transmissions. Instead, we configure the Wi-Fi adapter to operate like a simple broadcast, which is more similar to analog video transmission hardware.

This configuration allows us to transmit high-quality video and other signals over long distances with low latency.



## QOpenHD App

We offer a multi-platform [app](https://github.com/OpenHD/QOpenHD/releases) with a customizable on-screen display (OSD) for live video. The app is designed to work seamlessly with our suite, and allows you to easily view and control your transmission.



## Support and Further Reading

If you need help or want to learn more, we offer several resources:

* [OpenHD Forum](https://forum.openhdfpv.org/)
* Public [Telegram](https://t.me/OpenHD\_User) and [Discord](https://discord.gg/P9kXs9N2RP) groups for lots of immediate interaction
* Please document problems on [Github](https://github.com/OpenHD/OpenHD/issues)
* First intro to Open.HD from CurryKitten on [Youtube](https://www.youtube.com/playlist?list=PL7WaECFssECJWfTc0vKYTfUdH5y8UgdI9)

{% hint style="warning" %}
If you have a problem with a specific version of Open.HD, please check the name of the image you used to burn your SD cards and provide it to us in Telegram so we can help narrow down the cause and find a solution.
{% endhint %}

{% hint style="info" %}
If you activate debugging, detailed debug logs can be found on the SD-Card and should be provided, when discussing a problem.
{% endhint %}

We hope you find OpenHD useful, and we look forward to helping you get the most out of your long-range video transmission!
