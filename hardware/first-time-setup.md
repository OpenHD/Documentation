# First Time Setup

When a project reaches a certain stage, the amount of options to choose from can get pretty overwhelming. This section of the documentation is intended to help guide newcomers to the project towards their first functional OpenHD implementation.

{% hint style="info" %}
If you have a pre-existing hardware requirement that is not met in this guide, it is still a good idea to follow the guide and make sure you have this, the simplest setup, working before venturing into the more complex setups. Every setup, no matter how complex uses the elements in this guide at it's base.
{% endhint %}

## Sourcing hardware

Assuming you are starting with nothing, we recommend you get the following Hardware:

### Ground

* A regular Laptop with disabled SecureBoot
* A 8812AU, 8812BU, 8811AU or 8814AU  WiFi Card (See [WiFi Adapters](wifi-adapters.md))
* A fast USB stick, to write the OpenHD USB Image on


### Air cheap
{% hint style="warning" %}
Pi Zero 1 is not supported you need the version 2 !
{% endhint %}

* A Raspberry Pi Zero 2:
* High Quality BEC's, one for the Wifi-Adapter and one for the Raspberry. (See Wiring -> Power)
* A  ([supported Camera](../hardware/cameras/raspberry-cameras.md)) and the required cable (keep in mind, the Pi Zero uses a 22 Pin type B csi cable)
* A soldering iron and required disposables.
* Various lengths of connection wires.



### Air more sophisticated (better for advanced features/dual Camera)
* A Raspberry CM4 with EMMC with:
  * An [Ochin CM4 carrier](ochin.md) board
  * We recommend fitting a cooler to the CM4, because it really can get hot.
  * A 8812AU, 8812BU, 8811AU or 8814AU WiFi Card (See [WiFi Adapters](wifi-adapters.md))
* A  ([supported Camera](../hardware/cameras/raspberry-cameras.md)) and the required cable (keep in mind, the Ochin uses a 22 Pin type B csi cable)
* A soldering iron and required disposables for creating the connections to the Wifi-Card


## Step-by-step

Now that you have your prerequisite Hardware, we can get down to business.

### Step 1: Considerations about X86

When using X86 the genaral rule of thumb is "the more potent"/newer the device is, the lower the latency should be.
Keep in mind, that you have enough battery or an external charging device.
Its also recommended to use a device with a good screen (high brightness) to have a pleasent experience

### Step 2: Connecting the WiFi Adapter to the AIR

Since we use very powerfull WiFi-Cards and most SBC's have limited USB-Output-Power, we need a dedicated BEC for that Card's. In Addition to that it's mandatory to solder the wifi card to the SBC because on the Air-SBC vibrations and movement in general will result in connection problems, that's why we recommend to remove the USB-Connector or at least solder to the USB-Connector. If you need help with that look in our forums, there are some extensive guides how to do it nicely. Also writing in the Telegram or Discord Chat can help you.
Is recommended to visit the wiring section to see how to connect everything
([Wiring](../hardware/wiring.md))

### Step 4: Flashing the Ground SBC for the first time

Please refer to the ([Installation Guide](../installation-guide.md)) since its quite similar
{% hint style="warning" %}
The flasing process can be much longer than on RPI
{% endhint %}

### Step 5: Booting your Ground

Please make sure SecureBoot is disabled and set up your BIOS(UEFI) to boot from USB.
Everything else is beeing taken care of. If QOpenHD doesn't start automatically, please execute OpenHD and QOpenHD which are linked to your Desktop.

(The boot can take several minutes, depending on your usb-sticks speed)

### Step 6: Flashing the Ochin SBC for the first time

If you're not using the Ochin board,you can jump to the next step. If you're using the Ochin, you first need to install your CM4 into the Ochin board and flash it. The Ochin board requires external power even when the usb-c is connected. To enter the "flash-mode" push the Button while connecting power. Now you can continue with the normal setup shown in this Video. And when it comes to flashing jump to the next Step

{% embed url="https://www.youtube.com/watch?v=jp_mF1RknU4&t=70s" %}

  Keep in mind, flashing is very slow, because some limitations of the RPi-Foundation. Do not disconnect while flashing, it can brick your device.

### Step 6.5: Flashing the Air SBC

Please refer to the ([Installation Guide](../installation-guide.md)) 

### Step 7: Starting the Air SBC

The first boot will take several Minutes, because initial configs and setups are executed. The SBC will reboot multiple times. OpenHD will automatically start to transmit Video, if everything is correct.
If you haven't configured your camera correctly you'll see a black image that says "rebooting camera", in this case look into the "Air CAM 1" Menu in QOpenHD (the OpenHD Logo opens the Menu) and select the correct camera overlay in the V_OS_CAM_CONFIG menu. After this your SBC will reboot and start transmitting video.

{% hint style="info" %}
If you have any issues now, please don't hesitate and write in our Chats, so we can help you get everything working correctly.
{% endhint %}
