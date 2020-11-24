# Ground Recording

Open.HD automatically stores video and telemetry in a temporary storage while it is being received from the Air SBC. 

To **save** video, telemetry and screenshots to a USB memory stick, simply **plug** the USB drive into the Ground SBC **AFTER** you are done flying. After a few **seconds**, a **message** should appear and the recorded video will start **playing** on the HDMI screen while being **saved** to USB. A message will appear when it is **done** saving.

These are the relevant settings:

{% tabs %}
{% tab title="VIDEO\_TMP" %}
| Value | Description |
| :--- | :--- |
| memory | Save the recording to RAM disk. Limited to around 12 minutes of video and data. |
| sdcard | Save the recording to a separate partition on the SD Card. |
{% endtab %}

{% tab title="ENABLE\_SCREENSHOTS" %}
| Value | Description |
| :--- | :--- |
|  |  |
{% endtab %}
{% endtabs %}

{% hint style="info" %}
When using the `sdcard` option you still plug in a USB drive after flying to encode and copy the video to the USB drive. It is possible to remove the SD Card and get the video file directly from the `myvideo` partition \(`/dev/mmcblk03`\). The video will be in `.raw` format. This can be played by VLC. Using the USB drive will wrap the video in a AVI container.
{% endhint %}

{% hint style="warning" %}
Due to issues with the Linux kernel, using the `sdcard` setting may lead to video stuttering bad blocks or video freezing. Use a fast SD Card to mitigate this and test thoroughly before flying!
{% endhint %}

