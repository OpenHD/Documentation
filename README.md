# Introduction

![](.gitbook/assets/plain\_openhd\_logo.jpg)

Welcome to the Open.HD Introduction Page!

OpenHD uses off-the-shelf Wi-Fi adapters available for purchase online, however it is not standard Wi-Fi, which is unsuitable for low-latency or very long distance transmission. Instead, Open.HD configures the Wi-Fi adapter in a way that is closer to a simple broadcast, much like analog video transmission hardware you may be using already.

High definition video, 2-way UAV telemetry, audio, and RC control signals can all be sent over a single transmission channel.

A multi-platform [Open.HD app ](https://github.com/OpenHD/QOpenHD/releases)is available for live video with a customizable OSD.

**For support and further reading:**

* [OpenHD Forum](https://discuss.openhdfpv.com)
* Public [Telegram](https://t.me/OpenHD\_User) and [Discord](https://discord.gg/N685WjnF) groups for lots of immediate interaction
* Please document problems on [Github](https://github.com/OpenHD/Open.HD/issues)
* First Intro to Open.HD from CurryKitten on [Youtube](https://www.youtube.com/playlist?list=PL7WaECFssECJWfTc0vKYTfUdH5y8UgdI9) (2 of x parts availible)

{% hint style="warning" %}
If you have a problem with a specific version of Open.HD, please check the name of the image you used to burn your SD cards and provide it to us in Telegram so we can help narrow down the cause and find a solution.
{% endhint %}

{% hint style="info" %}
&#x20;If you don't have or remember the version of Open.HD you used for your SD cards, you can find out what it was by looking in the `root` partition of the image (either connect the SD card it to a Linux machine or connect to the pi via SSH). There will be a file called `/openhd_version.txt` containing the exact version of the image.
{% endhint %}
