---
description: Open.HD for Dummies (for Marvin Lange)
---

# Getting Started

When a project reaches a certain stage, the number of options can be very overwhelming. This section of the documentation is intended to help guide newcomers towards their first functional Open.HD implementation.

{% hint style="warning" %}
If you have a pre-existing hardware requirement that is not met in this guide, it is still a good idea to follow the guide and make sure you have this, the simplest setup, working before venturing into more complex builds. Every setup, no matter how complex uses the elements in this guide as it's base.
{% endhint %}

## Sourcing hardware

Assuming you are starting with nothing, we recommend you get the following hardware:

* A Raspberry Pi4B for the Ground SBC
* A Raspberry Pi3A+ or Raspberry Pi Zero for the Air SBC
* A Raspberry Pi V1 or V2 camera with CSI connector \(Raspberry Pi Zero needs a different CSI cable\)
* Two WiFi cards that support the band you want to use. \(See [WiFi Adapters](../hardware/wifi-adapters.md)\)
* An HDMI cable for connecting the Ground SBC to a screen
* An HDMI capable screen \(you can use your TV for testing!\)
* Two High class SD Cards of 8Gb or more
* An SD card Adapter for your computer to flash the cards.
* A mobile device capable of running QOpen.HD and connecting to the Ground SBC \(_optional_\)
* Two BEC's for powering the Air and Ground SBC's. \(See [Guidelines](../hardware/wiring.md#general-tips-and-guidelines)\)
* Various lengths of connection wires.
* A soldering iron and required disposables.

## Step-by-step

Now that you have your prerequisite hard- and software, we can get down to business.

### Step 1: Powering the Ground SBC

This is where the BE**C's** come in. Much like the Air SBC, the Ground SBC will likely be **powered** by a **LiPo** battery. The Raspberry Pi and the WiFi cards all use **5V**, which is what most BEC's **produce**. So hook up one of your SBC's to a LiPo battery and use a **multimeter** to double-check the **output** is +5V.

{% hint style="info" %}
The Raspberry Pi and most WiFi adapters actually like the voltage to be slightly higher than +5V, along the lines of 5.2V ~ 5.4V. If you have a variable output, best set it to +5.3V. Do not go higher than +5.4V or you will damage your Raspberry Pi and/or WiFi cards!
{% endhint %}

When you have **verified** the output of the BEC, we can **connect** it to the Raspberry Pi, to do this, we have two **options**. **Soldering** or using the **GPIO Pin Header**, for the Ground SBC it's OK to use the GPIO Pin Header, for the Air unit we **recommend soldering**. Connect the output from the BEC to the PI on pins 2 and 6 \(or 4 and 6\) according to this **diagram**:

![Raspberry Pi GPIO header pins](../.gitbook/assets/image%20%2824%29.png)

This can be done **easily** by just plugging in the Servo **header** that comes with most BECs into the Raspberry Pi Pin Header. Make sure the RED **wire** is connecting to Pin 2 or 4 and the BLACK **wire** is connecting to PIN 6. Now when you **connect power** to the BEC, the Raspberry Pi will power up!

![Raspberry Pi Powered from Pin Header](../.gitbook/assets/image%20%281%29.png)

{% hint style="warning" %}
For all following steps, make sure to disconnect the power before attaching anything to the Raspberry Pi unless explicitly stated.
{% endhint %}

### Step 2: Connecting the WiFi Adapter

Now that we have **power** going to the Raspberry Pi it's time to **complicate** things. Attaching **WiFi** cards should be as **easy** as **plugging** them into the Pi's USB ports, unfortunately **it isn't**. Due to the way the Raspberry Pi is **designed** the USB ports do not receive **enough power** to drive the WiFi cards, especially when connecting **more** than one WiFi card as is often the case on a ground station.

So we need to make sure we provide **enough** power to the WiFi card while still **attaching** it to the Raspberry Pi's USB port. There are several ways to do this, including using a USB HUB and powering that from the BEC. Take a look at [Wiring](../hardware/wiring.md) for inspiration. For this step-by-step we will create a **modified** USB **cable**.

![The basic diagram we want to achieve for this step](../.gitbook/assets/image%20%284%29%20%281%29.png)

Using the diagram above **create** a USB cable with the D+ and D- **soldered** to the Raspberry Pi and the +5V and GND **soldered** to the **BEC**.

{% hint style="danger" %}
While it may seem tempting to solder the +5V and GND to the solder points on the Raspberry Pi, doing so is not OK! We will be feeding +5V into the circuit of the Pi where this is not intended, probably destroying the USB controller. Make sure the +5V wire of the USB cable is no longer connected on the Pi side. GND is OK connected or unconnected to the Pi.
{% endhint %}

### Step 3: Connecting a display

For this step-by-step we will just **connect** a display to the **HDMI** port, any TV or monitor with HDMI in will be useable. Bear in mind that bringing your 85" flatscreen TV to the field might be impractical. So for a more portable setup use a small HDMI capable monitor or use the 7" Raspberry Pi Touch Screen and create the ultimate GCS. \(See examples [here](https://discuss.openhdfpv.com/c/custom-tx-aio/9)\)

### Step 5: Preparing the SD card

Now that we have all the hardware connected to the Ground SBC it's time to put **Open.HD** on an **SD card** and boot it up! In order to put Open.HD on an SD card please follow these steps:

1. Go to the [release](https://github.com/OpenHD/Open.HD/releases) of Open.HD and download the latest release.
2. Extract the archive to a place on your computer where you can find it again.
3. You should now have a `.img` file.
4. Download and install [Balena Etch](https://github.com/balena-io/etcher/releases/)er for your OS.
5. Put the SD card in the SD card reader \(if you don't have one in your PC or laptop, get a USB to SD card adapter, they can be found for cheap, but investing in a slightly more expensive high speed adapter will greatly reduce the time spent staring at the progress bar of Balena Etcher\)
6. If your OS prompts you to format the card, ignore that.
7. Start Balena Etcher.
8. Select the `.img` file we downloaded and extracted earlier for the image file.
9. Select the SD card as the target \(Balena Etcher should only show the SD cards, but be careful, double-check that the indicated size matches the SD card\).
10. Hit _write_ and wat for the process to complete, depending on your SD card adapter this can take minutes to an hour.
11. When Balena Etcher finishes it will automatically dismount the SD card making it safe to unplug it from your computer.
12. Put the SD card in your Ground SBC.
13. Pro tip: Start the second SD card for the Air unit before continuing to the next step, Air and Ground use the same image. That way it will be done when we arrive at the Air unit steps.

### Step 4: Starting the Ground SBC for the first time

Now that we have everything connected to the Ground SBC, it's time to plug in the power.

{% hint style="danger" %}
When bench-testing you can use a bench power supply instead of a LiPo to prevent draining the LiPo, but make sure it can supply the required Amps \(minimum 3A\). When using a LiPo, connect a LiPo warning device to prevent over-discharging!
{% endhint %}

### Step 5: Connecting QOpen.HD to the Ground SBC

If everything went well, you should see the SBC **boot** up and eventually show the **QOpen.HD screen** on the connected HDMI **monitor**. If for some reason it does **not**, please go **back** and make sure you have followed all the steps **exactly** as described.

If you happen to be lucky and you are running on a **touchscreen** you can go ahead and **press** the Open.HD **logo** in the top left corner. You will see the menu system that allows you to **configure** all the settings. If you don't have a touchscreen, don't worry, you can attach a **mouse** and/or **keyboard** to the Ground SBC and use those as well!

**Optionally** you can connect a **mobile** device \(Phone or Tablet\) with the **QOpen.HD App** installed to the ground station. By default the Open.HD image will create a '**hotspot**' WiFi network to which you can connect with the device. The default network name will be `Open.HD` and the password will be `wifiopenhd`.

When **connected** to the **hotspot** start the QOpen.HD app on your **device**. If all went well you should see the **same** interface as on the HDMI **monitor**. Since we don't have an Air device yet it will show a **black** screen with the **HUD**, but you **should** see the Temperature and CPU load of the Ground SBC change as on the HDMI monitor.

TODO: Picture

### Step 6: Powering the Air SBC

Power for the Air SBC is much like powering the Ground SBC. So use the steps described there to make sure you hook up an BEC with enough Amps to the Air SBC. Please try to solder as much of the connections that you can, soldering will prevent many troubleshooting steps later on.

Since it is quite common to use a Raspberry Pi Zero for the Air SBC here are some schematics for hooking up power AND connecting the WiFi card to that SBC.

![Properly wired Raspberry Pi Zero](../.gitbook/assets/image%20%288%29.png)

As you can see both the USB Cable and the Pi are fed power from the BEC.

{% hint style="danger" %}
Please make sure the USB connector on the WiFi Adapter side is also secured, some people solder the USB connectors together, some people use glue, whatever you do, make sure it can **not wig**gle or **disconnect**. Even an tiny wiggle might **temporarily disconnect** the WiFi card resulting in a complete **loss of signal** from the Air SBC.
{% endhint %}

### Step 7: Connecting the WiFi Adapter to the Air SBC

This step is mostly covered in the diagram shown above. Let's reiterate that, however tempting it might be, do **NOT** use the **USB connectors** on the Pi to connect the WiFi Adapter with a **standard** cable, you might get lucky, but **soldering** is the **only** way to prevent **costly** lessons.

### Step 8: Connecting a camera

We will now **attach** the CSI **camera** to the Air SBC, this is a very **simple** procedure, but you need to make sure to connect the cable '**the right way around**' on both ends. First let's take a look at the ports on the Raspberry Pi's.

![The Raspberry Pi Zero CSI connector, notice the pins are on the side near the PCB](../.gitbook/assets/image%20%2818%29%20%281%29.png)

![The Raspberry Pi 3B CSI connector, notice the pins are facing away from the white locking tab](../.gitbook/assets/image%20%2814%29.png)

The pictures above should make it **clear** how to inspect the camera, but for good measure, here is the connector on the **camera** side:

![The Raspberry Pi V1.3 Camera board connector, notice the pins are on the side of the PCB \(white part\)](../.gitbook/assets/image%20%2812%29.png)

So now that we know where the pins are on the boards, let's inspect the CSI **cable** itself.

![The &apos;pins&apos; are exposed on one side of the CSI cable](../.gitbook/assets/image%20%2817%29.png)

![And the opposite side is clearly labelled \(blue here, can be different on other cables\)](../.gitbook/assets/image%20%2813%29.png)

So now it's a matter of **inserting** the cable into the **ports** with the **pins** of the cable **facing** the **pins** of the connector, **pull** up the locking tab and **insert** the cable:

![Pull up the locking tab and insert the cable with the pins facing the connector pins](../.gitbook/assets/image%20%2816%29.png)

Now using **equal** pressure on **both** sides gently **push** the locking tab all the way **down** while making sure the cable does not **slide** out:

![Use equal pressure to lock the tab](../.gitbook/assets/image%20%289%29.png)

Make sure the cable is **properly seated** before continuing.

![A properly seated CSI cable](../.gitbook/assets/image%20%2815%29.png)

Now do the **same** on the **Camera** connector. The procedure on the Raspberry Pi Zero is the **same**, the CSI connector is a bit **smaller** and in a different place, but it works the same. Be aware that you need a **different** CSI **cable** for the Raspberry Pi Zero due to the smaller **connector**.

{% hint style="warning" %}
The CSI camera is the **simplest** option to use and usually yields the best **performance**. The CSI cables however, are quite susceptible to **noise** and **interference**. If you see **horizontal lines** or odd **discoloration** in the image, **shield** the CSI cable by wrapping it in **tin foil** or other conductive material.
{% endhint %}

### Step 9: Preparing the SD card

Now if you've been **following** the steps to the **letter** you will already have an SD card from step 5. If **not**, please use the instructions from step 5 to create a second SD card for the Air SBC.

Good, now it's a **simple** matter of **inserting** the **SD card** into the Air Pi and your air unit is good to go!

### Step 10: Bask in the glory of your work

So now comes the moment of **truth**, apply power to the **Ground** SBC and subsequently apply power to the **Air** SBC. Allow both to **boot** completely, most CSI cameras have a small LED that lights up when the camera is **activated**, this is a good indication the boot went well and the system has started.

{% hint style="warning" %}
The Raspberry Pi Zero might take a **long** while to boot up, please allow a couple of **minutes** before despairing!
{% endhint %}

When all went **well**, and for the sake of this step-by-step we will assume so, you will be **greeted** by a nice crisp HD **video** streaming from your Air SBC to your Ground SBC, go ahead and **wave** at yourself to get a feel for the **latency**. Please notice that when using the HDMI out to a TV, the TV itself might introduce quite some latency.

Go ahead, **celebrate** your success, and please **let us know** if it worked for you! If for some reason the system does **not** work for you and you are sure you have **followed** all the **steps**, please **contact** us on [Telegram ](https://web.telegram.org/#/im?p=@OpenHD_HDFPV)or on the [Forums ](https://discuss.openhdfpv.com/c/help/6)to get help.

### Next steps

Logically most user will want to connect their Flight Controller to the system to actually see the OSD do it's thing. To do this, follow the steps outlined in [Wiring ](../hardware/wiring.md)-&gt; [Flight Controller](../hardware/wiring.md#flight-controller) and then make sure to use the correct settings in [Telemetry and OSD](../software-setup/telemetry-and-osd.md). After that, you can look into [RC Control](../rc-control/general.md) over Open.HD as well as the subjects in the Advanced Setup.

