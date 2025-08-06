# FAQ

<!-- LEGACY DOCUMENTATION NOTICE -->
> ⚠️ **This documentation is outdated!** A current version is available at [openhdfpv.org](https://openhdfpv.org)
> 
> [📖 **View Updated Version of This Page** →](https://openhdfpv.org)

---


#### I can't find the images.

The easiest way to flash OpenHD images is to use our ImageWriter, just select the Image in the drop down and click flash.

In the advanced tabs there are the images for X86 and Jetson devices.

#### Where are the config-files ?

With 2.3-evo we removed the complex config files. Everything is set up in QOpenhd or the ImageWriter.

#### I just get a command line, what do I need to do now?

OpenHD is setup to automatically setup and connect. On the Air you just get a Command Prompt and no interaction is needed.
On the Ground QOpenHD will start automatically and give you a GUI. If not you may have made an error while flashing, please remember selecting GROUND while writing your SDCard.

#### I don't want to use the ImageWriter, what do I need to do.

In general the image writer writes the image, mounts it and writes a file (air.txt) or (ground.txt) into the folder openhd. You just need to do this manually without the ImageWriter. In the future there may be a lot more functionality coming, which then just needs to be done manually.

#### I can't see the wifi-hotspot

You need to enable the hotspot in the QOpenHD settings first, it is disabled by default.

#### My camera is not detected, what can I do?

With 2.3-evo we extended the camera support a lot, but to do this we needed to add a way to handle all the new cameras. Autodetection isn't that easy anymore.
As default all MMAL cameras are selected, but you can select the right Overlay for your camera in AIR_tmp.
The overlays are listed in our camera-tabs in this wiki.

#### I just bought a camera which is not supported, how can I use it?

Not all cameras are usable, that's why we do not support each and every camera, you can try if it is compatible with one of our overlays, if not it isn't compatible.
In general we do not recommend (or actively) support Autofocus cameras, since they are highly susceptible to vibration which can even damage your camera.



