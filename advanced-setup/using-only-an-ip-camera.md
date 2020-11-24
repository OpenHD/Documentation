# Using only an IP Camera

Open.HD currently detects whether it is an Air or Ground unit by looking for an CSI camera. If one is found, the system assumes the role of the Air unit. When you use an IP camera as the main camera, the system will not find a CSI connected camera and will assume the role of Ground unit.

To prevent this, place a file called `air.txt` on the `boot` partition of the SD Card you use in the Air SBC. This forces the Open.HD system into Air unit mode.

Inside `openhd-settings-1.txt` change these settings:

```text
SecondaryCamera=No
IsCamera1Enabled=0
```

To

```text
SecondaryCamera=IP
IsCamera1Enabled=1
```

Now enable the band switcher:

```text
IsBandSwicherEnabled=1
```

And remove the comment before these lines:

```text
#IPCameraHiRes="gst-launch-1.0 rtspsrc...
#IPCameraLowRes="gst-launch-1.0 rtspsrc...

to

IPCameraHiRes="gst-launch-1.0 rtspsrc...
IPCameraLowRes="gst-launch-1.0 rtspsrc...
```

The settings in those two lines will need to be modified to suit your specific IP Camera and are only provided as a starting point.

