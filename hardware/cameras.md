# Cameras

OpenHD supports and recommends the following cameras on the Raspberry Pi:

### Supports: 
Can be enabled and used easily (No custom scripting), in case things don't work you can ask us for help.

### Recommends:
They provide unique benefits, like superb image quality, low latency, a good feature set and/or professional use cases.

### Raspberry Pi foundation CSI cameras


| Name                                                                    | Sensor | Field of use    | Price | Overlay |
| ----------------------------------------------------------------------- | ------ | --------------- | ----- | ------- |         
| [Pi Cam V1](https://www.raspberrypi.org/documentation/hardware/camera/) | OV5647 | Normal          | $25   |   MMAL  |  
| [Pi Cam V2](https://www.raspberrypi.org/documentation/hardware/camera/) | IMX219 | Normal          | $25   |   MMAL  |  
| [Pi Cam HQ](https://www.raspberrypi.org/documentation/hardware/camera/) | IMX477 | Bigger Vehicles | $50   |   MMAL  |  


### Arducam CSI cameras

| Name                                                                                                                                                                                                                                            | Field of use    | Price |      Overlay       |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------- | ----- | ------------------ |
| [Arducam IMX477 Mini](https://www.arducam.com/product/arducam-12mp-imx477-mini-high-quality-camera-module-for-raspberry-pi/)                                                                                                                    | Normal          | $75   |  libcamera_imx477  |
| [Arducam IMX462](https://www.uctronics.com/arducam-for-raspberry-pi-ultra-low-light-camera-1080p-hd-wide-angle-pivariety-camera-module-based-on-1-2-7inch-2mp-starvis-sensor-imx462-compatible-with-raspberry-pi-isp-and-gstreamer-plugin.html) | Low Light       | $60   |  libcamera_arducam |
| [Arducam IMX519 MINI (FIXED FOCUS)](https://www.arducam.com/product/arducam-mini-16mp-imx519-camera-module-for-raspberry-pi-zero-b0391/)                                                                                                        | HQ mini         | $35   |  libcamera_imx519  |
| [Arducam 2MP Ultra Low Light STARVIS IMX290](https://www.uctronics.com/presale-arducam-2mp-ultra-low-light-starvis-imx290-motorized-ir-cut-camera-for-raspberry-pi.html)                                                                        | Low Light       | $30   |  libcamera_imx290  |
| [Arducam 2MP Ultra Low Light STARVIS IMX327](https://www.uctronics.com/presale-arducam-2mp-ultra-low-light-starvis-imx327-motorized-ir-cut-camera-for-raspberry-pi.html)                                                                        | Low Light       | $30   |  libcamera_imx327  |
| [Arducam 2MP Ultra Low Light STARVIS IMX462](https://www.uctronics.com/arducam-2mp-ultra-low-light-starvis-imx462-motorized-ir-cut-camera-for-raspberry-pi.html)                                                                                | Low Light       | $60   |  libcamera_imx462  |


### Veye CSI cameras

| Name                                                                          |               Field of use                | Price |    Overlay    |
| -----------------------------------------------------------------------       |              ---------------              | ----- | ------------- |
| [VEYE 327E](http://www.veye.cc/en/product/veye-mipi-327e/)                    | Low Light                                 | $90   |   veye_cam2m  |
| [VEYE IMX307](http://www.veye.cc/en/product/cs-mipi-imx307/)                  | Low Light, variable Framerate/Resolution  | $60   | veye_csimx307 |
| [VEYE IMX462](http://www.veye.cc/en/product/veye-mipi-imx462/)                | Low Light                                 | $80   |   veye_cam2m  |
| [VEYE IMX385](http://www.veye.cc/en/product/veye-mipi-imx385/)                | Ultra Low Light                           | $80   |   veye_cam2m  |
| [Innomaker IMX290](https://www.inno-maker.com/product/mipi-cam-290/)          | Low Light                                 | $90   |     veye327   |

### Thermal/USB Cameras


| Name | Lens | Sensor | Resolution | FPS |
| :--- | :--- | :--- | :--- | :--- |
| Hti-201 | Chalcogenide | Raytheon | 320x240 | 9hz | 
| Hti-301 | Germanium | iRay | 384x288 | 25hz |
| FLIR Boson 320 | Germanium | FLIR | 320x256 | 9hz/60hz | 
| FLIR Boson 640 | Germanium | FLIR | 640x512 | 9hz/60hz |

[more information](special-camera.md) 


### HDMI CSI Adapter


| Name | Csi lanes |  Resolution |
| :--- | :--- | :--- |
| [HC100F](https://www.waveshare.com/hdmi-to-csi-adapter.htm) | 2 | up to 1080p@30fps |
| [Geekworn C779](https://geekworm.com/products/raspberry-pi-hdmi-to-csi-2-adapter-board-with-15-pin-ffc-cable) | 2 | up to 1080p@30fps |
| [Geekworm C790](https://geekworm.com/products/c790?_pos=1&_sid=605794d2b&_ss=r)  | 4  | up to 1080p@30fps |

More information about CSI-HDMI can be found [here](hdmi-cameras.md).

### USB Cameras

[Read here](usb-camera.md) 

### IP Cameras

[Read here](ip-cameras.md)

### Get your camera supported !

Cameras not listed here may potentionally work, but aren't tested and configured.

We only integrate Cameras which are tested and fitting to the purpose of openhd.
If you want to get new cameras supported ask your camera vender to support OpenHD development with their hardware, 
but contact us first at developer@openhdfpv.org

{% hint style="danger" %}
While many cameras can potentially work, latency is the biggest issue. Please read the Camera pages to fully understand all variables.
{% endhint %}

{% hint style="danger" %}
When using multiple Cameras you need to choose one Camera-Subsystem, so you can not use libcamera and raspicam at the same time.
This means f.e. you can not use an Veye-Camera and an Arducam camera at the same time.
{% endhint %}

{% hint style="danger" %}
When using multiple Cameras the second camera is using Software decoding and encoding, it is not recommended to use a high quality camera. It is generally made for a thermal camera or something with lower resolutions.
{% endhint %}

{% hint style="danger" %}
With the upcoming of many new camera's there is one thing we need to mention.
OpenHD is not supporting ANY autofocus cameras, since they are basically not usable on equipment with vibrations (like drones), this also includes the Raspberry V3-lineup
{% endhint %}