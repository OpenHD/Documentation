# Supported SBC's

While support for SBC's other than the Raspberry Pi is underway, currently the only officially supported devices are:

| SBC                                   | AIR | GROUND | Notes |
| ------------------------------------- | :-: | :----: | ----- |
| Raspberry Pi 2B+                      |  ✔  |    ❌   |       |
| Raspberry Pi 3A                       |  ✔  |    ❌   | 1     |
| Raspberry Pi 3A+                      |  ✔  |    ❌   | 1     |
| Raspberry Pi 3B                       |  ✔  |    ✔   | 2     |
| Pi 3B mini (unofficial)               |  ✔  |    ❌   | 2     |
| Raspberry Pi 3B+                      |  ✔  |    ✔   |       |
| Raspberry Pi 4B                       |  ✔  |    ✔   |       |
| Raspberry Pi Zero (not recommended)   |  ✔  |    ❌   | 1     |
| Raspberry Pi Zero W (not recommended) |  ✔  |    ❌   | 1     |
| Raspberry Pi Zero 2 W                 |  ✔  |    ❌   | 1, 4  |
| Raspberry Pi Compute Module CM3+      |  ✔  |    ✔   | 3     |

1. it is **not** a good **idea** to use a Pi **Zero**, Pi **Zero 2 W** or a Pi **3A(+)** on the **ground** side, you **may** get it to **work** but the resource requirements (particularly GPU **memory**) on the ground are **higher** than they are on the **air** side.
2. Will **work** but does **not** have internal dual band **hotspot** which will reduce functionality
3. Requires a `dt-blob.bin` file for your **carrier** board when used as AIR to support **dual cameras** at the moment, ask for help in Telegram
4. Zero 2w is currently supported by replacing files 0n the SD with the files available on the telegram user group or from this forum post [Zero 2 W Post](https://forum.openhdfpv.org/t/open-hd-not-booting-on-zero-2-w). Once the SD has been flashed, before booting use a pc to replace the files in the boot partition. In future OpenHD will support this board on the defualt image.

### Future support

The team is hard at work to support more SBC's. Active development is done on these SBC's:

* NVIDIA Jetson (series)
* NanoPi (series)

If you want to participate in the development, please reach out to us to see how you can help.
