# Displays

## Supported Display Options

Virtually any screen/monitor connected to the HDMI port on your Pi will work. Besides that the following displays have been successfully tested:

* Samsung 32 inch TV connected via HDMI to Pi.
* Pi Official Touch Screen connected to DSI port on your Pi. Resolution 800x480.
* An LCD module from old 17 inch laptop with eBay driver [\(for example this\)](http://www.ebay.com/itm/HDMI-VGA-2AV-Lcd-controller-Board-VS-TY2662-V1-for-LCD-panel-Only-driver-board-/181596796562?hash=item2a48033692:g:TGEAAOSwQJhUdwFZ) using 1920x1080 to HDMI on Pi. Default FPS.
* Goggles One \(1920x1080\) \(set to fixed 1920x1080 resolution in config.txt!\)
* Headplay HD \(1280x800\)
* Fatshark Base HD \(1280x720\)
* Fatshark HDO \(960x720\)
* Fatshark HD1/2/3 \(800x600\) \(set to fixed 800x600 resolution in config.txt!\)
* Yuneec Skyview
* Zeiss Cinemizer OLED

Please note that the monitor has to be connected and powered before the Pi is powered because the auto-detection only works at start-up. You can define your \(custom\) monitor resolution in config.txt statically though to be able to connect the monitor after the Pi is already running.

## Using a phone or tablet

Regardless of the monitor attached directly to the Ground SBC you can use a phone or tablet running one of the following apps:

* [Mission Planner](../ground-station-software/mission-planner.md)
* [QGroundControl](../ground-station-software/qgroundcontrol.md)
* [Tower](../ground-station-software/tower.md)
* [FPV\_VR](../ground-station-software/fpv_vr.md)
* [RaspberryPi Camera Viewer](../ground-station-software/raspberrypi-camera-viewer.md)

{% hint style="info" %}
When using your phone or tablet we recommend using the QOpen.HD app which was designed specifically for this project.
{% endhint %}

The phone can be connected either via [USB Tethering](../advanced-setup/usb-tethering.md) or by connecting to the [Hotspot WiFi ](../advanced-setup/wifi-hotspot.md)network started by the Ground SBC if the SBC has an internal WiFi capable of working on a band other than the active Air connection.

## Using a Ground Station

In this scenario the Ground SBC acts as a proxy for the Video and Telemetry for a separate Groundstation. This can be anything you can think of as longs as it is able to interpret the Video and Telemetry and is able to connect to the Ground SBC.

Common examples of ground stations are:

* Laptops running [Mission Planner](../ground-station-software/mission-planner.md) or QGroundControl
* Tablets running APM Planner, Tower or one of the Open.HD specific apps \(see [Using a phone or tablet](displays.md#using-a-phone-or-tablet)\)

## Dual Display Setup

If you would like to use the Raspberry DSI "ribbon" style connection with the popular Raspberry Pi 7" LCD display, you can simply connect it and power it up.

The same goes for any HDMI display, however, by default they cannot be used simultaneously. A patch was created with the intention of implementing it with the stock image however, it created problems with the new Pi3 A+ because the patch did not work and the Pi3 A+ only has 512MB ram

#### If you want to use MIPI-DSI & HDMI Simultaneously:

**You might need to set resolution manually so HDMI matches the default Raspberry Pi DSI LCD Display.**

The official 7" Raspberry Pi LCD which is 800 x 480 might need to be set as the default resolution to match so that both displays come up.

**In the Openhd-settings.txt file**

```text
 #
 MirrorDSI_To_HDMI= "Y"
```

**In the config.txt file**

Change GPU memory to:

```text
gpu_mem="256"
```

Towards the bottom of config.txt file change the default field from

```text
  [pi3+]
  start_file=start_x.elf
  fixup_file=fixup_x.dat``
```

To This:

```text
  [pi3+]
  start_file=1to3b_x.elf
  fixup_file=1to3bup_x.dat
```

