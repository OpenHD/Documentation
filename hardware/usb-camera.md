# Cameras

### Overview

{% hint style="danger" %}
Most USB Cameras will create higher latency.
{% endhint %}


In general, OpenHD can automatically detect and use usb cameras that provide either raw uncompressed or 
already encoded (h264,h265,mjpeg) data.
However, they often (not always) come with limitations:

1) Fixed encode bitrate - you cannot use new features like variable bitrate, and need to manually tune your link
2) Not ideal encoding parameters - your stream might have high latency, or bad error recovery
3) RAW - requires SW encoding, which only allows low resolutions/framerates, even on RPI 4

### Warnings

Some USB 3.0 cameras _might_ be capable of ultra-low latency when paired with a suitable SBC with a zero-copy video processing pipeline, but in most cases USB cameras are only suitable when they have an internal h264/h265 encoder. (currently there is no known usb camera, which is able to achieve lower latency then a csi camera)