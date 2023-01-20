# Cameras

| Name | Sensor | Field of use | Price |
| :--- | :--- | :--- | :--- |
| [Hawkeye Firefly Split Mini Version 4K](https://www.fireflycameras.com/products/hawkeye-firefly-split-mini-version-4k-170-degree-hd-recording-dvr-fpv-camera-wdr-single-board-built-in-mic-low-latency-tv-output-for-rc-drone-airplane) | CMOS | Good WDR | $75 |
| [FF Split](https://a.aliexpress.com/_BPMdpz) | Unknown | Good WDR | $75 |

## Overlay

HDMI cameras need the MMAL Overlay


## HDMI Input

To use an HDMI Camera you need an HDMI-CSI Adapter, these adapters will allow you to connect a camera with an HDMI connection, which allows you to use more than just the usual pi camera sensor boards. Depending on the camera, this may give you a much better picture, including support for things like WDR.

All of the small/cheap Toshiba chip boards are very similar, and will support up to 1080p25 or 1080p30 HDMI camera resolution on most of the pi models.

This is a limitation of the CSI connection between the adapter and the pi. The Raspberry Pi Compute Module boards are technically capable of 1080p60, however the driver needs a minor change to support 1080p60 and that has not be done yet.

**Note:** If your camera only supports 1080p60 or 4k60 output on the HDMI connection, it will not work with any of the Toshiba boards.

### Latency test

This was done by Bortek, using the Auvidea B102 with a Gopro4 camera.

[![LatencyTest](https://camo.githubusercontent.com/d7e0dfc1302d703f485402c61091b91c247da8c179e48b2e40af8a6506dfb1ae/68747470733a2f2f696d672e796f75747562652e636f6d2f76692f494242594e314931594f552f302e6a7067)](https://www.youtube.com/watch?v=IBBYN1I1YOU)

#### Camera compatibility

* GoPro4
* SJcam M10

**These cameras do not work!:**

* Samsung NX500 \(1080p60, framerate too high\)
* Canon EOS M \(1080i, interlaced output is not supported by these adapters\)


### DCDZ HDMI CSI-2 adapter

![dcdz-hdmi-csi.jpg](https://github.com/OpenHD/Open.HD/raw/master/wiki-content/AddOns_HDMI%20in%20Cards/dcdz-hdmi-csi.jpg)

AliExpress link: [DCDZ HDMI CSI-2 adapter](https://www.aliexpress.com/item/4000152180240.html)

Very widely used for OpenHD, but only available through AliExpress and Taobao, so those of you in the U.S. or Europe may have trouble getting them quickly. See the similar geekworm board below, those are available on Amazon.

Has a connector for both the Raspberry Pi Zero and full size Raspberry Pi models, none of the other cards do.

### Geekworm HDMI CSI2 adapter

![geekworm-hdmi-csi.jpg](https://github.com/OpenHD/Open.HD/raw/master/wiki-content/AddOns_HDMI%20in%20Cards/geekworm-hdmi-csi.jpg)

Available on Amazon in the U.S., and is similar to the DCDZ adapter above.

Amazon store: [Geekworm HDMI CSI2 adapter](https://www.amazon.com/Geekworm-Raspberry-Supports-1080p25fps-Compatible/dp/B0899L6ZXZ)

Geekworm store: [Geekworm HDMI CSI2 adapter](https://geekworm.com/products/raspberry-pi-hdmi-to-csi-2-adapter-board-with-15-pin-ffc-cable)

Has a connector compatible with the full size pi models. 

### Auvidea B102

More info: [Auvidea B102](https://auvidea.eu/product/70502/)

Same basic capabilities as the others, but has a connector compatible with the Pi Zero only.

### Auvidea B101

More info: [Auvidea B101](https://auvidea.eu/b101-hdmi-to-csi-2-bridge-15-pin-fpc/)

Same basic capabilities as the others, has a connector compatible with the full size pi models.

[Technical details](http://www.auvidea.eu/download/manual/B10x_technical_reference_1.3.pdf)

### Lintest Systems PiCapture HD1

More info: [Lintest Systems PiCapture HD1](https://lintestsystems.com/products/picapture-hd1)

This is a more complicated \(and expensive\) card, it supports HDMI just like the others \(with the same limitations\), but also supports analog component input, though it is unlikely that any camera worth putting on a drone will have component connections \(they were common on HDTVs and DVD players at one point\).

The adapter has LEDs that will tell you whether the camera connection is OK.

## HDMI Cameras

### [FireFly Split](https://a.aliexpress.com/_BPMdpz)

An HDMI camera specifically designed for drones, has onboard recording to MicroSD on the camera itself, WDR support and weighs 60g.

Be aware that some of these cameras have been shipped without HDMI output, however the link above is reported to be the correct HDMI model.

**Note**: to use this camera for Open.HD you need an [HDMI Input](cameras.md#hdmi-input) board .Be aware that while the camera itself can do 4k resolution, the Raspberry Pi is not capable of encoding 4k video. However some other boards supported by Open.HD like the Jetson Nano can handle it.
