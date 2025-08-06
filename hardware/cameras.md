# Cameras

<!-- LEGACY DOCUMENTATION NOTICE -->
> ⚠️ **This documentation is outdated!** A current version is available at [openhdfpv.org](https://openhdfpv.org)
> 
> [📖 **View Updated Version of This Page** →](https://openhdfpv.org)

---


OpenHD supports and recommends the following cameras on the Raspberry Pi:

### Raspberry Pi CSI cameras

| Vendor                  | Model                                                                                                                                                                                                                                   | Field of use                  | Price | Overlay           |
| ----------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------- | ----- | ----------------- |
||||||
| Arducam                 | [SkyMaster HDR](https://www.arducam.com/product/presalearducam-12mp-imx708-hdr-120-wide-angle-camera-module-with-m12-lens-for-raspberry-pi/)                                                                                            | Highest Quality               | $37   | libcamera\_imx708 |
| Arducam                 | [SkyVision Pro](https://www.arducam.com/product/16mp-imx519-camera-module-with-m12-lens-wide-angle-color-rolling-shutter-for-raspberry-pi-and-openhd/)                                                                                  | High Quality                  | $37   | libcamera\_imx519 |
| Arducam                 | [IMX477M](https://www.arducam.com/product/12mp-imx477m-mini-wide-angle-camera-module-for-raspberry-pi/)                                                                                                                                 | low weight,small              | $37   | libcamera\_imx477 |
| Raspberry Pi Foundation | [Pi Cam V1 (OV5647)\*](https://www.raspberrypi.org/documentation/hardware/camera/)                                                                                                                                                      | Normal                        | $25   | MMAL              |
| Raspberry Pi Foundation | [Pi Cam V2 (IMX219)\*](https://www.raspberrypi.org/documentation/hardware/camera/)                                                                                                                                                      | Normal                        | $25   | MMAL              |
| Raspberry Pi Foundation | [Pi Cam HQ (IMX477)\*](https://www.raspberrypi.org/documentation/hardware/camera/)                                                                                                                                                      | HQ                            | $50   | MMAL              |
| Arducam                 | [IMX477 Mini](https://www.arducam.com/product/arducam-12mp-imx477-mini-high-quality-camera-module-for-raspberry-pi/)                                                                                                                    | Normal                        | $75   | libcamera\_imx477 |
| Arducam                 | [IMX462](https://www.uctronics.com/arducam-for-raspberry-pi-ultra-low-light-camera-1080p-hd-wide-angle-pivariety-camera-module-based-on-1-2-7inch-2mp-starvis-sensor-imx462-compatible-with-raspberry-pi-isp-and-gstreamer-plugin.html) | Low Light                     | $60   | 2                 |
| Arducam                 | [IMX519 MINI](https://www.arducam.com/product/arducam-mini-16mp-imx519-camera-module-for-raspberry-pi-zero-b0391/)                                                                                                                      | <p>HQ Mini<br>fixed focus</p> | $35   | libcamera\_imx519 |
| Arducam                 | [STARVIS IMX290](https://www.uctronics.com/presale-arducam-2mp-ultra-low-light-starvis-imx290-motorized-ir-cut-camera-for-raspberry-pi.html)                                                                                            | Low Light                     | $30   | libcamera\_imx290 |
| Arducam                 | [STARVIS IMX327](https://www.uctronics.com/presale-arducam-2mp-ultra-low-light-starvis-imx327-motorized-ir-cut-camera-for-raspberry-pi.html)                                                                                            | Low Light                     | $30   | libcamera\_imx327 |
| Arducam                 | [STARVIS IMX462](https://www.uctronics.com/arducam-2mp-ultra-low-light-starvis-imx462-motorized-ir-cut-camera-for-raspberry-pi.html)                                                                                                    | <p>Ultra<br>Low Light</p>     | $60   | libcamera\_imx462 |
| VEYE                    | [IMX 327E](http://www.veye.cc/en/product/veye-mipi-327e/)                                                                                                                                                                               | Low Light                     | $90   | veye\_cam2m       |
| VEYE                    | [IMX307](http://www.veye.cc/en/product/cs-mipi-imx307/)                                                                                                                                                                                 | Low                           |       |                   |

\*This cameras use mainly raspivid which is legacy and discontinued. These cameras aren't really recommended for FPV, since V1,V2 of Raspberry cameras do not provide a good image outdoors, and the HQ camera is much bigger and more expensive then smaller versions of it. V1 sensor is also not produced anymore and V2 sensor is about to follow.

### Thermal/USB Cameras

| Name             | Lens         | Sensor   | Resolution | FPS      |
| --------------   | ------------ | -------- | ---------- | -------- |
| Hti-201          | Chalcogenide | Raytheon | 320x240    | 9hz      |
| Hti-301          | Germanium    | iRay     | 384x288    | 25hz     |
| Infiray T2 search| Germanium    | iRay     | 256×192    | 25hz     |
| FLIR Boson 320   | Germanium    | FLIR     | 320x256    | 9hz/60hz |
| FLIR Boson 640   | Germanium    | FLIR     | 640x512    | 9hz/60hz |

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

We also want to thank our cooperation partners for providing the Team with Prototypes and want to specifically thank [Arducam](https://www.arducam.com/openhd/) for helping us in developing cameras specifically to our need.

{% hint style="info" %}
#### Supported Cameras \*

Can be enabled and used easily (No custom scripting), in case things don't work you can ask us for help.
{% endhint %}

{% hint style="info" %}
#### Recommended Cameras \*\*

Among the available options, we highly recommend the top 3 cameras as they offer unparalleled versatility and optimization for OpenHD. These cameras stand out for their exceptional image quality, low latency, extensive feature set, and suitability for professional applications. If you are currently without a preferred camera choice, these top recommendations are guaranteed to provide unique benefits and fulfill your requirements.
{% endhint %}
