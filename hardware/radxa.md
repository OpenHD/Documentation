# Radxa Rock SBC's

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
