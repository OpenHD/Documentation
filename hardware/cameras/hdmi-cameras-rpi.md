# HDMI Cameras

<!-- LEGACY DOCUMENTATION NOTICE -->
> ⚠️ **This documentation is outdated!** A current version is available at [openhdfpv.org](https://openhdfpv.org)
> 
> [📖 **View Updated Version of This Page** →](https://openhdfpv.org)

---


| Name | Sensor | Field of Use | Price |
| ---- | ------ | ------------ | ----- |
| [Hawkeye Firefly Split Mini Version 4K](https://www.fireflycameras.com/products/hawkeye-firefly-split-mini-version-4k-170-degree-hd-recording-dvr-fpv-camera-wdr-single-board-built-in-mic-low-latency-tv-output-for-rc-drone-airplane) | CMOS | Good WDR | $75 |
| [FF Split](https://a.aliexpress.com/\_BPMdpz) | Unknown | Good WDR | $75 |

## Overlay

HDMI cameras require the MMAL Overlay.

## HDMI Input

To use an HDMI Camera, you need an HDMI-CSI Adapter. These adapters enable you to connect cameras with HDMI outputs, allowing the use of a wider variety of cameras beyond the usual Raspberry Pi camera sensor boards. Depending on the camera, this may result in improved picture quality, including support for features like WDR.

Most small/cheap Toshiba chip boards support up to 1080p25 or 1080p30 HDMI camera resolutions on most Raspberry Pi models. The Raspberry Pi Compute Module boards are technically capable of 1080p60, but the necessary driver change to support 1080p60 has not been implemented yet.

**Note:** If your camera only supports 1080p60 or 4k60 HDMI output, it will not work with the Toshiba boards.

### Latency Test

A latency test was conducted by Bortek using the Auvidea B102 with a GoPro4 camera.

[![LatencyTest](https://camo.githubusercontent.com/d7e0dfc1302d703f485402c61091b91c247da8c179e48b2e40af8a6506dfb1ae/68747470733a2f2f696d672e796f75747562652e636f6d2f76692f494242594e314931594f552f302e6a7067)](https://www.youtube.com/watch?v=IBBYN1I1YOU)

#### Camera Compatibility

* GoPro4
* SJcam M10
* Canon EOS 700D

**Cameras That Do Not Work:**

* Samsung NX500 (1080p60, framerate too high)
* Canon EOS M (1080i, interlaced output is not supported by these adapters)

### DCDZ HDMI CSI-2 Adapter

AliExpress link: [DCDZ HDMI CSI-2 Adapter](https://www.aliexpress.com/item/4000152180240.html)

This adapter is widely used for OpenHD. It's available through AliExpress and Taobao. Users in the U.S. or Europe may experience delays in obtaining them. For those regions, consider the similar geekworm board mentioned below, available on Amazon.

The adapter is compatible with both Raspberry Pi Zero and full-size Raspberry Pi models, setting it apart from other cards.

### Geekworm HDMI CSI2 Adapter

Available on Amazon in the U.S., this adapter is similar to the DCDZ adapter mentioned above. Amazon store link: [Geekworm HDMI CSI2 Adapter](https://www.amazon.com/Geekworm-Raspberry-Supports-1080p25fps-Compatible/dp/B0899L6ZXZ) Geekworm store link: [Geekworm HDMI CSI2 Adapter](https://geekworm.com/products/raspberry-pi-hdmi-to-csi-2-adapter-board-with-15-pin-ffc-cable)

The adapter is compatible with full-size Raspberry Pi models.

### Auvidea B102

More info: [Auvidea B102](https://auvidea.eu/product/70502/)

The Auvidea B102 shares similar capabilities with other adapters, but it's only compatible with the Pi Zero.

### Auvidea B101

More info: [Auvidea B101](https://auvidea.eu/b101-hdmi-to-csi-2-bridge-15-pin-fpc/)

Similar to other adapters, the Auvidea B101 is compatible with full-size Raspberry Pi models. [Technical details](http://www.auvidea.eu/download/manual/B10x\_technical\_reference\_1.3.pdf)

### Lintest Systems PiCapture HD1

More info: [Lintest Systems PiCapture HD1](https://lintestsystems.com/products/picapture-hd1)

This more complex (and expensive) card supports HDMI like other adapters, as well as analog component input. However, it's unlikely that any drone-worthy camera uses component connections. The adapter includes LEDs to indicate the status of the camera connection.

## HDMI Cameras

### [FireFly Split](https://a.aliexpress.com/\_BPMdpz)

A drone-specific HDMI camera with onboard recording to MicroSD, WDR support, and a weight of 60g.

Note that some cameras were shipped without HDMI output. The provided link is reported to be the correct HDMI model.