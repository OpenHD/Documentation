# Ethernet

Different to the working procedure of 2.0 in OpenHD evo there are two modes of operation:
1.Client mode
2.Host mode

#Client mode
OpenHD has it's ethernet standartly activated as Client mode, this means you can connect it to a router or anything that provices a DHCP server and use it like that.

#Host mode
This mode is made for IP cameras or connecting perifials to the ethernet Port which do not have a DHCP server.
The Pi will start it's on DHCP server and let's device connect to it

{% hint style="warning" %}
Warning
{% endhint %}
