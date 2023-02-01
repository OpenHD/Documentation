# Displays

## Supported Display Options

Virtually any screen/monitor connected to the HDMI port on your Pi will work. Besides that the following displays have been successfully tested:

{% hint style="info" %}
The type and model of your monitor will affect the latency, since response time, picture enhancement and refresh rate will add latency. Best latency can be archieved with low response time, gaming monitors with more than 120hz refresh rate.
{% endhint %}

* Samsung 32 inch TV connected via HDMI to Pi.
* Pi Official Screen connected to DSI port on your Pi. Resolution 800x480.
* An LCD module from old 17 inch laptop with eBay driver [(for example this)](http://www.ebay.com/itm/HDMI-VGA-2AV-Lcd-controller-Board-VS-TY2662-V1-for-LCD-panel-Only-driver-board-/181596796562?hash=item2a48033692:g:TGEAAOSwQJhUdwFZ) using 1920x1080 to HDMI on Pi. Default FPS.
* Goggles One (1920x1080) (set to fixed 1920x1080 resolution in config.txt!)
* Headplay HD (1280x800)
* Fatshark Base HD (1280x720)
* Fatshark HDO (960x720)
* Fatshark HD1/2/3 (800x600) (set to fixed 800x600 resolution in config.txt!)
* Yuneec Skyview
* Zeiss Cinemizer OLED

Please note that the monitor has to be connected and powered before the Pi is powered because the auto-detection only works at start-up. You can define your (custom) monitor resolution in config.txt statically though to be able to connect the monitor after the Pi is already running.
You also have to uncomment "hdmi_force_hotplug=1", so you will be able to "hotplug" your hdmi monitor / goggles.

## Using a phone or tablet

Regardless of the monitor attached directly to the Ground SBC you can use a phone or tablet running one of the following apps:

* [Mission Planner](broken-reference)
* [QGroundControl](../ground-station-software/qgroundcontrol.md)
* [Tower](../ground-station-software/tower.md)
* [FPV\_VR](../ground-station-software/fpv\_vr.md)
* [RaspberryPi Camera Viewer](broken-reference)

{% hint style="info" %}
When using your phone or tablet we recommend using the QOpenHD app which was designed specifically for this project. Will be updated to fully support EVO.
{% endhint %}

The phone can be connected either via USB Tethering or by connecting to the Hotspot WiFi network started by the Ground SBC. In EVO releases, band selection it's automated now. Also, an ethernet to usb adapter can be used, just enable ethernet hotspot in ground pi's settings in User Interface.

{% hint style="warning" %}
When using your phone/tablet as the only display (connected to the groundstation), the viewing experience is less then ideal, there might be stutters and lost frames.
{% endhint %}

## Using a Laptop kombined with the X86 releases

In Evo we added the possibility to use your existing Laptop to be used as a groundstaion.
For this to work you either need the USB-Image and boot from it, or install OpenHD using the OpenHD X86 installer.


{% hint style="warning" %}
When using your X86 device, your experience (latency,framerate,....) is dependend on the power of your device, on more powerful devices the latency is much less then on the pi. On older/less powerfull devices it may be higher.
{% endhint %}


## Dual Display Setup

Dual display setup isn't tested in Evo, but anyone who wan't to tinker with it can contact an developer for help.