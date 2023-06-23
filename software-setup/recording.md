In OpenHD, there are 2 possible ways for recording your flight to share it on youtube and more.

1) Air recording:
Record video locally on your Air unit. This eliminates any breakups / interference that might happen during flight from the recorded video.
NOTE 1) The RPI HW is not capable of recording the video with OSD - see 2) for that \
NOTE 2) The bitrate of the air recording is the same bitrate as used for transmission \

2) Ground recording:
Due to the HW limitation of RPI not being able to record Video + OSD at the same time, we recommend the following user-proven option:
Use QOpenHD on a tablet, android phone and a screen recorder (TODO which) to record the video and osd.
If you are using a (strong) x86 laptop on the ground, you can obviosly also use the integrated screen recording.


Air recording - enable / disable:
You can either manually enable / disable recording of your primary / secondary camera via QOpenHD, or (recommended) use the following feature:
Automatically start / stop recording when you arm / disarm your FC.
To use this feature, go to QOpenHD / CAMERA1 (or CAMERA2) and set V_AIR_RECORDING to AUTO(armed)
Your air recording will now automaticallly start / stop when you arm / disarm your drone, and you can download the recording
after flight. Note that when AUTO(armed) is enabled, the QOpenHD air recording widget should not be used
( you can check the remaining space counter though to validate if air recording is working or not).

 NOTE: If there is not enough free space on your air unit (SD Card), air recording is automatically stopped.
