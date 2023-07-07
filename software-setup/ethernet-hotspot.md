# Ethernet

Different to the working procedure of 2.0 in OpenHD evo there are two modes of operation:
1.Passive (recommended)
2.Active

#Passive
OpenHD has it's ethernet standardly activated as Client mode, this means you can connect it to a router or anything that provices a DHCP server and use it like that.

## Setup on Ubuntu

## Setup on Windows

#Active
This mode is made for IP cameras or connecting perifials to the ethernet Port which do not have a DHCP server.
The SBC will start it's on DHCP server and let's device connect to it.

{% hint style="warning" %}
This removes the ability to share internet with the SBC.
{% endhint %}
