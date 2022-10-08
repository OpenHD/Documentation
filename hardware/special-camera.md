# Special Usecase Cameras

{% hint style="danger" %}
Special Usecase Cameras are currently only supported on the Raspberry Pi
{% endhint %}

## Thermal Cameras


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

Open.HD supports several thermal cameras, including the FLIR One, the Seek Compact, Hti-301, and others.

Thermal cameras generally connect via USB, and you do not need to do anything except configure the Open.HD settings file to get them working.

**Note:** This page needs example flight images from each thermal camera, if you have any please get in touch with us so we can add them.

### A Warning

Thermal cameras are _nothing like normal cameras_! Review the available info about each camera before you make any purchase decisions.

It may seem counterintuitive, but a thermal camera with a resolution of 204x156 can be significantly worse than one with an 80x60 resolution. The entire thermal imaging system in the camera matters, from the lens material and size, to the _kind_ of sensor inside, the resolution of the sensor, and the image post-processing done by the camera.

Any poorly performing part of the system can severely degrade the image produced by the camera, potentially making it unusable for a particular use case. Sometimes that is an acceptable tradeoff in order to reach a low price point.

And keep in mind that a particular thermal camera might be OK for close up electronics work or basic household uses, but could be terrible for drone flight.

### Legal restrictions

Thermal cameras are highly regulated items, so depending on where you live you may have to pay a higher price for a specific camera, obtain a license of some kind in order to import or possess it, or may not be able to buy one at all.

The frame rate is generally the issue when it comes to regulations, not the resolution. The reason for that restriction comes from the possibility that a thermal camera could be used for as part of a weapon.

If you live in a country that is part of the Wassenaar agreement, you should be able to buy 30/60hz thermal cameras but the price may be higher if they were imported from the United States.

There are Chinese companies such as Hti Instrument that sell directly on AliExpress, TaoBao and through their own websites. If you have trouble getting a FLIR or Seek camera from the United States, you may have better luck with something like Hti.

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

These are designed to connect to a smartphone, there were iOS and Android versions with different connectors. The Android version has a standard Micro USB connector and can be connected to an OpenHD system with a USB OTG cable.

Many people use these cameras, they are well known and they do work, despite the low resolution and thermal performance.

The resolution is 160x120, which is _the absolute minimum_ you would want for drone flight. You will be able to see heat signatures but without much detail.

The sensor inside the FLIR One G2 is a FLIR Lepton 3 \(confusing, yes\), which is a very good thermal image sensor. However FLIR's lens and image processing choices reduce the image quality.

#### FLIR One G3 \([Amazon](https://www.amazon.com/FLIR-One-Thermal-Imager-Android/dp/B0728C7KNC)\)

DO NOT BUY THESE, they are _significantly_ worse than a G2. Even when the G2 was new, it was only about $50 more than the G3 is now, it's a very bad deal.

#### FLIR One G3 Pro \([Amazon](https://www.amazon.com/FLIR-ONE-Pro-Professional-Smartphones/dp/B085DW3NSF)\)

These are largely identical to the G2, they have a Lepton 3 sensor with 160x120 resolution.

FLIR created 2 different price points with the G3 and G3 Pro. The Pro is significantly more expensive now than the G2 was when it was being manufactured and sold, but you can still find used G2 cameras for $120-200 on ebay and other websites.

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

Same as the regular Pro, but the frame rate is never locked to 9hz, and can instead reach at least 15hz.

These are export controlled items because of the frame rate, you can buy them easily in many countries but you may have trouble ordering one if you have to ship across a border.

#### Hti-201 \([manufacturer](https://hti-instrument.com/products/ht-201-mobile-phone-thermal-imager)\)

![Hti-201 Thermal Camera](https://github.com/OpenHD/Open.HD/raw/master/wiki-content/Thermal-Cameras/hti-201.jpg)

These are basically clones of the Seek Compact Pro.

The camera housing has a very awkward shape compared to most other thermal cameras, the side with the sensor and lens has a significant bump.

#### Hti-301 \([manufacturer](https://hti-instrument.com/products/ht-301-mobile-phone-thermal-imager), [Amazon](https://www.amazon.com/Resolution-Infrared-Thermal-Smartphone-Hti-Xintai/dp/B07Z7J6LXD)\)

![Hti-301 Thermal Camera](https://github.com/OpenHD/Open.HD/raw/master/wiki-content/Thermal-Cameras/hti-301.jpg)

A very good thermal camera with 384x288 resolution and a fairly large germanium lens and a frame rate of 25hz. They are expensive compared to some others, but the thermal performance is very good.

These cameras are designed to work like a normal webcam, in that there is no special driver required.

Note that you may have trouble getting 25hz video streams out of these when used with a raspberry pi due to USB limitations.

#### FLIR Boson 320 \([manufacturer](https://www.flir.com/products/boson/), [GroupGets](https://store.groupgets.com/collections/frontpage/products/flir-boson-320)\)

![FLIR Boson 320 Thermal Core](https://github.com/OpenHD/Open.HD/raw/master/wiki-content/Thermal-Cameras/flir-boson-320.jpg)

A 320x256 thermal imager "core", full 60hz frame rate but FLIR makes a 9hz version as well. They are fairly expensive but have Germanium lenses.

Unlike most of the other cameras these are not designed for a smartphone, they are designed for integration in something like a larger camera system or a drone. You must buy an appropriate connection board to snap on to the back of the camera, some have USB while others have analog video output. For OpenHD you would want the USB kind, analog video requires a special adapter to digitize it again and most of them will not work well with a raspberry pi.

These are export controlled items due to the very high frame rate.

**Note**: as of the time this wiki page is being written, I am not aware of anyone having used a Boson with OpenHD, there may be some changes required in software to make them work.

Real world flight video:

[![FLIR Boson 320 flight](https://github.com/OpenHD/Open.HD/raw/master/wiki-content/Thermal-Cameras/flir-boson-320-flight.jpg)](https://www.youtube.com/watch?v=PQGDQzf-Z50)

#### FLIR Boson 640 \([manufacturer](https://www.flir.com/products/boson/), [GroupGets](https://store.groupgets.com/collections/frontpage/products/flir-boson-640)\)

Same as the 320 model, but with higher resolution.

