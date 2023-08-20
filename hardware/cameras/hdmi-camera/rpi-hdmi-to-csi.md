# RPI HDMI to CSI Adapter: Unofficial Usage and Quirks

The RPI HDMI to CSI adapter provides a means of interfacing HDMI output from cameras to the Raspberry Pi platform. However, it's important to note that this adapter is not officially supported by the Raspberry Pi Foundation, and as a result, it presents certain challenges and limitations. Here's a concise rundown of these quirks:

1. **Encoder Bitrate Control**: One notable issue is the unreliable performance of the encoder bitrate control. This often results in fluctuations like overshoot and undershoot in the bit rate. To mitigate this problem, it is recommended to disable variable bitrate and instead manually set a conservative bitrate, such as 8 MBit/s for MCS3 encoding.

2. **Resolution and Framerate Configuration**: Configuring the resolution and framerate through the adapter can be problematic and may even fail in certain instances. To enhance the likelihood of successful configuration, it is advised to set the camera resolution to match exactly the resolution and framerate output by your HDMI source.

3. **Maximum Resolution and Framerate**: The Raspberry Pi hardware encoder is constrained to a maximum output of 1080p@30fps or 720p@60fps. Consequently, it's important not to select an HDMI output video signal from your camera that exceeds these limits.

4. **Reliable Adapter Detection**: For consistent and reliable detection of the HDMI to CSI adapter during boot, it is crucial to sequence the power supply. In practice, ensure that the OpenHD system is powered on after your HDMI camera. This ensures that the adapter receives a valid HDMI input signal prior to the initialization of the Air Pi system.

While the RPI HDMI to CSI adapter serves as a bridge between HDMI cameras and Raspberry Pi devices, its unofficial nature can lead to these operational quirks. Users seeking to employ this adapter should be aware of these limitations and implement the recommended workarounds for optimal results.
