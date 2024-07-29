# ochin_CM4v2 Board

The ochin_CM4v2 board is a carrier board for the Raspberry Pi CM4 module, designed to expose the connections to the peripherals made available by the CM4 module.

## Overview

This summary is intended to facilitate the installation and use of the ochin_CM4v2 with OpenHD software.

For more detailed documents, please follow the official GitHub links:  
* [ochin_CM4v2 user manual](https://github.com/ochin-space/ochin-CM4v2/blob/master/%C3%B6ch%C3%ACn%20CM4v2%20-%20Manual.pdf)  
* [ochin_CM4v2 quick start flashing guide](https://github.com/ochin-space/ochin-CM4v2/blob/master/%C3%B6ch%C3%ACn%20CM4v2%20-%20Quick%20Start%20Flashing%20Guide.png)  
* [ochin_CM4v2 wiring and suggestions](https://github.com/ochin-space/ochin-CM4v2/blob/master/%C3%B6ch%C3%ACn%20CM4v2%20-%20Wiring%20and%20Suggestions.pdf)  
* [ochin_CM4v2 GitHub repository](https://github.com/ochin-space/ochin-CM4v2)

## Specifications

The ochin_CM4v2 carrier board includes the following features:
* 4x USB 2.0 480Mbps (4x SM04B-GHS-TB(LF)(SN) connectors)
* 1x USB Type-C (for flashing eMMC)
* 2x CSI camera (2x FH12-22S-0.5SH (55) connectors)
* I2C1 (SM04B-GHS-TB(LF)(SN) connector)
* SPI1 / 6 (SM06B-GHS-TB(LF)(SN) connector)
* UART0 / 1 + Video Out (SM06B-GHS-TB(LF)(SN) connector)
* UART4 / UART5 (SM06B-GHS-TB(LF)(SN) connector)
* 1x Ethernet transformerless 100Base-T
* 1x microHDMI
* 2x general purpose LEDs
* 1x RGB LED on external tiny board
* 1x general purpose button on external tiny board

## Wiring

![wiring](https://raw.githubusercontent.com/OpenHD/Documentation/evo/.gitbook/assets/Ochinv2-1.png)
![ext-board](https://raw.githubusercontent.com/OpenHD/Documentation/evo/.gitbook/assets/Ochinv2-2.png)
![underside](https://raw.githubusercontent.com/OpenHD/Documentation/evo/.gitbook/assets/Ochinv2-3.png)
![button](https://raw.githubusercontent.com/OpenHD/Documentation/evo/.gitbook/assets/Ochinv2-4.png)

## Preliminary Considerations

1. The ochin_CM4v2 now supports the uHDMI video output. It is designed to be used both on the “air” and on the “ground” side.
2. The ochin_CM4 does not have a slot for the microSD; it is mandatory to use Raspberry Pi CM4 modules with eMMC (not lite).
3. The Raspberry Pi CM4 module gets pretty hot very quickly, please use an adequate heatsink.
4. The ochin_CM4 cannot be powered via the USB-C connector. The Type-C connector is only used for writing the eMMC.
5. The CSI flat cable is very close to the USBs and is prone to RF noise. It’s suggested to shield the flat cable with copper tape (or at least alu tape).
6. The USB WiFi dongle will draw some Amps, please use supply cables of adequate size between the ochin_CM4 board and the USB dongle.

## Installation and Connections

### Power Supply

The ochin_CM4v2 board is equipped with a 5VDC switching regulator necessary to power the CM4 module and all the peripherals connected to it. The regulator can accept input voltages from 7.5VDC to 28VDC (LiPo from 2S to 7S) and provide output currents up to 7A. It is possible to use the VBUS of the USB ports also to power the WiFi module. The board is equipped with a current switch that cuts the VBUS for currents higher than 3A to protect the CM4 module. It is possible to bypass the current switch if more current is needed on the VBUS, waiving the VBUS safety (see the ochin_CM4 board manual).

### CM4 Module Installation and Flash

The CM4 connectors are delicate and dense. Ensure no dust or debris is on the connectors before positioning the CM4 module. Gently place the module on the connectors until they snap into place. Press the two long edges of the CM4 module until the connectors are fully inserted. Limit disassembly to avoid damaging the connector contacts.

![right](https://raw.githubusercontent.com/OpenHD/Documentation/evo/.gitbook/assets/Ochinv2-5.png)
![wrong](https://raw.githubusercontent.com/OpenHD/Documentation/evo/.gitbook/assets/Ochinv2-6.png)

To remove the CM4 module from the ochin board, use the proper extractor. The .STL files for printing the extractor can be found in the “3D” section of the GitHub repository.

![tools](https://raw.githubusercontent.com/OpenHD/Documentation/evo/.gitbook/assets/Ochin5.png)
![tools2](https://raw.githubusercontent.com/OpenHD/Documentation/evo/.gitbook/assets/Ochin6.png)
![tools3](https://raw.githubusercontent.com/OpenHD/Documentation/evo/.gitbook/assets/Ochin7.png)

### Flashing the CM4 eMMC

1. Power up the board with boot configuration as a “mass storage device”.
   * Power off the board (no Vin connected)
   * Press the “nRPiboot” button on the tiny external board and, keeping it pressed, power up the board using the “Vin” Connector.
   * Connect the board to your PC using the USB Type-C port.

![board](https://raw.githubusercontent.com/OpenHD/Documentation/evo/.gitbook/assets/Ochinv2-8.png)

2. Run the “RPiboot” software, downloaded from the Raspberry Pi [website](https://github.com/raspberrypi/usbboot/raw/master/win32/rpiboot_setup.exe). The PC will see the eMMC partition as if it were an SD card in the SD card reader.
3. Flash the eMMC using the OpenHD imageWriter.

### Connecting the CSI Camera

The CSI camera can be connected to one of the two FFC connectors. The copper contacts of the flat cable must be oriented PCB-side.

### Connecting the WiFi Dongle

The WiFi dongle can be connected to one of the 4 USB connectors on the board. It is advisable to cut a USB extender and solder it to a GHS connector, keeping the wires on the connector side as short as possible.

![connection1](https://raw.githubusercontent.com/OpenHD/Documentation/evo/.gitbook/assets/Ochin9.png)
![connection2](https://raw.githubusercontent.com/OpenHD/Documentation/evo/.gitbook/assets/Ochin10.png)

### Connecting the Telemetry

To connect the telemetry to the FC, use one of the available UART ports. The default UART is UART0 / 1. Ensure that the logic levels of the FC UART are 0V-3V3, as the GPIOs of the CM4 module are not 5V tolerant.

![telemetry](https://raw.githubusercontent.com/OpenHD/Documentation/evo/.gitbook/assets/Ochin11.png)

## Where to Buy the Ochin?

[Purchase the Ochin CM4v2 board here](https://www.seeedstudio.com/Ochin-Tiny-Carrier-Board-for-Raspberry-Pi-Compute-Module-4-p-5463.html).
