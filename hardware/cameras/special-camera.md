# Special Use Case Cameras

> :warning: **Important Note:** Special Use Case Cameras are currently supported only on the Raspberry Pi.

## Thermal Cameras

### Camera Overview

OpenHD supports a variety of thermal cameras, including the Hti-301, Infiray T2, and others.

Thermal cameras typically connect via USB and need to be enabled as secondary cameras.


### A Warning

Thermal cameras are not like ordinary cameras. It's important to review available information about each camera before making any purchase decisions.

Surprisingly, a thermal camera with a resolution of 204x156 can be notably worse than one with an 80x60 resolution. The entire thermal imaging system matters, from lens material and size to the sensor type, sensor resolution, and image post-processing by the camera.

Any weak link in the system can severely degrade the image, making it unsuitable for specific uses. Sometimes, this trade-off is acceptable to achieve a lower price point.

Additionally, remember that while a thermal camera might be useful for close-up electronics work or basic household tasks, it may not perform well for drone flight.

### Legal Restrictions

Thermal cameras are highly regulated items, so legal requirements can impact purchasing decisions. Depending on your location, you may need to pay a higher price, obtain licenses, or face limitations on buying certain cameras.

Regulations often center around frame rate, not resolution. This is due to the potential use of thermal cameras in weapons.

For countries part of the Wassenaar agreement, buying 30/60Hz thermal cameras is possible, although prices may be higher if imported from the United States.

Direct purchase options are available from Chinese companies like Hti Instrument on platforms like AliExpress and TaoBao. If obtaining FLIR or Seek cameras from the U.S. proves difficult, alternatives like Hti might be more accessible.

### Flying with a Thermal Camera

Consider what you will realistically see with a specific thermal camera in various situations.

Low-resolution thermal cameras might show a hot object in an area but not identify it. While this could work for search and rescue, situations requiring higher thermal resolution might necessitate better cameras.

Remember that thermal cameras have much lower resolutions compared to typical FPV cameras. For instance, a 1280x720 FPV camera has 48x the resolution of a 160x120 thermal camera. At greater distances, the main FPV camera might be able to see an object while the thermal camera cannot.

Also, consider the thermal "span" of the area in view. If everything has nearly the same temperature, the image could be noisy or flat. In such cases, a low NETD rating and a larger lens are necessary.

### Camera Information

Here are brief descriptions of individual cameras mentioned earlier. Carefully read this information before purchasing any of them.

#### Hti-301

A high-quality thermal camera with 384x288 resolution, a large germanium lens, and a 25Hz frame rate. Though more expensive, its thermal performance is excellent. These cameras work as regular webcams, requiring no special driver.

![Hti-301 Thermal Camera](https://github.com/OpenHD/OpenHD/blob/fc9d050b3d8d9bc2493895b558ee2f13f6ec15b1/wiki-content/Thermal-Cameras/hti-301.jpg?raw=true)

#### FLIR Boson 320

A 320x256 thermal imager core with a 60Hz frame rate. Expensive but equipped with Germanium lenses. Primarily designed for integration in larger camera systems or drones. Requires an appropriate connection board. Export controlled due to the high frame rate.

![FLIR Boson 320 Thermal Core](https://github.com/OpenHD/OpenHD/blob/fc9d050b3d8d9bc2493895b558ee2f13f6ec15b1/wiki-content/Thermal-Cameras/flir-boson-320.jpg?raw=true)

### Lenses

The lens on a thermal camera isn't ordinary glass (which doesn't allow IR wavelengths to pass through).

Germanium lenses offer high-quality thermal images but are costly. Many lightweight thermal cameras use Silicon or Chalcogenide lenses instead.

In most cases, you can't replace a thermal camera lens unless it's designed for it. Even cameras with removable lenses often require careful handling to avoid damage.


<!-- The following content is commented out for future use.
#### Seek Compact \([manufacturer](https://www.thermal.com/compact-series.html), [Amazon](https://www.amazon.com/Seek-Thermal-CompactPRO-Resolution-Imaging/dp/B00NYWAHHM)\)

These cameras are inexpensive but have significant lens and sensor issues. A FLIR One G2 is a better option if cost is a primary concern.

#### Seek Compact Pro \([manufacturer](https://www.thermal.com/compact-series.html), [Amazon](https://www.amazon.com/Seek-Thermal-CompactPRO-Resolution-Imaging/dp/B07V34RFLW)\)

Model numbers for these cameras do not end with an X (e.g., UQ-AAA). They are better than the non-pro model, featuring a 320x240 sensor and Chalcogenide lens. Noise may be noticeable in scenes with a small thermal span.

Seek has updated these cameras over time, improving the sensor and firmware.

#### Seek Compact Pro FastFrame \([manufacturer](https://www.thermal.com/compact-series.html), [DigiKey](https://www.digikey.com/en/products/detail/seek-thermal/UQ-AAAX/10230124)\)

Model numbers for these cameras end with an X (e.g., UQ-AAAX). The UQ-EAAX is an export version but is otherwise identical. Similar to the regular Pro, but frame rate is not locked at 9Hz and can exceed 15Hz. Export controlled due to frame rate.

#### Hti-201 \([manufacturer](https://hti-instrument.com/products/ht-201-mobile-phone-thermal-imager)\)

These are similar to Seek Compact Pro cameras and are essentially clones. The camera housing has an awkward shape compared to other thermal cameras.

Real world flight video:

[![FLIR Boson 320 flight](https://github.com/OpenHD/OpenHD/blob/fc9d050b3d8d9bc2493895b558ee2f13f6ec15b1/wiki-content/Thermal-Cameras/flir-boson-320-flight.jpg?raw=true)](https://www.youtube.com/watch?v=PQGDQzf-Z50)
-->
