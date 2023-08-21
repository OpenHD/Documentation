# Flight Controllers

OpenHD supports a range of flight controllers through MavLink integration, with a general recommendation of F405 or better controllers for optimal performance. The following flight controller software is currently supported:

| Software             | Bidirectional MavLink Support |
| --------------       | ---------------------------- |
| [INAV](../software-setup/inav.md)                 | Yes                          |
| [Ardupilot](../software-setup/ardupilot.md)            | Yes                          |
| [PX4](../software-setup/px4.md)                  | Yes                          |
| [Betaflight*](../software-setup/betaflight.md)          | No                           |

> **Warning:** Betaflight support is currently not enabled, and the development team is actively working on enabling it. It's important to be aware that Betaflight doesn't allow for bidirectional MavLink, meaning that settings cannot be changed via MavLink, and OpenHD-RC functionality is not available.


## Recommended Flight Controllers

For the best experience with OpenHD, flight controllers with an F405 or better chipset are recommended due to their processing power and compatibility with OpenHD features. These controllers are well-suited to provide a seamless integration between OpenHD and your aircraft.

| Flight controllers   | 
| --------------       |
| [Speedybee F405 Wing](https://www.speedybee.com/speedybee-f405-wing-app-fixed-wing-flight-controller/) |
| [SpeedyBee F405 Mini BLS 35A 20x20 Stack](https://www.speedybee.com/speedybee-f405-mini-bls-35a-20x20-stack/) |
| [Mateksys F405-WTE](http://www.mateksys.com/?portfolio=f405-wte) |
| [Mateksys H743-Wing](http://www.mateksys.com/?portfolio=h743-wing-v2) 

*this is not complete, just shows FC's that are commonly used.


## Choosing the Right Flight Controller

When selecting a flight controller, consider the specific requirements of your drone and the software you plan to use. 
In general Inav is recommended for beginners and Arduplane is more tailored to experienced users due to its complexity during setup.

## Ensuring Adequate UARTs

Make sure the chosen flight controller has enough UART ports for your setup. A common setup includes:

1. UART1 for the control link (ELRS, Frsky, etc.)
2. UART2 for GPS
3. UART3 for OpenHD

If you plan to incorporate additional components such as a gimbal, secondary GPS, or advanced sensors, you'll need more UART ports.

## INAV vs Arduplane Controllers

Not all flight controllers are compatible with Arduplane. Some use proprietary software like KISS, which is not supported. Generally, we recommend the following MCUs:

1. F405
2. F745
3. H743

If you don't intend to use Ardupilot, these MCUs are also suitable:

1. F411
2. F721
