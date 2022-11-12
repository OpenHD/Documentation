---
description: CSI camera modes on RPI
---

# Raspberry

You can choose between 2 CSI camera modes on raspberry pi.\
\
1\) broadcom mmal (legacy camera stack). Only works with original rpi foundation cameras (or clones with security chip). It offers better latency than libcamera, but is deprecated by the RPI foundation in favour of libcamera. We use it as default in OpenHD, just like previous OpenHD releases.\
\
2\) libcamera / libcamera-ardu: Works with original rpi foundation cameras AND a wide variety of other cameras. In general, you can achieve the same or often better image quality with libcamera (by chosing the right CSI camera) but not the same latency as with broadcom mmal.\
\
You can switch from broadcom mmal to libcamera and back via QOpenHD (requires a reboot). \
\
Note: We cannot autodetect wheather you connected a camera that is only supported by libcamera/ libcamera-ardu. You have to manually select the right CSI camera mode in QOpenHD, then OpenHD can detect your CSI camera.
