# Using only a USB Camera

Open.HD currently detects whether it is an Air or Ground unit by looking for an CSI camera. If one is found, the system assumes the role of the Air unit. When you use a USB camera as the main camera, the system will not find a CSI connected camera and will assume the role of Ground unit.

To prevent this, place a file called `air.txt` on the `boot` partition of the SD Card you use in the Air SBC. This forces the Open.HD system into Air unit mode.

Inside `openhd-settings-1.txt` change these settings:

```text
SecondaryCamera=No
IsCamera1Enabled=0
```

To

```text
SecondaryCamera=USB
IsCamera1Enabled=1
```

Now enable the band switcher:

```text
IsBandSwicherEnabled=1
```

And remove the comment before this line

```text
#USBCamera="gst-launch-1.0 videotestsrc... 

to

USBCamera="gst-launch-1.0 videotestsrc... 
```

Now turn on the Air and Ground unit. If all is working as intended you will see a test video stream. Now that you know the basics are working we can send the actual video by changing the `USBCamera` setting to an appropriate pipeline for your USB camera. 

Since this depends heavily on the camera used there is no single solution. We are working on adding predefined pipelines for known cameras. Several examples are included in the config file for now, use these as a starting point.



