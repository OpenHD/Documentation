# SBC's

While support for SBC's other than the Raspberry Pi is underway, currently the only officially supported devices are:

| SBC                                   |  AIR      | GND | Notes | recommended for   |
| ------------------------------------- | :-------: | :-: | ----- | :---------------: |
| Raspberry Pi 2B+                      |  yes      |  no |       |                   |
| Raspberry Pi 3A                       |  yes      |  no | 1     |                   |
| Raspberry Pi 3A+                      |  yes      |  no | 1     |                   |
| Raspberry Pi 3B                       |  yes      | yes | 2     |                   |
| Raspberry Pi 3B+                      |  yes      | yes |       |                   |
| Raspberry Pi 4B                       |  yes      | yes |       |       Ground      |
| Raspberry Pi Zero (not recommended)   |  no       |  no | 4     |                   |
| Raspberry Pi Zero W (not recommended) |  no       |  no | 4     |                   |
| Raspberry Pi Zero 2                   |  yes      |  no |       |                   |
| Raspberry Pi Zero 2 W                 |  yes      |  no |       |                   |
| Raspberry Pi Compute Module CM3+      |  yes      | yes | 3     |                   |
| Raspberry Pi Compute Module CM4       |  yes      | yes | 3     |       Ground      |
| Jetson Nano 2gb                       |  yes      | yes |       |         Air       |
| Jetson Nano 4gb                       |  yes      | yes |       |         Air       |



1. it is not a good idea to use a Pi Zero or a Pi 3A(+) on the ground side, you may get it to work but the resource requirements (particularly GPU memory) on the ground are higher than they are on the air side.
2. Will work but does not have internal dual band hotspot which will reduce functionality
3. Requires a dt-blob.bin file for your carrier board when used as AIR to support dual cameras at the moment, ask for help in Telegram
4. There is a small possibility that those boards are readded later in the developing phase with reduced features and significantly more latency
