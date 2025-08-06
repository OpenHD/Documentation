# Ethernet Modes in OpenHD Evo

<!-- LEGACY DOCUMENTATION NOTICE -->
> ⚠️ **This documentation is outdated!** A current version is available at [openhdfpv.org](https://openhdfpv.org)
> 
> [📖 **View Updated Version of This Page** →](https://openhdfpv.org)

---


In OpenHD Evo, there are two modes of Ethernet operation:

1. Passive (Recommended)
2. Active

## Passive Mode

In Passive mode, OpenHD's Ethernet is configured as a client, allowing you to connect it to a router or any device providing a DHCP server for seamless network integration.

### Setup on Ubuntu

1. Connect an Ethernet cable from your Linux device to the Single Board Computer (SBC).
2. Wait briefly.
3. Open a terminal and enter the command: `sudo arp-scan --interface=eth0 --localnet` (**Replace ETH0 with the correct adapter connected to the SBC**).
4. Test the connection by entering the SBC's IP address into your web browser; it should redirect you to the OpenHD web interface.
### Tethering

1. **Record IP Addresses:**  
   Once connected, note the IP addresses of both devices:
   - **SBC IP**: For example, `10.42.0.118`
   - **Laptop IP**: For example, `10.42.0.1`
   
2. **Configure Forwarding in OpenHD:**  
   SSH into the RPI (user and password is `openhd`).Open the `hardware.conf` file located in `/boot/openhd/` on your SBC. Modify the `NW_MANUAL_FORWARDING_IPS` IP address to point to your laptop’s IP:

   ```bash
   # Specify additional IP address(es) for video and telemetry forwarding.
   # OpenHD can detect external devices based on the connection and platform.
   # Only applicable on ground units.

   NW_MANUAL_FORWARDING_IPS = 10.42.0.1  # Replace with your Ground Station IP (laptop)
   ```

This setup will ensure that video and telemetry data are directed to your laptop's IP, enhancing your tethered OpenHD experience.

### Setup on Windows

1. Connect an Ethernet cable from your Windows device to the SBC.
2. Search for "View network connections."
3. Access the settings of the network connection providing your Windows device with internet access.
4. Click on "Properties" and "Share."
5. Select your Ethernet connection with the SBC.
6. Wait briefly.
7. Use a software tool to scan for devices on your system (recommendation: Angry IP Scanner) to locate active devices.
8. Test the connection by entering the SBC's IP address into your web browser; it should redirect you to the OpenHD web interface.
9. (Sometimes not needed) Edit the hardware.conf on your SBC and add the Windows IP address to the forwarding IP addresses (usually 192.168.137.1).

### Setup on Android

#### USB Tethering

{% hint style="warning" %}
This mode charges your mobile phone from the SBC; please note that Raspberry Pi devices may sometimes fail to boot when a phone is connected.
{% endhint %}

1. Connect a suitable cable to your SBC; ensure it's a data-capable USB cable.
2. Go to your network settings, enable hotspot, and then enable USB Tethering.
3. All further configurations are done on the SBC.
4. For the best experience, use the official QOpenHD Evo app, available on the Play Store.

{% hint style="information" %}
Some carriers and manufacturers may hide the tethering setting. If it's not visible due to the absence of a SIM card or other reasons, you may need to use a third-party app to enable it (recommended app will be provided later).
{% endhint %}

#### Ethernet Tethering

1. Connect a suitable Ethernet adapter to your Android device.
2. Go to your network settings, enable hotspot, and then enable Ethernet Tethering.
3. All further configurations are done on the SBC.
4. For the best experience, use the official QOpenHD Evo app, available on the Play Store.

{% hint style="information" %}
Some carriers and manufacturers may hide the tethering setting. If it's not visible due to the absence of a SIM card or other reasons, you may need to use a third-party app to enable it (recommended app will be provided later).
{% endhint %}

## Active Mode

Active mode is designed for IP cameras or connecting peripherals to the Ethernet port that do not have a DHCP server. In this mode, the SBC runs its own DHCP server, allowing devices to connect directly.

{% hint style="warning" %}
Active mode does not support sharing internet with the SBC.
{% endhint %}
