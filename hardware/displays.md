# Displays

<!-- LEGACY DOCUMENTATION NOTICE -->
> ⚠️ **This documentation is outdated!** A current version is available at [openhdfpv.org](https://openhdfpv.org)
> 
> [📖 **View Updated Version of This Page** →](https://openhdfpv.org)

---


## Supported Display Options

Virtually any screen/monitor connected to the HDMI port on your Pi will work. Additionally, the following displays have been successfully tested:

> **Note 1**: The type and model of your monitor will affect the latency since response time, picture enhancement, and refresh rate will add latency. The best latency can be achieved with low response time, gaming monitors with a refresh rate of more than 120Hz.

## Screen Scale

When using QOpenHD on embedded devices such as RPI or ROCK with displays exceeding 720p resolution, it may be necessary to manually adjust the screen scale, affecting the size of text and UI elements.

To make these adjustments, follow these steps:

1. Navigate to OSD / Screen in the QOpenHD interface.
2. Locate the option to adjust the screen scale.

Recommended values for different resolutions:

- ≥720p: Default (1.0)
- ≥1080p: 1.5
- ≥4k: 2.0

## DSI Displays

On the Raspberry Pi, we're using the FKMS driver to enable low latency decoding. Some of the newer monitors require the KMS driver, which does not work with OpenHD. Only Official Raspberry Pi DSI monitors can use FKMS.
Some DSI vertical displays are not supported since they are mnade to work vertically and cant be changed

## Zeiss Cinemizer OLED

Please note that the monitor has to be connected and powered before the Pi is powered on because the auto-detection only works at start-up. You can define your (custom) monitor resolution in `config.txt` statically to connect the monitor after the Pi is already running. Also, make sure to uncomment `hdmi_force_hotplug=1` to enable "hotplugging" for your HDMI monitor/goggles.

## Using a Phone or Tablet

Regardless of the monitor attached directly to the Ground SBC, you can use a phone or tablet running the official [QOpenHD App](https://play.google.com/store/apps/details?id=com.openhd.openhd).

> **Note 2**: When using your phone or tablet, dual video doesn't work, and the latency might be slightly higher.

> **Warning 1**: When using your phone/tablet as the only display (connected to the ground station), the viewing experience is less than ideal, and there might be stutters and lost frames.

## Using a Laptop Combined with the X86 Releases

In Evo, we added the possibility to use your existing laptop as a ground station. For this to work, you either need the USB-Image and boot from it or install OpenHD using the OpenHD X86 installer.

> **Warning 2**: When using your X86 device, your experience (latency, framerate, etc.) depends on the power of your device. On more powerful devices, the latency is much less than on the Pi. On older/less powerful devices, it may be higher.

## Dual Display Setup

> **Note 3**: Dual display setup isn't working because of the low latency video decode we use. On X86, it will work without issues. On the Pi, there is no capability to do so without adding a lot of latency.
