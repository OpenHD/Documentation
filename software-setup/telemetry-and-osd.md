# Telemetry and OSD

{% hint style="warning" %}
With Ardupilot you may need to enable certain "stream rate" parameters on the flight controller. More information is available on the rc with mavlink page
{% endhint %}


# Wiring

* Connect the serial port TX pin of your flight controller to the serial port RX pin on the Pi. _**WARNING:**_ The Pi uses 3.3V logic level on the serial ports, make sure your flight control also uses 3.3V. 5V might destroy the Pi serial port! So don't connect the + 5V ! \(See [https://pinout.xyz/](https://pinout.xyz/) for pinout\).

