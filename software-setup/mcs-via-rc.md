Change your MCS index (bitrate) dynamically during flight using a dedicated (multi-position) switch on your RC

The MCS index is the main parameter that affects your video bitrate and maximum range. 
E.g. by increasing the MCS index, you increase your available bitrate but reduce range (and the other way around).
In OpenHD evo, you can change the MCS index during flight, given the following prerequisites:
1) You are using rtl8812au
2) Your camera supports variable bitrate (openhd can set your camera encoder bitrate)
3) Your FC reports your rc channels to openhd (ardupilot)

You can do so via QOpenHD and a touch screen.
However, with the use of directional antennas, it is common that you cannot reliably change parameters on your 
air unit close or at maximum range. This is why you can also configure OpenHD and your RC such that the MCS
index can be changed via a specific channel from your RC
-> If you reach maximum range at a given bitrate, or have trouble getting an image - flip a switch and reduce
the mcs index. This gives you full controll trading range and bitrate !

Setup:
1) You need a free channel on your RC that is transmitted over your RC link (works both with rc over openhd 
and rc via another link, e.g. ExpressLRS, Crossfire, ... which is also recommended for long range flights anyways
In this example, I am going to use Channel 7

2) Make sure your RC channels are forwared from the FC to the OpenHD air unit - in QOpenHD, go to RC -> FC CHANNELS DEBUG.
Moving channel 7 should give movement on channel 7.

2) Go to OpenHD / AIR and change MCS_VIA_RC from "DISABLED" to your selected channel (Channel 7 in this case)

Your setup in OpenHD is now completed - however, you need to transmit the right PWM values depending on your RC / Switch.
The mapping in OpenHD is as follows: (PWM on the selected channel)
// [900 ... 1200] : MCS0
// [1200 ... 1400] : MCS1
// [1400 ... 1600] : MCS2
// [1600 ... 1800] : MCS3
// [1800 ... 2100] : MCS 4

If you are using a 2 Position switch, it is recommended to configure the switch on your RC such that 
low = MCS1 = ~ 1300 PWM
high= MCS3 = ~ 1700 PWM
If you are using a 3 Postion switch, it is recommended to configure
low    = MCS1 = ~ 1300 PWM
medium = MCS2 = ~ 1500
high   = MCS3 = ~ 1700 PWM
MCS 3 is generally a good trade off between range & image quality
MCS 1 serves as a backup with greatly reduced image quality, but more range
However, you can obviously configure different configurations using different PWM values.



