# Audio

Not everybody uses this feature, but in some use cases it might be necessary to transmit Audio from the Air unit to the Ground unit as well. This is disabled by default as there are many options that can not be auto detected.

### Microphones

Currently 3 tested options

* A Linux compatible 3.5mm audio in/out USB stick with separate CCTV style 5v or 12v powered mic. \(best option\)
* The small all in one mic \(smallest but poor/very low volume\)
* Logitech C920 webcam \(great audio input/output and if the webcam part of the video feed can be eventually matured it should be plug and play for video/audio\)

![The currently supported microphones](../.gitbook/assets/image%20%2821%29.png)

### Audio out on Ground

For hardware you can use the 3.5 jack, or HDMI output on the ground station. Please make the following modifications in the `openhd-settings-1.txt` file in the `boot`partition of the SD card for both Air and Ground unit.

```text
DefaultAudioOut=2 #0 Auto, 1 Analog, 2 HDMI
IsAudioTransferEnabled=1
MicBoost=75
SpeakersLevel=75
```

