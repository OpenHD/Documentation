# RPI HDMI to CSI

The RPI HDMI to CSI adapter is not a product officially supported by the rpi foundation, and therefore it has some quirks. Here is a quick list:\
\
1\) The encoder bitrate controll does not work properly - it regularily suffers from overshoot / undershoot. Disable variable bitrate, and manually set a reservative bitrate like 8MBit/s for MCS3\
\
2\) Changing resolution, framerate is buggy and often straight out doesn't work. It is recommended to set the camera resolution to exactly the resolution / framerate your camera outputs via HDMI\
\
3\) The RPI HW encode maxes out at 1080p@30 / 720p@60. Don't select a HDMI output video signal higher than that in your camera.\
\
4\) To reliably detect the HDMI to CSI adapter at boot, OpenHD needs to be powered after your HDMI camera. E.g. the adapter needs to have a valid HDMI input signal when the air pi is bootet up.\
