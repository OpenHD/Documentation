# Cameras

### Overview

The Jetson Nano does not support every camera, which is supported by the RaspberryPi.

Currently the Support is limited to 

| Camera                                |  Notes  |
| ------------------------------------- | :-----: |
| IMX219                                |         |
| IMX477                                |  1      |
| Veye-Camera                           |  2      |


1. To activate IMX477 support you need to use our Configuator or add a IMX477.txt file to the /boot/OpenHD folder
2. Veye-Camera does only support h264 and has a higher latency then the others, but is much more low light capable. 