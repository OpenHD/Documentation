# Supported SBC's

While support for SBC's other than the Raspberry Pi is underway, currently the only officially supported devices are:

| SBC | AIR | GROUND | Notes |
| :--- | :---: | :---: | :--- |
| Raspberry Pi 2B+ | ✔ | ❌ |  |
| Raspberry Pi 3A | ✔ | ❌ | 1 |
| Raspberry Pi 3A+ | ✔ | ❌ | 1 |
| Raspberry Pi 3B | ✔ | ✔ | 2 |
| Raspberry Pi 3B+ | ✔ | ✔ |  |
| Raspberry Pi 4B | ✔ | ✔ |  |
| Raspberry Pi Zero | ✔ | ❌ | 1 |
| Raspberry Pi Zero W | ✔ | ❌ | 1 |
| Raspberry Pi Compute Module CM3+ | ✔ | ✔ | 3 |

1. it is **not** a good **idea** to use a Pi **Zero** or a Pi **3A\(+\)** on the **ground** side, you **may** get it to **work** but the resource requirements \(particularly GPU **memory**\) on the ground are **higher** than they are on the **air** side.
2. Will **work** but does **not** have internal dual band **hotspot** which will reduce functionality
3. Requires a `dt-blob.bin` file for your **carrier** board when used as AIR to support **dual cameras** at the moment, ask for help in Telegram

### Future support

The team is hard at work to support more SBC's. Active development is done on these SBC's:

* NVIDIA Jetson \(series\)
* NanoPi \(series\)

If you want to participate in the development, please reach out to us to see how you can help.

