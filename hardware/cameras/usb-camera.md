# Cameras

<!-- LEGACY DOCUMENTATION NOTICE -->
> ⚠️ **This documentation is outdated!** A current version is available at [openhdfpv.org](https://openhdfpv.org)
> 
> [📖 **View Updated Version of This Page** →](https://openhdfpv.org)

---


## Overview

OpenHD has the ability to automatically detect and utilize USB cameras that provide either raw uncompressed or pre-encoded (h264, h265, mjpeg) data streams. However, it's important to note the following potential limitations:

1. **Fixed Encode Bitrate:** Cameras with a fixed encode bitrate may not support features like variable bitrate. This could necessitate manual tuning of your connection settings.

2. **Suboptimal Encoding Parameters:** Some cameras might have encoding parameters that lead to issues such as increased latency or poor error recovery in your stream. Thoughtful adjustment of these parameters is recommended for optimal streaming performance.

3. **RAW Format Challenges:** Cameras that deliver RAW data require software-based encoding, which can impose constraints on achievable resolutions and frame rates. This limitation persists even on powerful platforms like the Raspberry Pi 4.

By being mindful of these potential challenges, users can make informed decisions about camera selection and configuration to ensure the best possible streaming experience with OpenHD.
