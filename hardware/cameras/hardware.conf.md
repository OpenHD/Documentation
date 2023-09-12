# OpenHD Hardware Configuration (hardware.conf)

The **hardware.conf** file in OpenHD allows advanced users and developers to override default configurations and camera setups when the normal setup via the graphical user interface (GUI) isn't sufficient. It contains critical settings for managing Wi-Fi, cameras, network interfaces, and some generic options. Here are the important sections and parameters you need to understand:

## Wi-Fi Configuration

### [wifi] Section

#### WIFI_ENABLE_AUTODETECT
- **Description**: Determines whether OpenHD should automatically detect and configure Wi-Fi cards.
- **Value**: `true` (Automatic detection enabled) or `false` (Manual configuration).
- **Note**: When set to `false`, manual configuration is required.

#### WIFI_WB_LINK_CARDS
- **Description**: Specifies the interface name(s) of the cards used for Wi-Fi broadcast.
- **Value**: If `WIFI_ENABLE_AUTODETECT` is `false`, specify the interface name(s).
- **Note**: For the ground station, multiple cards can be specified, but only one card is used for transmission from ground to air.

#### WIFI_WIFI_HOTSPOT_CARD
- **Description**: Defines the interface name of the card used for the Wi-Fi hotspot.
- **Value**: Empty or specify the interface name.
- **Note**: Ensure it does not conflict with cards used for wifibroadcast.

## Camera Configuration

### [camera] Section

#### CAMERA_ENABLE_AUTODETECT
- **Description**: Determines whether OpenHD should automatically detect and configure cameras.
- **Value**: `true` (Automatic detection enabled) or `false` (Manual configuration).
- **Note**: When set to `false`, manual configuration is required.

#### CAMERA_N_CAMERAS
- **Description**: Specifies the number of cameras in use.
- **Value**: `1` (Primary camera only) or `2` (Primary and secondary cameras).

#### CAMERA_CAMERA0_TYPE and CAMERA_CAMERA1_TYPE
- **Description**: Defines the types of cameras to use when auto-detection is disabled.
- **Value**: Choose from available camera types such as `DUMMY_SW` for emulated software cameras or other camera-specific options.
- **Note**: The specific camera types are explained in the comments within the configuration file. For unmanaged Cameras the unmanagedCamera script needs to be edited, too
## Network Configuration

### [network] Section

#### NW_ETHERNET_CARD
- **Description**: Configures how OpenHD manages the Ethernet connection.
- **Value**: `RPI_ETHERNET_ONLY` (default) or specify the interface name of your Ethernet card.
- **Note**: Useful primarily on Raspberry Pi as a ground station.

#### NW_MANUAL_FORWARDING_IPS
- **Description**: Specifies additional IP addresses to which OpenHD should forward video and telemetry data.
- **Value**: Comma-separated list of IP addresses.
- **Note**: Useful for manual network configuration.

#### NW_FORWARD_TO_LOCALHOST_58XX
- **Description**: Controls whether OpenHD forwards video streams to localhost on ports 5800 and 5801.
- **Value**: `true` or `false`.
- **Note**: These streams are primarily used by the OpenHD web UI for FPV preview.

## Generic Configuration

### [generic] Section

#### GEN_ENABLE_LAST_KNOWN_POSITION
- **Description**: Enables or disables writing the last known position (latitude and longitude) to a file for recovery purposes in case of a crash on the ground.
- **Value**: `true` or `false`.
- **Note**: Useful for ground unit recovery.

---

**Note**: Editing the **hardware.conf** file can have a significant impact on OpenHD's behavior and should be done with caution. Changes to this file may require a restart of OpenHD and can be overwritten during OpenHD updates. This file is typically located at `/boot/openhd/hardware.conf` on OpenHD images.
