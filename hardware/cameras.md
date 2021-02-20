# Cameras

### Overview

{% hint style="danger" %}
While many cameras can potentially work, latency is the biggest issue. Please read this page to completely understand the available options and pros and cons of each.
{% endhint %}

{% hint style="success" %}
 For using 3rd party cameras via HDMI please refer to the [HDMI Input](cameras.md#hdmi-input) Section
{% endhint %}

{% hint style="success" %}
The best value csi camera is the "small" version of hq camera (IMX477) from arducam.

The best value usb camera is the veye 
{% endhint %}

 If you have tested a camera, please let us know how it performs by filling out this [form](https://docs.google.com/forms/d/e/1FAIpQLSc9hSLo_BCuiZAzI6lTYKBLIlI07JjcbsiVbniP8zyEAgg8Aw/viewform). We will add the results to the camera matrix.

<table>
  <thead>
    <tr>
      <th style="text-align:left">Name</th>
      <th style="text-align:left">Connection</th>
      <th style="text-align:left">Sensor</th>
      <th style="text-align:left">Resolution</th>
      <th style="text-align:left">FPS</th>
      <th style="text-align:left">Price</th>
      <th style="text-align:left">Notes</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="text-align:left"><a href="https://www.raspberrypi.org/documentation/hardware/camera/">Pi Cam V1</a>
      </td>
      <td style="text-align:left">CSI</td>
      <td style="text-align:left">OV5647</td>
      <td style="text-align:left">1080p</td>
      <td style="text-align:left">30-90</td>
      <td style="text-align:left">$25</td>
      <td style="text-align:left">FPS depends on resolution</td>
    </tr>
    <tr>
      <td style="text-align:left"><a href="https://www.raspberrypi.org/documentation/hardware/camera/">Pi Cam V2</a>
      </td>
      <td style="text-align:left">CSI</td>
      <td style="text-align:left">IMX219</td>
      <td style="text-align:left">1080p</td>
      <td style="text-align:left">30-90</td>
      <td style="text-align:left">$25</td>
      <td style="text-align:left">FPS depends on resolution</td>
    </tr>
    <tr>
      <td style="text-align:left"><a href="https://www.raspberrypi.org/documentation/hardware/camera/">Pi Cam HQ</a>
      </td>
      <td style="text-align:left">CSI</td>
      <td style="text-align:left">IMX477</td>
      <td style="text-align:left">1080p</td>
      <td style="text-align:left">30-120</td>
      <td style="text-align:left">$50</td>
      <td style="text-align:left">FPS depends on resolution, See <a href="https://discuss.openhdfpv.com/t/m12-lens-holder-for-pi-hq-cam/107">link </a>for
        improved lens holder to reduce weight.</td>
    </tr>
    <tr>
      <td style="text-align:left"><a href="https://www.inno-maker.com/product/mipi-cam-290">Veye/Innomaker 290</a>
      </td>
      <td style="text-align:left">CSI</td>
      <td style="text-align:left">IMX290</td>
      <td style="text-align:left">1080p</td>
      <td style="text-align:left">30</td>
      <td style="text-align:left">$90</td>
      <td style="text-align:left">Amazing in low light</td>
    </tr>
    <tr>
      <td style="text-align:left"><a href="https://www.logitech.com/en-gb/product/hd-pro-webcam-c920">Logitech C920</a>
      </td>
      <td style="text-align:left">USB</td>
      <td style="text-align:left">--</td>
      <td style="text-align:left">1080p</td>
      <td style="text-align:left">30</td>
      <td style="text-align:left">$95</td>
      <td style="text-align:left">Reportedly &quot;low&quot; latency for usb</td>
    </tr>
    <tr>
      <td style="text-align:left"><a href="http://www.hisilicon.com/en/Products">Hi3518</a>
      </td>
      <td style="text-align:left">IP</td>
      <td style="text-align:left">--</td>
      <td style="text-align:left">1080p</td>
      <td style="text-align:left">30</td>
      <td style="text-align:left">--</td>
      <td style="text-align:left">h264/h265</td>
    </tr>
    <tr>
      <td style="text-align:left"><a href="https://www.kurokesu.com/shop/cameras/CAMERA_C1_MICRO_M12">C1 Micro</a>
      </td>
      <td style="text-align:left">USB</td>
      <td style="text-align:left">AR0330</td>
      <td style="text-align:left">1080p</td>
      <td style="text-align:left">30</td>
      <td style="text-align:left">&#x20AC;112</td>
      <td style="text-align:left">h264, 12g weight</td>
    </tr>
    <tr>
      <td style="text-align:left"><a href="https://www.kurokesu.com/shop/cameras/CAMUSB1">C1</a>
      </td>
      <td style="text-align:left">USB</td>
      <td style="text-align:left">AR0330</td>
      <td style="text-align:left">1080p</td>
      <td style="text-align:left">30</td>
      <td style="text-align:left">&#x20AC;100</td>
      <td style="text-align:left">h264</td>
    </tr>
    <tr>
      <td style="text-align:left"><a href="https://www.kurokesu.com/shop/cameras/CAMERA_C1_PRO">C1 Pro</a>
      </td>
      <td style="text-align:left">USB</td>
      <td style="text-align:left">IMX290</td>
      <td style="text-align:left">1080p</td>
      <td style="text-align:left">30</td>
      <td style="text-align:left">&#x20AC;139</td>
      <td style="text-align:left">h264</td>
    </tr>
    <tr>
      <td style="text-align:left"><a href="https://www.e-consystems.com/usb-cameras/imx290-low-light-usb-camera.asp">e-con Hyperyon</a>
      </td>
      <td style="text-align:left">USB</td>
      <td style="text-align:left">IMX290</td>
      <td style="text-align:left">1080p</td>
      <td style="text-align:left">60</td>
      <td style="text-align:left">$240</td>
      <td style="text-align:left">h264, WDR/HDR</td>
    </tr>
    <tr>
      <td style="text-align:left"><a href="https://a.aliexpress.com/_BPMdpz">Firefly Split</a>
      </td>
      <td style="text-align:left">HDMI</td>
      <td style="text-align:left">Unknown</td>
      <td style="text-align:left">
        <p>4k(record)</p>
        <p>1080p stream</p>
      </td>
      <td style="text-align:left">60</td>
      <td style="text-align:left">$70</td>
      <td style="text-align:left">WDR, HDMI-CSI board, Onboard Rec</td>
    </tr>
  </tbody>
</table>

* Resolutions are maximum, which might not be ideal for performance
* Higher FPS is possible in certain cases with some cams
* HDMI connection implies the use of an HDMI adapter card and incurs additional latency
* Many users report success with HDMI adapter cards and cameras with low latency HDMI out. GoPro and similar are popular and offer perhaps some of the best image quality at the expense of greater size, weight, cost and depending on the camera, latency

### CSI Camera cables for Raspberry Pi Zero

The Raspberry Pi Zero requires special CSI cables since it has a smaller CSI connector on the board. You can find these on sites like AliExpress, we have included two example links:

* Short Raspberry Zero CSI cable: [https://www.aliexpress.com/item/32861638369.html](https://www.aliexpress.com/item/32861638369.html)
* 8 Cm Raspberry Pi Zero CSI cable: [https://www.aliexpress.com/item/33032182445.html](https://www.aliexpress.com/item/33032182445.html)

Feel free to use any other cable you might find, these two are known to work.

### Latency considerations

When very low latency is required, every part of the system from glass-to-glass must be carefully chosen and tuned. In some cases a particular combination of SBC + camera sensor may be required.

Generally, there must be an **H.264/H.265 encoder** inside the camera board itself, or there must be a CSI connection between the sensor and the SBC to ensure that frames are transferred and encoded as fast as possible.

Some USB 3.0 cameras _might_ be capable of ultra-low latency when paired with a suitable SBC with a zero-copy video processing pipeline, but in most cases USB cameras are only suitable when they have an internal H.264 encoder.

IP cameras are not specifically designed for low latency, and many of them have latency upwards of 500 ms+, but there are specific cameras available for purchase that have reasonable latency closer to 100-200 ms.

## USB Cameras

### Logitech C920

Note that in recent years Logitech has been removing the H.264 encoder from all of their webcams, if you buy one new it may not actually have an H.264 encoder inside and that would prevent it from being used properly in Open.HD.

#### C1 series from Kurokesu

These are exceptionally well made USB H.264 cameras built with high quality sensors and a Sonix chip to handle image processing and H.264 encoding. Latency is reported to be 90-125 ms minimum.

### [e-con Systems Hyperyon](https://www.e-consystems.com/usb-cameras/imx290-low-light-usb-camera.asp)

A USB H,264 camera with an IMX290 sensor and an onboard ISP tuned for low light, also supports HDR/WDR. Should work with every board supported by Open.HD, including the Nanopi series. It is expensive, but may be useful to someone.

Comes with an M12 lens with 132° FOV.

There are 2 boards, one with the camera sensor 40 mm x 25 mm, and the other 25 mm x 65 mm board contains the encoder and USB connector, the total weight for everything is 37.5 g.

## HDMI Input

These adapters will allow you to connect a camera with an HDMI connection, which allows you to use more than just the usual pi camera sensor boards. Depending on the camera, this may give you a much better picture, including support for things like WDR.

All of the small/cheap Toshiba chip boards are very similar, and will support up to 1080p25 or 1080p30 HDMI camera resolution on most of the pi models.

This is a limitation of the CSI connection between the adapter and the pi. The Raspberry Pi Compute Module boards are technically capable of 1080p60, however the driver needs a minor change to support 1080p60 and that has not be done yet.

**Note:** If your camera only supports 1080p60 or 4k60 output on the HDMI connection, it will not work with any of the Toshiba boards.

### Latency test

This was done by the user _Bortek_, using the Auvidea B102 with a Gopro4 camera.

[![IMAGE ALT TEXT HERE](https://camo.githubusercontent.com/d7e0dfc1302d703f485402c61091b91c247da8c179e48b2e40af8a6506dfb1ae/68747470733a2f2f696d672e796f75747562652e636f6d2f76692f494242594e314931594f552f302e6a7067)](https://www.youtube.com/watch?v=IBBYN1I1YOU)

#### Camera compatibility

* GoPro4
* SJcam M10

**These cameras do not work!:**

* Samsung NX500 \(1080p60, framerate too high\)
* Canon EOS M \(1080i, interlaced output is not supported by these adapters\)

#### Settings

They will be auto detected and do not require special settings, but you should still set the resolution and frame rate to match your camera in `openhd-settings-1.txt` like this:

```text
WIDTH=1920
HEIGHT=1080
FPS=30
EXTRAPARAMS="-cd H264 -n -fl -ih -pf high -md 1 -awb off -awbg 1.0,1.0 -ex off"
```

You may need to change the resolution/frame rate on the camera itself so that it does not exceed the capabilities of the adapter board.

### DCDZ HDMI CSI-2 adapter

![dcdz-hdmi-csi.jpg](https://github.com/OpenHD/Open.HD/raw/master/wiki-content/AddOns_HDMI%20in%20Cards/dcdz-hdmi-csi.jpg)

AliExpress link: [DCDZ HDMI CSI-2 adapter](https://www.aliexpress.com/item/4000152180240.html)

Very widely used for Open.HD, but only available through AliExpress and Taobao, so those of you in the U.S. or Europe may have trouble getting them quickly. See the similar Geekworm board below, those are available on Amazon.

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

This is a more complicated \(and expensive\) card, it supports HDMI just like the others \(with the same limitations\), but also supports analog component input, though it is unlikely that any camera worth putting on a drone will have component connections \(they were common on HDTV's and DVD players at one point\).

The adapter has LED's that will tell you whether the camera connection is OK.

## HDMI Cameras

### [FireFly Split](https://a.aliexpress.com/_BPMdpz)

An HDMI camera specifically designed for drones, has onboard recording to Micro-SD on the camera itself, WDR support and weighs 60 g.

Be aware that some of these cameras have been shipped without HDMI output, however the link above is reported to be the correct HDMI model. See the [website ](https://www.fireflycameras.com/products/hawkeye-firefly-split-4k-160-degree-hd-recording-dvr-mini-fpv-camera-wdr-single-board-built-in-mic-low-latency-tv-output-for-rc-drone-airplane?_pos=1&_sid=77d319bcd&_ss=r)for more details.

**Note**: to use this camera for Open.HD you need an [HDMI Input](cameras.md#hdmi-input) board .Be aware that while the camera itself can do 4K recording it only outputs 1080p30 or 720p60 on the HDMI port.

## Thermal Cameras

Open.HD supports several thermal cameras, including the FLIR One, the Seek Compact, Hti-301, and others.

Thermal cameras generally connect via USB, and you do not need to do anything except configure the Open.HD settings file to get them working.

**Note:** This page needs example flight images from each thermal camera, if you have any please get in touch with us so we can add them.

### A Warning

Thermal cameras are _nothing like normal cameras_! Review the available info about each camera before you make any purchase decisions.

It may seem counter intuitive, but a thermal camera with a resolution of 204x156 can be significantly worse than one with an 80x60 resolution. The entire thermal imaging system in the camera matters, from the lens material and size, to the _kind_ of sensor inside, the resolution of the sensor, and the image post-processing done by the camera.

Any poorly performing part of the system can severely degrade the image produced by the camera, potentially making it unusable for a particular use case. Sometimes that is an acceptable trade off in order to reach a low price point.

And keep in mind that a particular thermal camera might be OK for close up electronics work or basic household uses, but could be terrible for drone flight.

### Legal restrictions

Thermal cameras are highly regulated items, so depending on where you live you may have to pay a higher price for a specific camera, obtain a license of some kind in order to import or possess it, or may not be able to buy one at all.

The frame rate is generally the issue when it comes to regulations, not the resolution. The reason for that restriction comes from the possibility that a thermal camera could be used for as part of a weapon.

If you live in a country that is part of the _Wassenaar_ agreement, you should be able to buy 30/60 Hz thermal cameras but the price may be higher if they were imported from the United States.

There are Chinese companies such as Hti Instrument that sell directly on AliExpress, TaoBao and through their own websites. If you have trouble getting a FLIR or Seek camera from the United States, you may have better luck with something like Hti.

### Camera Overview

| Name | Lens | Sensor | Resolution | FPS | Price | Notes |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| FLIR One G2 | Silicon | FLIR Lepton 3 | 160x120 | 7-9hz | $100-200 | Can be purchased used on eBay |
| FLIR One G3 | Silicon | FLIR Lepton 2 | 80x60 | 7-9hz | $199 | DO NOT BUY, get a G2 if you can |
| FLIR One G3 Pro | Silicon | FLIR Lepton 3 | 160x120 | 7-9hz | $399 | Get a G2 if you can |
| Seek Compact | Chalcogenide | Raytheon | 206x156 | 7hz | $120-240 | Worse than FLIR One G2 \(maybe even G3\) |
| Seek Compact Pro | Chalcogenide | Raytheon | 320x240 | 7hz | $250-499 | A bit noisy, get the FastFrame if possible |
| Seek Compact Pro FastFrame | Chalcogenide | Raytheon | 320x240 | ~15hz | $430-600 | A bit noisy |
| Hti-201 | Chalcogenide | Raytheon | 320x240 | 9hz | $200-300 | These are Seek Compact Pro clones |
| Hti-301 | Germanium | iRay | 384x288 | 25hz | $760 | High quality but untested |
| FLIR Boson 320 | Germanium | FLIR | 320x256 | 9hz/60hz | ~$1500 | High quality, untested |
| FLIR Boson 640 | Germanium | FLIR | 640x512 | 9hz/60hz | ~$3500 | High quality, untested |

### Flying with a thermal camera

You will want to give some consideration to what you will actually be able to _see_ with a specific thermal camera in a particular situation.

Very low resolution thermal cameras may allow you to see that a hot object is in a particular area, but you may not be able to tell what it is. In some cases like search and rescue, this may be perfectly fine, but in other cases you may need higher thermal resolution.

Remember we're talking about sensors with very low resolution to begin with, for example a 1280x720 FPV camera has _48x_ the resolution of a 160x120 thermal camera. At longer range you may not even be able to see an object at all, even if you can still see it with the main FPV camera.

Another consideration is the thermal "span" of the area in view of the thermal camera, if the ground is the same temperature as the trees, objects and animals \(for example they're all around 97F\), you will have trouble seeing anything but noise or a flat image with many cameras. In that case you would need to look for a camera with a low NETD rating, and a good sized lens.

**FLIR Tau 2 and range test**

[![FLIR Tau 2 flight](https://github.com/OpenHD/Open.HD/raw/master/wiki-content/Thermal-Cameras/flir-tau-2-flight-screenshot.jpg)](https://www.youtube.com/watch?v=WXKOqgxwp-c)

**FLIR Boson 320 flight over a neighborhood**

[![FLIR Boson 320 flight](https://github.com/OpenHD/Open.HD/raw/master/wiki-content/Thermal-Cameras/flir-boson-320-flight.jpg)](https://www.youtube.com/watch?v=PQGDQzf-Z50)

### Lenses

The lens on a thermal camera is not ordinary glass \(which does not allow IR wavelengths to pass through\).

Germanium lenses allow for high quality thermal images, but they are expensive. Most cheap/light thermal cameras will use Silicon or Chalcogenide lenses instead.

You generally cannot replace the lens on a thermal camera unless it was specifically designed for it, and even those that are designed to have removable lenses sometimes require very careful handling to avoid causing damage.

### Camera information

Below are some brief descriptions of individual cameras from the table above, please read this info carefully before buying any of them.

In some cases a thermal camera may require a different SBC, a video adapter of some kind, or special software in order for it to work properly.

#### FLIR One G2

![flir one g2](https://github.com/OpenHD/Open.HD/raw/master/wiki-content/Thermal-Cameras/flir-one-g2.jpeg)

These are designed to connect to a smartphone, there were iOS and Android versions with different connectors. The Android version has a standard Micro USB connector and can be connected to an Open.HD system with a USB OTG cable.

Many people use these cameras, they are well known and they do work, despite the low resolution and thermal performance.

The resolution is 160x120, which is _the absolute minimum_ you would want for drone flight. You will be able to see heat signatures but without much detail.

The sensor inside the FLIR One G2 is a FLIR Lepton 3 \(confusing, yes\), which is a very good thermal image sensor. However FLIR's lens and image processing choices reduce the image quality.

#### FLIR One G3 \([Amazon](https://www.amazon.com/FLIR-One-Thermal-Imager-Android/dp/B0728C7KNC)\)

DO NOT BUY THESE, they are _significantly_ worse than a G2. Even when the G2 was new, it was only about $50 more than the G3 is now, it's a very bad deal.

#### FLIR One G3 Pro \([Amazon](https://www.amazon.com/FLIR-ONE-Pro-Professional-Smartphones/dp/B085DW3NSF)\)

These are largely identical to the G2, they have a Lepton 3 sensor with 160x120 resolution.

FLIR created 2 different price points with the G3 and G3 Pro. The Pro is significantly more expensive now than the G2 was when it was being manufactured and sold, but you can still find used G2 cameras for $120-200 on eBay and other websites.

#### Seek Compact \([manufacturer](https://www.thermal.com/compact-series.html), [Amazon](https://www.amazon.com/Seek-Thermal-CompactPRO-Resolution-Imaging/dp/B00NYWAHHM)\)

These are cheap, but have always had significant issues due to the lens and the sensor. You are **much** better off with a FLIR One G2 if cost is your primary reason for looking at these cameras.

#### Seek Compact Pro \([manufacturer](https://www.thermal.com/compact-series.html), [Amazon](https://www.amazon.com/Seek-Thermal-CompactPRO-Resolution-Imaging/dp/B07V34RFLW)\)

![seek compact pro compared to flir one g2](https://github.com/OpenHD/Open.HD/raw/master/wiki-content/Thermal-Cameras/seek-compact-pro-compare.jpeg)

Model numbers for these cameras _do not_ end with an X, e.g. UQ-AAA.

These are significantly better than the non-pro model, the sensor is 320x240 and has a Chalcogenide lens.

There is still a fair amount of noise in the system, these are better for scenes where there is a big difference/span between the hottest and coldest object in view. When the thermal span is small, the noise in the system can become very obvious.

Note that Seek has quietly updated these cameras over time, so you may have one that works more like a FastFrame even though it wasn't marketed that way when purchased. They have also made some improvements to the sensor and firmware over time.

#### Seek Compact Pro FastFrame \([manufacturer](https://www.thermal.com/compact-series.html), [DigiKey](https://www.digikey.com/en/products/detail/seek-thermal/UQ-AAAX/10230124)\)

Model numbers for these cameras end with an X, like UQ-AAAX. The UQ-EAAX is an export version but is otherwise identical.

Same as the regular Pro, but the frame rate is never locked to 9 Hz, and can instead reach at least 15 Hz.

These are export controlled items because of the frame rate, you can buy them easily in many countries but you may have trouble ordering one if you have to ship across a border.

#### Hti-201 \([manufacturer](https://hti-instrument.com/products/ht-201-mobile-phone-thermal-imager)\)

![Hti-201 Thermal Camera](https://github.com/OpenHD/Open.HD/raw/master/wiki-content/Thermal-Cameras/hti-201.jpg)

These are basically clones of the Seek Compact Pro.

The camera housing has a very awkward shape compared to most other thermal cameras, the side with the sensor and lens has a significant bump.

#### Hti-301 \([manufacturer](https://hti-instrument.com/products/ht-301-mobile-phone-thermal-imager), [Amazon](https://www.amazon.com/Resolution-Infrared-Thermal-Smartphone-Hti-Xintai/dp/B07Z7J6LXD)\)

![Hti-301 Thermal Camera](https://github.com/OpenHD/Open.HD/raw/master/wiki-content/Thermal-Cameras/hti-301.jpg)

A very good thermal camera with 384x288 resolution and a fairly large germanium lens and a frame rate of 25 Hz. They are expensive compared to some others, but the thermal performance is very good.

These cameras are designed to work like a normal webcam, in that there is no special driver required.

Note that you may have trouble getting 25 Hz video streams out of these when used with a raspberry pi due to USB limitations.

#### FLIR Boson 320 \([manufacturer](https://www.flir.com/products/boson/), [GroupGets](https://store.groupgets.com/collections/frontpage/products/flir-boson-320)\)

![FLIR Boson 320 Thermal Core](https://github.com/OpenHD/Open.HD/raw/master/wiki-content/Thermal-Cameras/flir-boson-320.jpg)

A 320x256 thermal imager "core", full 60 Hz frame rate but FLIR makes a 9 Hz version as well. They are fairly expensive but have Germanium lenses.

Unlike most of the other cameras these are not designed for a smartphone, they are designed for integration in something like a larger camera system or a drone. You must buy an appropriate connection board to snap on to the back of the camera, some have USB while others have analog video output. For Open.HD you would want the USB kind, analog video requires a special adapter to digitize it again and most of them will not work well with a raspberry pi.

These are export controlled items due to the very high frame rate.

**Note**: as of the time this wiki page is being written, I am not aware of anyone having used a Boson with Open.HD, there may be some changes required in software to make them work.

Real world flight video:

[![FLIR Boson 320 flight](https://github.com/OpenHD/Open.HD/raw/master/wiki-content/Thermal-Cameras/flir-boson-320-flight.jpg)](https://www.youtube.com/watch?v=PQGDQzf-Z50)

#### FLIR Boson 640 \([manufacturer](https://www.flir.com/products/boson/), [GroupGets](https://store.groupgets.com/collections/frontpage/products/flir-boson-640)\)

Same as the 320 model, but with higher resolution.

