---
description: Change Camera settings, like resolution, framerate,...
---

# Camera Settings

OpenHD evo allows you to change camera settings like resolution, framerate and more live without a reboot.\
Example:\
![](<../.gitbook/assets/Screenshot from 2022-11-12 19-26-07.png>)\
\
NOTE: While there is some user input validation(s), some parameters cannot be completely validated. It is recommended to have an eye on your video stream while chaning camera settings like resolution@framerate.\
If your video stream "stops working" suddenly, check the log in QOpenHD - if there are many "restarting camera,check your parameters / conenction" errors you probably set an unsuported value (e.g. 720p120fps on rpi). In most cases, you can recover from this error by selecting a supported video resolution (like 720p30fps on rpi).
