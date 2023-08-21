# IP cameras

> :warning: **Important Note:** IP camera support has limitations and should be chosen carefully, considering its disadvantages.

IP cameras cannot be automatically detected, as they lack a common protocol like USB cameras. They also require custom scripting for integration and lack support for bitrate adjustments, making them quite bad for long range sytems. They also don't support adjusting the keyframe interval, which can black out your video for several seconds when having any interference.

To implement IP cameras, you can utilize the [custom_unmanaged_camera.sh](custom-unmanaged-camera.md) script, which needs to be activated through the [hardware.conf](../hardware.md) configuration.


# Warning

IP-Cameras are not specifically designed for low latency, and many of them have latency upwards of 500ms+, but there are specific cameras available for purchase that have reasonable latency closer to 100-200ms. Remember this latency will be added to the "normal" latency your system has. So most IP-Camera Setups will have 300-600ms latency. It is not recommended to use an IP-Camera as primary camera.
That means the main reason to choose an IP-Camera is to enable some custom features normal Cameras do not support.
