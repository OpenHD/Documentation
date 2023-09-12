# Dynamic MCS Index Adjustment with RC Switch

In OpenHD, you have the flexibility to dynamically change your MCS (Modulation and Coding Scheme) index, which directly affects your video bitrate and maximum range, during your flight. By increasing the MCS index, you can boost your available bitrate at the cost of reduced range, and vice versa. This feature is particularly useful for optimizing your FPV experience based on your current needs and conditions.

## Prerequisites

To change the MCS index during flight in OpenHD Evo, ensure the following prerequisites are met:

1. You are using the rtl8812au wireless adapter.
2. Your camera supports variable bitrate, as OpenHD can adjust your camera's encoder bitrate.
3. Your Flight Controller (FC) reports your RC (Radio Control) channels to OpenHD, which is commonly supported by ArduPilot-based setups.

## Method 1: QOpenHD and Touch Screen

You can adjust the MCS index during your flight using the QOpenHD interface on a touch screen. However, when using directional antennas, it may not be practical to make parameter changes on your Air unit when it is far from you or at maximum range.

## Method 2: RC Channel Switch

To address the limitations of Method 1, OpenHD allows you to configure your RC so that you can change the MCS index via a specific channel from your RC transmitter. This enables you to make real-time adjustments even when your aircraft is at the edge of its range or under challenging conditions.

### Configuration Steps

Follow these steps to set up the MCS index adjustment via your RC channel switch:

1. Ensure you have a free channel available on your RC transmitter that can be transmitted over your RC link. This setup works with both RC connections over OpenHD and other RC links like ExpressLRS, Crossfire, etc. The use of alternative RC links is recommended for long-range flights. For this example, we'll use Channel 7.

2. Verify that your RC channels are forwarded from the Flight Controller (FC) to the OpenHD Air unit. You can check this by going to QOpenHD, navigating to RC -> FC CHANNELS DEBUG, and confirming that moving channel 7 corresponds to channel 7 movements.

3. In the OpenHD interface on your Air unit, go to **OpenHD -> AIR** and change the setting **MCS_VIA_RC** from "DISABLED" to your selected channel (in this case, Channel 7).

### PWM Value Mapping

Now that you've completed the setup in OpenHD, you need to transmit the correct PWM (Pulse Width Modulation) values depending on your RC switch configuration. Here's the mapping in OpenHD:

- [900 ... 1200]: MCS0
- [1200 ... 1400]: MCS1
- [1400 ... 1600]: MCS2
- [1600 ... 1800]: MCS3
- [1800 ... 2100]: MCS4

For users with a 2-position switch, it is recommended to configure the switch on your RC as follows:
- Low Position: MCS1 (Approximately 1300 PWM)
- High Position: MCS3 (Approximately 1700 PWM)

If you are using a 3-position switch, consider the following configuration:
- Low Position: MCS1 (Approximately 1300 PWM)
- Medium Position: MCS2 (Approximately 1500 PWM)
- High Position: MCS3 (Approximately 1700 PWM)

MCS 3 typically strikes a balance between range and image quality, making it a good choice for general use. MCS 1 can serve as a backup with significantly reduced image quality but greater range. Of course, you can configure different PWM values to suit your preferences and requirements.
