# Features

The following improvements have been made to the provided wiki page:

## Supported Devices:

* [Raspberry](../hardware/raspberry.md)
* [Radxa Rock 5](../hardware/radxa.md)
* [X86 Devices](../hardware/X86.md)

## List of Features in the Latest Evo Release

The latest [Evo release](https://github.com/OpenHD/OpenHD/releases) of OpenHD incorporates a range of advanced features and capabilities:

### Enhanced Channel Support
* OpenHD now supports all 2.4GHz and 5.8GHz channels, providing users with versatile frequency options.

### Stable Video Reception
* OpenHD ensures remarkably stable video reception even in challenging multipath environments. This stability eliminates the constant glitching commonly experienced with analog FPV systems.

### Dual Camera Support
* The platform offers dual camera support for a variety of [camera types](../hardware/cameras.md), including libcamera, veye, raspivid, USB, thermal, and unmanaged cameras.

### Custom Camera Integration
* OpenHD is developing[custom cameras](https://www.arducam.com/openhd/) together with arducam, specifically designed for the platform, expanding hardware choices for our users.

### Two-Way Settings
* Experience real two-way communication settings, enhancing control and customization options.

### Integrated High-Resolution OSD
* The OSD (On-Screen Display) features high-resolution visuals and is fully customizable. It also seamlessly integrates with MAVLink telemetry data.

### Real-Time Telemetry Display
* Users can monitor real-time data such as Received Signal Strength Indicator (RSSI), packet loss, video bitrate, and other critical information directly on the OSD.

### Dynamic Adjustability
* OpenHD enables real-time adjustments of various parameters, including TX power, modulation, video settings, camera configurations, and more.

### Picture-in-Picture Functionality
* Enjoy the benefits of an adjustable Picture-in-Picture feature for secondary video signals, enhancing situational awareness.

### Reliable Video Link
* OpenHD employs a unique wifibroadcast link with highly optimized FEC, that overcomes issues commonly associated with standard Wi-Fi connections, such as high latency, disconnections and video freezing. The system ensures rapid video recovery.

### Secure Link
* OpenHD provides mechanism's to ensure the security of your UAV, including verification and customizable encryption. Always providing a secure link which can not simply be overtaken by external signals. 

### MAVLink Telemetry Support
* Bidirectional MAVLink telemetry support is integrated, offering compatibility with a wide range of flight controllers, with remarkable stability.

### Multi-Device Data Forwarding
* Users can forward video streams and telemetry data to secondary devices using multiple methods, enhancing data accessibility and allowing for custom setups like FPV over the Internet.

### Seamless QGroundControl Compatibility
* FC (Flight Controller) settings, video parameters, and telemetry configurations seamlessly integrate with QGroundControl without requiring any modifications. For better integration with existing Groundstations.

### Multi Platform Compatibility
* OpenHD is programmed to work on various platforms, like the raspberry pi or X86 devices. On X86 we provide Images with preinstalled and tuned versions of QOpenHD,OpenHD,Inav,MissionPlanner,QGroundcontrol,...

### OSD Clarity in Challenging Situations
* The OSD overlay displayed on the receiver remains clear and functional even when video quality is compromised, ensuring essential flight information is still accessible.

### Streamlined Configuration
* Configuration tasks are simplified through the use of QOpenHD and the [OpenHD-ImageWriter](../downloads.md), eliminating the need for complex configuration files.

### Efficient Flashing Process
* OpenHD flashing is recommended to be performed using the [OpenHD-ImageWriter](../downloads.md) tool, streamlining the flashing procedure.

### Low-Latency RC Control
* Experience low-latency and high-update-rate remote control over the Wi-Fi broadcast link via USB joystick compatibility.

### Optimized FEC
* OpenHD employs an optimized Forward Error Correction (FEC) mechanism to ensure the most stable and reliable video transmission connections.

### Dedicated Development Team, Beta Testers, and Vibrant Community

* OpenHD benefits from a dedicated and specialized development team that continually strives to enhance the platform. Regular and frequent updates, along with feature improvements, are diligently implemented and tested by this skilled group.
* Our will to always innovate, our supporters via [OpenCollective](https://opencollective.com/openhd) and [partners](https://openhdfpv.org/partners/), allow us to test, integrate, manufacture new and exiting hardware. In addition part of our team is working on [custom hardware](https://www.patreon.com/OpenHD), which allows us furter optimize and minimize hardware for OpenHD.
* The OpenHD Community is a thriving and dynamic hub of support and knowledge. In the event of any challenges or issues, the community is always ready and willing to offer assistance and guidance.

These features are just a collection of most notable features, which enhance the capabilities of OpenHD, making it a powerful and versatile choice for remote video transmission and telemetry in various applications.
