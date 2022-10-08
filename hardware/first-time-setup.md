# First time Setup

When a project reaches a certain stage, the amount of options to choose from can get pretty overwhelming. This section of the documentation is intended to help guide newcomers to the project towards their first functional Open.HD implementation. 

{% hint style="info" %}
If you have a pre-existing hardware requirement that is not met in this guide, it is still a good idea to follow the guide and make sure you have this, the simplest setup, working before venturing into the more complex setups. Every setup, no matter how complex uses the elements in this guide at it's base.
{% endhint %}

## Sourcing hardware

{% hint style="info" %}
In today's Chip Shortage sourcing hardware can be stressful, but there are a few hints to get your Raspberry devices even when they're quite hard to get.
In Europe \([Berrybase](https://www.berrybase.de/)\) alwasy have some devices in stock for it's club members (membership is free).
In addition to that \([RpiLocator](https://rpilocator.com/)\) can help you get raspberry hardware worldwide.
{% endhint %}

Assuming you are starting with nothing, we recommend you get the following Hardware:


* A Raspberry Pi4B for the Ground SBC
* A 
* Two WiFi cards that support the band you want to use. \(See [WiFi Adapters](../hardware/wifi-adapters.md)\)
* An HDMI cable for connecting the Ground SBC to a screen
* An HDMI capable screen \(use your TV for testing!\)
* A mobile device capable of running QOpenHD and connecting to the Ground SBC
* Four BEC's for powering the Air and Ground SBC's, and the Wifi-Adapters independently. \(See Wiring -&gt; Power\)
* Various lengths of connection wires.
* A soldering iron and required disposables.

## Step-by-step

Now that you have your prerequisite hard- and software, we can get down to business.

### Step 1: Powering the Ground SBC

The ground SBC needs enough "juice" to be able to decode, display and control the OpenHD-Link.
That's why we recommend the more "performant" device to be used on the Ground.
We recommend 3A for a Raspberry Pi and 5A for a Nvidia Jetson.


### Step 2: Connecting the WiFi Adapter

Since we use pretty powerfull WiFi-Cards and most SBC's have limited USB-Output-Power, we need a dedicated BEC for the Card.
In Addition to that it's common practice to notconnect the Wifi-Card directly to the SBC. On the Air-SBC Vibrations and movement in general will result in connection problems, that's why we recommend to remove the USB-Connector or at least solder to the USB-Connector.
If you need help with that look in our forums, there are some extensive guides how to do it nicely. Also writing in the Telegram or Discord Chat can help you.

### Step 3: Connecting a display

Just connect an HDMI-Display, most Displays should just work out of the box.

### Step 4: Starting the Ground SBC for the first time

Check wiring and plug in the SBC, keep in mind that the WiFi-card needs to be connected before you plug in the SBC, if not OpenHD will stop and fail.

### Step 5: Starting the Air SBC

Check wiring and plug in the SBC, keep in mind that the WiFi-card and Camera needs to be connected before you plug in the SBC, if not OpenHD will stop and fail.

