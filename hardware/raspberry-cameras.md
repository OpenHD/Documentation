# Raspberry Cameras

The lowest latency on the Raspberry can currently be archieved with RaspiCamSrc, which uses proprietary code from Broudcom.
This code is not actively developed anymore, but can be used very safely. We enable this mode as default. 

The Raspberry Foundation developed a new Camera-Subsystem called Libcamera, this is an opensource Project, but currently lacks some features and introduced additional latency.
Libcamera also does currently not allow to use a Veye-Camera.
And needs to be enabled in our Configuator or with adding a "libcamera.txt" to /boot/OpenHD

You can also use HDMI, USB and IP-Cameras on the Raspberry Pi