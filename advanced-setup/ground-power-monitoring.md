# Ground Power Monitoring

{% hint style="danger" %}
This section is under construction and has to be verified, use at your own risk.
{% endhint %}

To ensure you don't have surprise shutdowns on your Ground unit, it can be very convenient to monitor the Voltage and Current that are supplied to the system. There are several available options for this, using any one of those options will populate the required MAVLink messages that are shown in the OSD and on the Power page in QOpen.HD.

![The power screen in QOpen.HD, notice the Ground section](../.gitbook/assets/image%20%2810%29.png)

## INA219 - Simple and efficient

Using the INA219 modules, readily available from sources like [AliExpress ](https://www.aliexpress.com/item/4000223447065.html)is a simple and efficient way to add Ground Power monitoring. The module is easy to attach to the Ground unit using I2C. The following pictures and diagrams should be all you need. If the system finds the device attached it will automatically enable the functionality.

![Wiring schematic for the INA219](../.gitbook/assets/image%20%282%29.png)

![Overview of the INA219 board](../.gitbook/assets/image%20%2811%29.png)

![Real-life install in a Ground unit.](../.gitbook/assets/image.png)

## LiFePO4wered/Pi

This is a popular device that attaches directly to the GPIO pins of the Raspberry Pi. See the [website](https://lifepo4wered.com/lifepo4wered-pi.html) for more background information and installation procedures. If the system finds the device attached it will automatically enable the functionality. There is no need to follow the instructions regarding the installation of the software as this is already included in Open.HD.

![The LiFePO4wered/Pi device attached to a Raspberry Pi](../.gitbook/assets/image%20%2822%29.png)



