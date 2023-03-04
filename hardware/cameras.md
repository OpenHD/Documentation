# Cameras

OpenHD supports and recommends the following cameras on the Raspberry Pi:

### Supported Cameras \*

Can be enabled and used easily (No custom scripting), in case things don't work you can ask us for help.

### Recommended Cameras \*\*:

They provide unique benefits, like superb image quality, low latency, a good feature set and/or professional use cases.

### Raspberry Pi CSI cameras

<table><thead><tr><th>Vendor</th><th>Model</th><th>Field of use</th><th>Price</th><th data-type="rating" data-max="2">*/**</th><th>Overlay</th></tr></thead><tbody><tr><td>Raspberry Pi Foundation</td><td><a href="https://www.raspberrypi.org/documentation/hardware/camera/">Pi Cam V1 (OV5647)</a></td><td>Normal</td><td>$25</td><td>1</td><td>MMAL</td></tr><tr><td>Raspberry Pi Foundation</td><td><a href="https://www.raspberrypi.org/documentation/hardware/camera/">Pi Cam V2 (IMX219)</a></td><td>Normal</td><td>$25</td><td>1</td><td>MMAL</td></tr><tr><td>Raspberry Pi Foundation</td><td><a href="https://www.raspberrypi.org/documentation/hardware/camera/">Pi Cam HQ (IMX477)</a></td><td>HQ</td><td>$50</td><td>1</td><td>MMAL</td></tr><tr><td>Arducam</td><td><a href="https://www.arducam.com/product/arducam-12mp-imx477-mini-high-quality-camera-module-for-raspberry-pi/">IMX477 Mini</a></td><td>Normal</td><td>$75</td><td>2</td><td>libcamera_imx477</td></tr><tr><td>Arducam</td><td><a href="https://www.uctronics.com/arducam-for-raspberry-pi-ultra-low-light-camera-1080p-hd-wide-angle-pivariety-camera-module-based-on-1-2-7inch-2mp-starvis-sensor-imx462-compatible-with-raspberry-pi-isp-and-gstreamer-plugin.html">IMX462</a></td><td>Low Light</td><td>$60</td><td>2</td><td>libcamera_arducam</td></tr><tr><td>Arducam</td><td><a href="https://www.arducam.com/product/arducam-mini-16mp-imx519-camera-module-for-raspberry-pi-zero-b0391/">IMX519 MINI </a></td><td>HQ Mini<br>fixed focus</td><td>$35</td><td>2</td><td>libcamera_imx519</td></tr><tr><td>Arducam</td><td><a href="https://www.uctronics.com/presale-arducam-2mp-ultra-low-light-starvis-imx290-motorized-ir-cut-camera-for-raspberry-pi.html">STARVIS IMX290</a></td><td>Ultra<br>Low Light</td><td>$30</td><td>1</td><td>libcamera_imx290</td></tr><tr><td>Arducam</td><td><a href="https://www.uctronics.com/presale-arducam-2mp-ultra-low-light-starvis-imx327-motorized-ir-cut-camera-for-raspberry-pi.html">STARVIS IMX327</a></td><td>Ultra <br>Low Light</td><td>$30</td><td>1</td><td>libcamera_imx327</td></tr><tr><td>Arducam</td><td><a href="https://www.uctronics.com/arducam-2mp-ultra-low-light-starvis-imx462-motorized-ir-cut-camera-for-raspberry-pi.html">STARVIS IMX462</a></td><td>Ultra<br>Low Light</td><td>$60</td><td>1</td><td>libcamera_imx462</td></tr><tr><td>Innomaker</td><td><a href="https://www.inno-maker.com/product/mipi-cam-290/">IMX290</a></td><td>Ultra<br>Low Light</td><td>$90</td><td>2</td><td>veye327</td></tr><tr><td>VEYE</td><td><a href="http://www.veye.cc/en/product/veye-mipi-327e/">IMX 327E</a></td><td>Low Light</td><td>$90</td><td>2</td><td>veye_cam2m</td></tr><tr><td>VEYE</td><td><a href="http://www.veye.cc/en/product/cs-mipi-imx307/">IMX307</a></td><td>Low Light, var. Framerate / Resolution</td><td>$60</td><td>2</td><td>veye_csimx307</td></tr><tr><td>VEYE</td><td><a href="http://www.veye.cc/en/product/veye-mipi-imx462/">IMX462</a></td><td>Low Light</td><td>$80</td><td>2</td><td>veye_cam2m</td></tr><tr><td>VEYE</td><td><a href="http://www.veye.cc/en/product/veye-mipi-imx385/">IMX385</a></td><td>Ultra<br>Low Light</td><td>$80</td><td>2</td><td>veye_cam2m</td></tr></tbody></table>



### Thermal/USB Cameras

| Name           | Lens         | Sensor   | Resolution | FPS      |
| -------------- | ------------ | -------- | ---------- | -------- |
| Hti-201        | Chalcogenide | Raytheon | 320x240    | 9hz      |
| Hti-301        | Germanium    | iRay     | 384x288    | 25hz     |
| FLIR Boson 320 | Germanium    | FLIR     | 320x256    | 9hz/60hz |
| FLIR Boson 640 | Germanium    | FLIR     | 640x512    | 9hz/60hz |

[more information](special-camera.md)

### HDMI CSI Adapter

| Name                                                                                                          | Csi lanes | Resolution        |
| ------------------------------------------------------------------------------------------------------------- | --------- | ----------------- |
| [HC100F](https://www.waveshare.com/hdmi-to-csi-adapter.htm)                                                   | 2         | up to 1080p@30fps |
| [Geekworn C779](https://geekworm.com/products/raspberry-pi-hdmi-to-csi-2-adapter-board-with-15-pin-ffc-cable) | 2         | up to 1080p@30fps |
| [Geekworm C790](https://geekworm.com/products/c790?\_pos=1&\_sid=605794d2b&\_ss=r)                            | 4         | up to 1080p@30fps |

More information about CSI-HDMI can be found [here](hdmi-cameras.md).

### USB Cameras

[Read here](usb-camera.md)

### IP Cameras

[Read here](ip-cameras.md)

### Get your camera supported !

Cameras not listed here may potentionally work, but aren't tested and configured.

We only integrate Cameras which are tested and fitting to the purpose of openhd. If you want to get new cameras supported ask your camera vender to support OpenHD development with their hardware, but contact us first at developer@openhdfpv.org

{% hint style="danger" %}
While many cameras can potentially work, latency is the biggest issue. Please read the Camera pages to fully understand all variables.
{% endhint %}

{% hint style="danger" %}
When using multiple Cameras you need to choose one Camera-Subsystem, so you can not use libcamera and raspicam at the same time. This means f.e. you can not use an Veye-Camera and an Arducam camera at the same time.
{% endhint %}

{% hint style="danger" %}
When using multiple Cameras the second camera is using Software decoding and encoding, it is not recommended to use a high quality camera. It is generally made for a thermal camera or something with lower resolutions.
{% endhint %}

{% hint style="danger" %}
With the upcoming of many new camera's there is one thing we need to mention. OpenHD is not supporting ANY autofocus cameras, since they are basically not usable on equipment with vibrations (like drones), this also includes the Raspberry V3-lineup
{% endhint %}
