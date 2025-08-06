# Radxa Rock SBC's

<!-- LEGACY DOCUMENTATION NOTICE -->
> ⚠️ **This documentation is outdated!** A current version is available at [openhdfpv.org](https://openhdfpv.org)
> 
> [📖 **View Updated Version of This Page** →](https://openhdfpv.org)

---


The Radxa Single Board Computers (SBCs) are highly capable devices that offer significantly higher performance compared to the Raspberry Pi. Due to their impressive capabilities, we have incorporated support for Radxa SBCs in our 2.4-Evo releases and newer.

However, it's important to note that the software development for Radxa SBCs is currently in its early stages. We recommend using them primarily on the ground where hardware decoding support is only partially functional. Despite this limitation, the performance is still superior to that of the Raspberry Pi.

At present, there is only one camera available for Radxa SBCs, namely the IMX415, which may not meet the requirements of OpenHD. To address this limitation, we are actively collaborating with Arducam to develop and offer better camera options for Radxa SBCs.

For it there is a initial pipeline included, but it may not function well. We're also working on a HDMI pipeline and the integration for this. But keep in mind that only the Rock5B does have this functionality.

In the near future, we have plans to introduce support for the newest camera module from Arducam, the IMX462.

## Currently Supported Radxa SBCs

The following Radxa SBC models are currently supported:

| SBC                   | 
| --------------------- |
| Radxa Rock5B          |
| Radxa Rock5A          |

The following Radxa SBC models are currently being worked on:

| SBC                   | 
| --------------------- |
| Radxa CM3             |
| Core3566*             |
| Radxa Zero3W          |

*not technically radxa but we run radxa software on that board, it's also not the best working board, so it may take a lot of time until it is perfectly supported

## Radxa Zero3W pins
Even 7 keys mapped to GPIO pins, only Right/Left/Up/Down needed for joystick navigation.
| Function     | Pin#  | Pin#  | Function     |
| ---:         | :---: | :---: | :---         |
|              | 1     | 2     |              |
|              | 3     | 4     | 5V INPUT     |
|              | 5     | 6     | GNS          |
|              | 7     | 8     |              |
|              | 9     | 10    |              |
|              | 11    | 12    |              |
|              | 13    | 14    |              |
|              | 15    | 16    |              |
|              | 17    | 18    |              |
|              | 19    | 20    |              |
|              | 21    | 22    | Del key      |
|Backspace key | 23    | 24    |              |
|              | 25    | 26    |              |
|              | 27    | 28    |              |
|              | 29    | 30    |              |
|              | 31    | 32    |              |
|              | 33    | 34    |              |
|    Right key | 35    | 36    | Enter key    |
|     Left key | 37    | 38    | Down key     |
|              | 39    | 40    | Up key       |
