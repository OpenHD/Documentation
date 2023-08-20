# Cameras

### Overview


In general, OpenHD can automatically detect and use usb cameras that provide either raw uncompressed or 
already encoded (h264,h265,mjpeg) data.
However, they often (not always) come with limitations:

1) Fixed encode bitrate - you cannot use new features like variable bitrate, and need to manually tune your link
2) Not ideal encoding parameters - your stream might have high latency, or bad error recovery
3) RAW - requires SW encoding, which only allows low resolutions/framerates, even on RPI 4
