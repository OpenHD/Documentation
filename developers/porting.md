# Running OpenHD and QOpenHD on "unsupported" Hardware WIP

{% hint style="warning" %}
This isn't a complete guide, also it does require deep insights how linux is working and needs manual debugging.
{% endhint %}

### What do we need before we can start porting OpenHD (for Air)

If you want to run OpenHD on "unsupported" hardware you need to first look at the specs of your device, it should have:

1. camera support
2. a hardware encoder which supports h264 and optionally h265 with at least 720/60fps
3. a USB port
4. at least 512MB RAM*
5. a modern Linux kernel 5.0+ *
6. a USB port
7. you need to find a low latency Gstreamer encode pipeline**


*can also be done with less memory and a lower kernel number, but this will further complicate the situation
**there is no general rule, how to find a low latency encoder, in general you need to look after it being HW-accelerated and test and optimize it


{% hint style="info" %}
Here is a example pipeline, which was used on the raspberry pi for debugging:

gst-launch-1.0 v4l2src io-mode=dmabuf device=/dev/video0 ! "video/x-raw,format=(string)UYVY, width=(int)1920, height=(int)1080,framerate=(fraction)30/1" ! v4l2h264enc extra-controls="controls,repeat_sequence_header=1,h264_profile=1,h264_level=11,video_bitrate=5000000,h264_i_frame_period=15,h264_minimum_qp_value=10" ! "video/x-h264,level=(string)4" ! queue ! h264parse config-interval=-1 ! rtph264pay mtu=1024 ! udpsink host=127.0.0.1 port=5500
{% endhint %}



### Camera support

First thing you need to look after is that your SBC has a mipi-csi connector for plugging in low latency cameras.

Sadly MIPI is only a connector standard, it doesn't mean that all mipi cameras can be connected.
You need a Kernel Overlay (dto/dtbo/dts), with you can use to compile your kernel with camera support.
* If you can't find any or do only find support for bad camera, you are stuck and can't just write the files yourself, since this needs deep insights in registers which are usually kept behind nda's.
For most Cameras you also need a tuning file, in which special parameters are setup and a camera-driver.

If the SBC-Vendor lists official Camera support the above step could not be necessary.

*This files are board specific, even if you find a SOC with the same processor you can not just use that, it includes specific things like the pin-out and much more.

### What do we need before we can start porting OpenHD (for Ground)

For the ground we need to make sure that the SBC has a potent h264/h265 decoder, and a good documentation. 

1. find a low latency Gstreamer decode pipeline*
2. look up how the compositor on you sbc works
3. have a relative new Kernel (5.0+)[makes the experience easier]

* there is no general rule, how to find a low latency encoder, in general you need to look after it being HW-accelerated and test and optimize it

{% hint style="info" %}
Here is a example pipeline, which was used on the raspberry pi for debugging:

gst-launch-1.0 udpsrc port=5600 caps='application/x-rtp, media=(string)video, clock-rate=(int)90000, encoding-name=(string)H264' ! rtph264depay ! 'video/x-h264,stream-format=byte-stream' ! fdsink | hello_video.bin
{% endhint %}

The easiest way is to look if your SBC allows multiple layers in your compositor, which allow the video to run behind QT and make the QT background invisible.

### Wifi-Drivers (Air/Ground)

First you need to think about what network card you want to use. 
If you decide to just use the 8812au you're lucky and can install the driver quite easily.

For 8812au, 8812bu you just need to use DKMS to compile the drivers from us :

https://github.com/OpenHD/rtl8812au
https://github.com/OpenHD/rtl88x2bu

For atheros compatibility you need:
1. the right firmware to be copied to the folder where your kernel loads the firmware file:
https://github.com/OpenHD/OpenHD-KernelBuilder/tree/2.3.1-evo/overlay/lib/firmware/ath9k_htc
2. you need to build a custom kernel and port a few kernel commits, we did (this is quite tricky, you can't just apply them and it works)

### Compiling OpenHD (Air/Ground)

If you have your drivers compiled, we can go on with compiling OpenHD from source.

1. you need to clone our github repository: https://github.com/OpenHD/OpenHD
2. determine which dependencies you need (a good help are our  install_dep_ files)
3. install the dependencies
4. install a modern version of cmake
5. execute build_cmake.sh 

Now you should have a base setup and just need to modify OpenHD with your pipelines, if you're lucky there are already some in there.

### Compiling QOpenHD

Before starting to build QOpenHD we need to explain how QOpenHD runs on our SBC's.

1. we use QT 5.15.x, lower versions will not work*
2. we use EGLFS for SBC'S to get the most out of that hardware*
3. if you do not have support for multiple HW-layers, like on the Pi with KMS you need to write a decoder-helper which copies the video to a texture and build a renderer for it.

* if your linux is to old, you need to build QT yourself, this is a pretty intense process and can take up to 20h to build on lower end SBC'S (the pi4 needs about 8h)
it also needs modifications and you need a mkspecs configuation(for that platform) to build QT on the hardware itself

Then you need to figure out the dependencies (a good help are our  install_dep_ files)
After you got everything prepared you can simply build QOpenHD with build_qmake.sh 

### Finding a KMS-Plane for HW-decoding

I usually use modetest to look at possible planes for kmssink.
You need the package libdrm-tests.

then execute "modetest -p" and check if the plane is behind qopenhd

