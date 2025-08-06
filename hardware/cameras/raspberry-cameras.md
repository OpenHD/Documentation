# CSI Camera Modes on Raspberry Pi

<!-- LEGACY DOCUMENTATION NOTICE -->
> ⚠️ **This documentation is outdated!** A current version is available at [openhdfpv.org](https://openhdfpv.org)
> 
> [📖 **View Updated Version of This Page** →](https://openhdfpv.org)

---


> :warning: **Important Note:** OpenHD does not support ANY autofocus cameras due to their impracticality on equipment with vibrations, such as drones. This restriction includes the official Raspberry Pi V3 lineup.

On the Raspberry Pi, you have the option to choose between two CSI camera modes.

## 1. Broadcom MMAL (Legacy Camera Stack)

The Broadcom MMAL mode is the legacy camera stack. It only works with original Raspberry Pi Foundation cameras or clones that have the security chip. While it offers better latency compared to libcamera, it has been deprecated by the Raspberry Pi Foundation in favor of libcamera. OpenHD uses Broadcom MMAL as the default option, as done in previous OpenHD releases.

## 2. Libcamera

The libcamera mode works with both original Raspberry Pi Foundation cameras and a wide range of other cameras. Generally, you can achieve the same or even better image quality using libcamera by selecting the appropriate CSI camera. However, it might not provide the same latency as broadcom mmal.

You can switch between Cameras using QOpenHD (V_OS_CAM_CONFIG), but it requires a reboot.

> **Note:** Autodetection is not available for identifying whether you've connected a camera supported only by libcamera/libcamera-ardu. You must manually select the appropriate CSI camera mode in QOpenHD for OpenHD to detect your CSI camera.

> **Note:** We use a proprietary version of the libcamera library, which ensures compatibility with arducam and normal libcamera while also providing image adjustments which are normally excluded in gstreamer-libcamera. This version is licenced to OpenHD and not Open Source.

> **Tip:** When choosing between the camera modes, consider your latency and image quality requirements along with the compatibility of the camera you are using.
