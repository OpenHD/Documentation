---
description: Enable bidirectional telemetry between your FC and OpenHD
---

# Telemetry

There are 2 ways to connect your OpenHD air unit to your FC:

1\) (Reccomended): Using the HW UART from your air unit (e.g. see below for RPI) and one HW UART from your FC\
2\) (not recommended): Using an USB cable on FC that support it (e.g. PX4).\


{% hint style="warning" %}
With Ardupilot you may need to enable certain "stream rate" parameters on the flight controller. More information is available on the rc with mavlink page
{% endhint %}

## **1)** En**able UART in OpenHD**

By default, UART telemetry is disabled in OpenHD. You can enable it in QOpenHD using the AIR(TMP) Settings registry (FC\__UART\_CONN) and selecting serial0._\
__\
_Make sure to select the baud rate matching your FC._

__![](<../.gitbook/assets/Screenshot from 2022-11-12 19-19-37.png>)__

## 2) Wiring

* Connect the serial port TX pin of your flight controller to the serial port RX pin on the Pi. _**WARNING:**_ The Pi uses 3.3V logic level on the serial ports, make sure your flight control also uses 3.3V. 5V might destroy the Pi serial port! So don't connect the + 5V ! (See [https://pinout.xyz/](https://pinout.xyz/) for pinout).\


