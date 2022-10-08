# Cameras

### Overview

{% hint style="danger" %}
Most USB Cameras will create higher latency.
{% endhint %}


| Name | Sensor | Field of use | Price |
| :--- | :--- | :--- | :--- |
 [Logitech C920](https://www.logitech.com/en-gb/product/hd-pro-webcam-c920) | -- | "lower latency*" | $95 |
| [C1 Micro](https://www.kurokesu.com/shop/cameras/CAMERA_C1_MICRO_M12) | AR0330 | micro | €112 |
| [C1](https://www.kurokesu.com/shop/cameras/CAMUSB1) | AR0330 | HQ | €100 | 
| [C1 Pro](https://www.kurokesu.com/shop/cameras/CAMERA_C1_PRO) | IMX290 | HQ | €139 |
| [e-con Hyperyon](https://www.e-consystems.com/usb-cameras/imx290-low-light-usb-camera.asp) | IMX290 | low light | $240 |


* for USB devices, not lower than CSI



### Logitech C920

Note that in recent years Logitech has been removing the h264 encoder from all of their webcams, if you buy one new it may not actually have an h264 encoder inside and that would prevent it from being used properly in OpenHD.

#### C1 series from Kurokesu

These are exceptionally well made USB h264 cameras built with high quality sensors and a Sonix chip to handle image processing and h264 encoding. Latency is reported to be 90-125ms minimum.

### e-con Systems Hyperyon

A USB h264 camera with an IMX290 sensor and an onboard ISP tuned for low light, also supports HDR/WDR. Should work with every board supported by Open.HD. It is expensive, but may be useful to someone.

Comes with an M12 lens with 132° FOV.

There are 2 boards, one with the camera sensor 40 mm x 25 mm, and the other 25 mm x 65 mm board contains the encoder and USB connector, the total weight for everything is 37.5g.

