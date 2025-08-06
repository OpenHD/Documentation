# Running OpenHD and QOpenHD on "unsupported" Hardware

<!-- LEGACY DOCUMENTATION NOTICE -->
> ⚠️ **This documentation is outdated!** A current version is available at [openhdfpv.org](https://openhdfpv.org)
> 
> [📖 **View Updated Version of This Page** →](https://openhdfpv.org)

---


**Note: This guide is a work in progress and requires a deep understanding of Linux systems and manual debugging.**

## Introduction

Running OpenHD and QOpenHD on hardware that is not officially supported requires careful consideration of hardware specifications, Linux kernel behavior, and manual debugging. This guide outlines the essential requirements and steps to achieve this.

### Prerequisites

Before attempting to run OpenHD on unsupported hardware, make sure your device meets the following criteria:

1. **Camera Support:** Your hardware should have a mipi-csi connector for connecting low-latency cameras, parallel MIPI or other alternatives are not usable. (ov5647 is not a usable camera for outdoors)

2. **NEON HW-Acceleration:** Ensure your hardware supports NEON HW-acceleration for OpenHD forward error correction, without it you won't have video at all.

3. **Hardware Encoder:** The device must feature a hardware encoder capable of supporting h.264 and optionally h.265 formats at a minimum of 720/60fps.

4. **USB Port:** A USB port is required for interfacing with the Wifi Card.

5. **Minimum RAM:** Your hardware should possess at least 512MB of RAM. Lower configurations can work but may complicate the process.

6. **Modern Linux Kernel:** Make sure your hardware runs on a modern Linux kernel version 5.0 or higher for optimal compatibility.

7. **Gstreamer Encode Pipeline:** Find or create a low-latency Gstreamer encode pipeline that is hardware-accelerated for efficient video encoding.

### Camera Support (Air)

To enable camera support for OpenHD on unsupported hardware, follow these steps:

1. Verify if your Single Board Computer (SBC) has a mipi-csi connector compatible with low-latency cameras. (ov5647 is not a usable camera for outdoors)

2. Create a Kernel Overlay (dto/dtbo/dts) that adds camera support to your kernel. This overlay will need to be used during kernel compilation.

3. Look for official sensor support listed by the SBC vendor. These sensors can usually be used in OpenHD.

4. All cameras without inbuild ISP require a tuning file with special parameters. Ensure you have the necessary tuning file for your camera, SOC and ISP, it needs to be specifically tuned to your configuation. If there is no tuning fila available, you are out of luck, there are some companies which create these tuning files, but their services start at 10000USD and go way up with complexity and low order-numbers.

### Ground Setup

For OpenHD on the ground, consider the following steps:

1. **Decoder Support:** Make sure your SBC has a capable h.264/h.265 decoder and proper documentation.

2. **Gstreamer Decode Pipeline:** Create a low-latency Gstreamer decode pipeline. Hardware acceleration should be a priority for optimal performance.

3. **Compositor Configuration:** Understand how the compositor on your SBC works, particularly if it supports multiple layers for smooth video playback behind other elements, for this you either need a custom decoder, which is capable to write directly into the compositor without checking for KMS-Master's or you need a compositor which allows multiple kms master.

### WiFi Drivers (Air/Ground)

When dealing with WiFi drivers, consider these options:

- For 8812au or 8812bu chipsets, installation can be relatively straightforward.
- compile the drivers using DKMS or make from the provided repositories:
  - [rtl8812au](https://github.com/OpenHD/rtl8812au)
  - [rtl88x2bu](https://github.com/OpenHD/rtl88x2bu)

### Compiling OpenHD (Air/Ground)

To compile OpenHD from source, follow these steps:

1. Clone the [OpenHD repository](https://github.com/OpenHD/OpenHD) (including submodules).

2. Determine and install required dependencies. The `install_build_dep` file can be helpful for this.

3. Install a modern version of CMake.

4. Execute the `build_cmake.sh` script.

This should set up the base environment, and you can modify OpenHD with your specific pipelines.

### Compiling QOpenHD

For compiling QOpenHD, the user needs to be aware of the following:

1. Use QT version 5.15.x or higher.

2. Employ EGLFS for SBCs to maximize hardware utilization.

3. Ensure support for multiple hardware layers to prevent high latency and software decoding.

4. Study the decode-services and integrate custom ones as needed.

For compiling QOpenHD, follow these steps:

1. Ensure the Linux system has a QT 5.15.x. installation

2. Compile mavsdk with the necessary modifications.

3. Compile QOpenHD using the `build_qmake.sh` script.

### Finding KMS-Planes for HW Decoding

To identify KMS-planes for hardware decoding, follow these steps:

1. Install the `libdrm-tests` package.

2. Use `modetest -p` to check for available planes for `kmssink`.

### Debugging

Logging is via standard Linux journalling

1. Open a second terminal and type `journalctl -f` for "live" logs

## Conclusion

Running OpenHD and QOpenHD on unsupported hardware requires a deep understanding of hardware capabilities, Linux kernel features, and the intricacies of video processing. By following the steps outlined in this guide, you can work towards achieving successful implementation on your chosen hardware. Keep in mind that the process may involve trial and error, as well as manual debugging to overcome potential challenges. Also keep in mind, that the developers can not help you with every step, if you are not capable of doing it without much help, please use the supported platforms.
