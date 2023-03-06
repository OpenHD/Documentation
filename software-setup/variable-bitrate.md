# Variable Bitrate

To close the gap to other commercial FPV systems, one of the goals of OpenHD evo is to support variable bitrate. However, since OpenHD runs on a wide variety of devices/setups (which often at the hardware level do not properly support variable bitrate) this is easier said than done. Here is a quick list of things to watch out for (aimed at both experienced and new users).\
\
1\) As of 2.3.2, variable bitrate is on by default. This means OpenHD recommends bitrate(s) according to the selected link parameters to the encoder, and reduces the bitrate on TX errors. This only works on select camera(s) - see 3) !\
\
2\) To reduce the risk of pushing the link too much during flight, this version only ever automatically decreases the bitrate if needed, and never increases it back up. For more experienced user(s) that know their exact bitrate(s) we recommend disabling variable bitrate for now. \
You can disable variable bitrate using the QOpenHD parameter editor - go to OpenHD / Air(TMP) and disable:\
![](<../.gitbook/assets/Screenshot from 2023-03-06 21-29-49.png>)\
After that, you can manually adjust you encoder bitrate in the CAM1 (optionally CAM2) registry\
\
3\) A LOT of camera(s) (especially USB cameras, VEYE and the RPI CSI to HDMI adaper) do not properly support variable bitrate. To debug, take a look at the set and measured encoder bitrate - in case of  regular overshoot / undershoot,disable variable bitrate and tune your link according to your camera(s) need.\
Example of a camera properly adhering to the set encoder bitrate:\
![](<../.gitbook/assets/Screenshot from 2023-03-06 21-33-28.png>)\
\
4\) RTL8812AU (or other chips using the RTL88xxAU driver) are the only wifi card(s) supporting variable link rate(s). E.g. you can change the MCS index (modulation) and channel width (20Mhz or 40Mhz) on those cards, which increases / decreases the throughput (rate) of your RF link.\
\
