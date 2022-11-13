---
description: Flash your air and ground unit with OpenHD firmware
---

## Requirements:

1. A windows or linux PC (otherwise, read "manual install" below)
2. 
    a) SD card reader and a high quality SD card at least 16GB in size (Rpi only needs 8GB)

    b) High quality USB cable (if you use Hardware with internal memory (e.g. Ochin & CM4 with eMMC))


# Installation Guide

Step 1: 
Download and install the latest OpenHD imager (based on rpi imager) from 
[https://github.com/OpenHD/OpenHD-ImageWriter](https://github.com/OpenHD/OpenHD-ImageWriter)
![](<.gitbook/assets/Screenshot from 2022-11-12 16-46-44.png>)


Step 1.1: 
(Only CM4 with emmc): Connect your CM4 via USB and initialize flashing (TODO)

Step 3:
Open up the imager and select the latest OpenHD release from the drop down. The imager will automatically download the selected image. You can also download the image manually and flash it using the "Custom image" selector. Make sure to unzipp the image externally first, then select the .img file (Not the .zip file)

![](<.gitbook/assets/Screenshot from 2022-11-12 16-47-39.png>)

Step 4:
Insert your SD card into the card reader, and select it from the "Choose storage" option. If you are using a CM4, it'l show up like an SD card.

Step 5:
Click on "Settings" on the lower right corner and select either air or ground (depending weather you want to flash an air or ground image). You cannot skip this step. For a functional OpenHD setup, you need to flash one Air unit (select air) and one Ground unit (select ground).

Step 6:
Flash your image by clicking on "Write". This might take a while. 


### Manual install:
You can always flash OpenHD image(s) with the flashing tool of your choice. Note that in this case, you have to manually specify weather you want to boot as air or ground after flashing.
For air: Create a file called air.tx under /boot/OpenHD/
For ground: Create a file ground.txt under /boot/OpenHD/

Note: Filenames are case-sensitive. If you want to switch from air to ground, it is recommended to reflash your image, then create the air or ground file.
