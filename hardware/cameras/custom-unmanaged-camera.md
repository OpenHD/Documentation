# Custom Unmanaged Cameras

<!-- LEGACY DOCUMENTATION NOTICE -->
> ⚠️ **This documentation is outdated!** A current version is available at [openhdfpv.org](https://openhdfpv.org)
> 
> [📖 **View Updated Version of This Page** →](https://openhdfpv.org)

---


For advanced users, we have implemented "scripting support," which allows for custom camera pipelines, IP cameras, and general debugging.

This feature requires disabling auto-detection and needs manual activation in the `hardware.conf` configuration file.

The `custom_unmanaged_camera.sh` script can be found on the SD card in the `openhd/scripts` folder. You can edit this script. Just like in OpenHD 2.0, you can also use some of the old pipelines for testing purposes. However, please note that `omxenc` is not available in OpenHD Evo.

The `custom_unmanaged_camera.sh` can also manage Ethernet-Connections for IP-cameras.

Currently, there are several example pipelines available for:

| Camera                |
| --------------------- |
| OpenIPC cameras       |
| General IP cameras    |
| Seek Thermal cameras  |

> **Note 1**: The custom unmanaged camera service requires careful testing and doesn't provide automatic functionality right away. It is intended for advanced users and developers who understand its intricacies.

We encourage you to experiment with this feature, but please be aware that it's meant for users with a good understanding of camera pipelines and system integration.
