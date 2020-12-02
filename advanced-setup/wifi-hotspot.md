# WiFi Hotspot

To make it easy to connect a Phone or Tablet to your Ground SBC in order to view the video or change settings or even run your Ground Control software the system allows for a WiFi Hotspot by default.

You can change the way the Hotspot behaves by changing the `WIFI_HOTSPOT` parameter. It takes the following values:

| Value | Description |
| :--- | :--- |
| auto | Automatically selects a WiFi Band and channel that allows for the least amount of interference with the 'main' WiFi reception of the Air SBC |
| y | Uses the [custom ](wifi-hotspot.md#custom-band-and-channel-settings)Band and Channel settings for manual control |
| n | Disables the WiFi Hotspot functionality altogether |

### Default SSID an Password

The default SSID is `Open.HD` and the default password is `wifiopenhd`. Both values can be changed by editing the `apconfig.txt` file in the `BOOT` partition of the SD card. No settings for this have been exposed yet in the app.

### Custom Band and channel settings

When selecting the `y` option you can set the Band and Channel on which the system starts the WiFi Hotspot. 

{% tabs %}
{% tab title="HOTSPOT\_BAND" %}
| Value | Description |
| :--- | :--- |
| a | Use the 5,8Ghz WiFi band |
| g | Use the 2,4Ghz WiFi band |
{% endtab %}

{% tab title="HOTSPOT\_CHANNEL" %}
| Value | Description |
| :--- | :--- |
| 1 to 11 | Available channels for the 2,5 GHz g band |
| 36,40,44,48,52,56,60,64 | Available channels for the 5,8 GHz a band |
{% endtab %}
{% endtabs %}

### Custom Hotspot WiFi power

By reducing the power of the WiFi hotspot, you reduce the range, e.g. how far away from the Ground SBC you can be while still being connected to the WiFi, but you also reduce the interference impact on the main WiFi reception from the Air SBC.

{% tabs %}
{% tab title="HOTSPOT\_TXPOWER" %}
<table>
  <thead>
    <tr>
      <th style="text-align:left">Value</th>
      <th style="text-align:left">Description</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="text-align:left">100 to 3100</td>
      <td style="text-align:left">
        <p>The transmit power in units of mBm (100 mBm is equal to 1 dBm).</p>
        <p><em>3100</em> is the maximum available power for the internal WiFi.</p>
      </td>
    </tr>
  </tbody>
</table>
{% endtab %}
{% endtabs %}

### Automatic WiFi Hotspot shutdown

If you only use the hotspot for the initial setup it might be helpful if it shuts down after an initial period of time. Allowing yourself time to do any setup and then forgetting about it.

{% tabs %}
{% tab title="HOTSPOT\_TIMEOUT" %}
| Value | Description |
| :--- | :--- |
| 0 | Run the WiFi Hotspot for ever |
| 1 to 3600 | The amount of seconds to have the WiFi hotspot active after boot |
{% endtab %}
{% endtabs %}

