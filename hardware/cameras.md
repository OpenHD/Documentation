# Cameras

### Overview

{% hint style="danger" %}
While many cameras can potentially work, latency is the biggest issue. Please read the Camera pages to fully understand all variables.
{% endhint %}

Since we now support multiple platforms, Camea-Support needs to be split into multiple cathegories, since not every platform supports every camera.

The Raspberry Foundation developed a new Camera-Subsystem called Libcamera, this is an opensource Project, but currently lacks some features and introduced additional latency.

{% hint style="danger" %}
When using multiple Cameras you need to choose one Camera-Subsystem, so you can not use libcamera and raspicam at the same time.
This means f.e. you can not use an Veye-Camera and an Arducam camera at the same time.
{% endhint %}


