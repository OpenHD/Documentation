# RC over Serial

{% hint style="info" %}
Follow the instructions for [general ](general.md)RC setup first.
{% endhint %}

{% hint style="warning" %}
* Review your iNav board here before buying and connecting \([iNav boards](https://github.com/iNavFlight/inav/tree/master/docs)\)
* Only uninverted RC serial connections can be made
* Recommended and tested baud rate for RC is 115200
{% endhint %}

### Fundamentals of RC Control via Serial

Start by selecting the correct type of serial in the `openhd-settings-1.txt` file in the `boot` partition of SD card for the Air unit. Please change the following settings:

{% tabs %}
{% tab title="RC" %}
| Value | Description |
| :--- | :--- |
| sumd | Use the sumd serial protocol to send RC commands to the Flight Controller |
| ibus | Use the ibus serial protocol to send RC commands to the Flight Controller |
{% endtab %}

{% tab title="CTS\_PROTECTION" %}
| Value | Description |
| :--- | :--- |
| Y | Prioritizes RC uplink with RTS **Protection frames** and results in 10-15% **less** video bitrate. |
| N | Prioritizes Video downlink and uses data packets for RC. This might result in **small** RC **glitches** which are **not** usually a **problem** with **GPS** autopilots. |
{% endtab %}

{% tab title="FC\_RC\_BAUDRATE" %}
| Value | Description |
| :--- | :--- |
| 2400 to 115200 | The baud rate used to connect to the Flight Controller |
| 115200 | The most common baud rate and the default setting. |
{% endtab %}
{% endtabs %}

### iNav Configurator Settings

1. Connect your flight controller to the configurator and open the Ports tab
2. Turn on “Serial RX” on the UART you have connected the wire from the Air Pi TX pin. Now save settings
3. Open the Configuration tab. Under Receiver Mode select “RX\_SERIAL” and the protocol you choose above. Now save settings

### Wiring

Please make sure to follow the guidelines and precautions outlined in [Wiring ](../hardware/wiring.md)-&gt; [Flight Controller](../hardware/wiring.md#flight-controller), but since most INav boards function a bit differently in regards to the serial communication observe the following:

1. Connect the Air Pi tx pin to your flight controller UART RX pin.  This is the same UART you have selected in the configurator.  This UART might also be shared and/or labeled as the designated serial RX pin \(serial RX, SBUS, ppm\) it depends on your board. Keep in mind some boards have soft serial capability thereby allowing an uninverted serial connection to be made.  **NOTE:** softserial connections are limited to **19200** baud. This limits you to the msp protocol in Open.HD, which is msp v1. Users have had success with msp RC but beware.
2. Test. Power everything while the FC is connected to the iNav configurator and view the receiver tab

{% hint style="warning" %}
**NOTE:** Because most users will want telemetry as well as RC via Open.HD: **Serial RX and telemetry are not allowed to share the same UART in the iNAV configurator**. Connect the Air Pi RX pin \(telemetry\) to a different UART than the one you have assigned RC control \(serial RX\).
{% endhint %}

![A Picture speaks a thousand words](../.gitbook/assets/image%20%2825%29.png)

