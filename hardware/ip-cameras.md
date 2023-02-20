#IP cameras

{% hint style="danger" %}
IP-Camera support is currently under development and not ready yet.
{% endhint %}

IP cameras cannot be autodetected (since they don't share a common protocol, like USB cameras) and also require custom scripting
(Editing settings / pipeline(s) manually via a text editor)
They also don't support new features like changing the bitrate dynamically at run time. However, if you need to use an IP camera
(for whatever reason) we will publish a howto (for advanced users) here shortly. 

#Warning

IP-Cameras are not specifically designed for low latency, and many of them have latency upwards of 500ms+, but there are specific cameras available for purchase that have reasonable latency closer to 100-200ms. Remember this latency will be added to the "normal" latency your system has. So most IP-Camera Setups will have 300-600ms latency. It is not recommended to use an IP-Camera as primary camera.
That means the main reason to choose an IP-Camera is to enable some custom features normal Cameras do not support.
