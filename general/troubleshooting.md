# Troubleshooting

On this page we're documenting, the most appearing "bugs/issues" and how to fix them, also we're adding a little troubleshooting information, which will help to understand and document the issue you're having.

#### WIFI-LED is off or not continiously on

In the newer Realtek drivers the LED isn't controllable anymore, meaning we can not turn it on to show that the device is working.

Since we can not control it, blinking or not even turning on the LED is no indicator of the device or software is malfunctioning.

#### (Air) Terminal is shown and no stats ?

In evo we do not have any display-stats or indicator that the software is running. It'll show up a regular Terminal for debugging. 
OpenHD is setup to automatically setup and connect. On the Air you just get a Command Prompt and no interaction is needed.


If you want to see if openhd is running, you can type in "systemctl status openhd", this will show some stats.

#### (Ground) Terminal is shown and no OSD ?

OpenHD is setup to automatically setup and connect. On the Ground you should get QOpenHD (our OSD). 
If it didn't you may have made an error while flashing, please remember selecting GROUND while writing your SDCard.


#### My RPI-0,1,2 doesn't work

With OpenHD evo we stopped support on some platforms, all ARMv6 devices are not supported anymore.

#### Where are the extended settings for my veye camera

We don't have extended i2c settings for veye cameras, since veye didn't integrate them in standard v4l2 controls.

#### I can't get my custom display to work

If you need special drivers and need to use KMS as the display driver, we can not support that, since low latency modes are only available on FKMS.


### Troubleshooting steps

1. Make sure all your devices are powered via seperate BEC's and you have a keyboard available
2. You can check the status of openhd with "systemctl status openhd"
3. For better debugging please download the journal from our webinterface and provide it when contacting us in our Telegram Chat.
