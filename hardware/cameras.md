# Cameras

### Overview

{% hint style="danger" %}
While many cameras can potentially work, latency is the biggest issue. Please read the Camera pages to fully understand all variables.
{% endhint %}

{% hint style="danger" %}
With the upcoming of many new camera's there is one thing we need to mention.
OpenHD is not supporting ANY autofocus cameras, since they are basically not usable on equipment with vibrations (like drones), this also includes the Raspberry V3-lineup
{% endhint %}

Since we now support multiple platforms, Camea-Support needs to be split into multiple cathegories, since not every platform supports every camera.

USB-Cameras are generally usable with any SBC.
HDMI-Cameras are currently only supported on the Pi-SBC's.
IP-Camera support is not ready, yet.

Some USB 3.0 cameras _might_ be capable of ultra-low latency when paired with a suitable SBC with a zero-copy video processing pipeline, but in most cases USB cameras are only suitable when they have an internal h264/h265 encoder. (currently there is no known usb camera, which is able to achieve lower latency then a csi camera)

IP-Cameras are not specifically designed for low latency, and many of them have latency upwards of 500ms+, but there are specific cameras available for purchase that have reasonable latency closer to 100-200ms. Remember this latency will be added to the "normal" latency your system has. So most IP-Camera Setups will have 300-600ms latency. It is not recommended to use an IP-Camera as primary camera.

{% hint style="danger" %}
When using multiple Cameras you need to choose one Camera-Subsystem, so you can not use libcamera and raspicam at the same time.
This means f.e. you can not use an Veye-Camera and an Arducam camera at the same time.
{% endhint %}

{% hint style="danger" %}
When using multiple Cameras the second camera is using Software decoding and encoding, it is not recommended to use a high quality camera. It is generally made for a thermal camera or something with lower resolutions.
{% endhint %}
