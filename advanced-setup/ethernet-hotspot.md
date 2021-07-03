# Ethernet Hotspot

In some cases you want to use the Ethernet port of the Ground SBC to connect to a laptop for instance. In this case you can enable the Ethernet Hotspot.

{% tabs %}
{% tab title="ETHERNET\_HOTSPOT" %}
| Value | Description |
| :--- | :--- |
| Y | Enable the Ethernet hotspot |
| N | Disable the Ethernet hotspot |
{% endtab %}
{% endtabs %}

{% hint style="info" %}
Don't use a switch or Hub, directly connect the RJ-45 cable. The Pi will be IP `192.168.1.1` the connected PC will be `192.168.1.2`. Using a Switch or Hub won't work since the current implementation only supports one connected device.
{% endhint %}

{% hint style="warning" %}
When the Ethernet hotspot is on, the WiFi hotspot doesn't work.
{% endhint %}

{% hint style="warning" %}
If you are trying to ssh into the groundpi, turn OFF the Ethernet hotspot setting. If ethernet is connected to a router then get the pi IP address from the router.
{% endhint %}

