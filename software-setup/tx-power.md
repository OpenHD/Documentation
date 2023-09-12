# TX Power Configuration in OpenHD Evo

**NOTE**: When adjusting the TX (transmit) power settings, it is your responsibility to adhere to the rules and regulations of your country.

OpenHD Evo provides the ability to configure the TX power of Wi-Fi cards that support runtime power adjustments. Additionally, RTL8812AU and RTL8812BU users can specify different TX power levels when the Flight Controller (FC) is armed or disarmed.

## Wi-Fi Cards

OpenHD Evo offers robust support for RTL8812AU and RTL8812BU Wi-Fi cards, allowing you to modify the "TX power index," a unitless value specifying the output power of the Wi-Fi chip before amplification Several important considerations apply:

1. The actual TX power in milliwatts (mW) depends on the specific card you have, including any amplifiers it uses.

2. TX power indices are unitless values ranging from 0 to 63, with 63 representing the highest achievable output power for.

3. **Caution**: Selecting a TX power index that is too high and thereby feeding excessive power into the amplifiers on your card can result in damage. It is advisable to consult your card seller's website for specific guidance before adjusting the TX power. For ASUS card users, a range of 0 to 63 can generally be used safely.

4. High TX power settings require appropriate power supply and cooling. Refer to hardware recommendations for guidelines on powering your Wi-Fi cards.

5. TX power settings are local to your Air and Ground units. Adjust the air TX power under "OpenHD -> AIR" and the ground TX power under "OpenHD -> GND."

6. Excessive TX power indices at certain bitrates (MCS) can lead to overamplification and increased packet loss. Avoid using TX power indices of 53 or higher when flying with MCS 4 or higher. In general, TX power indices of <= 53 are recommended.

7. Default TX power settings: OpenHD Evo defaults to a TX power of <= 25mW (or a TX power index measured to commonly output <= 25mW) to comply with regulations. You may need to adjust the TX power settings manually after flashing OpenHD Evo to meet your specific requirements.

### Armed/Disarmed TX Power Feature

You can configure different TX power levels for the armed and disarmed states. To do this:

- Set `TX_POWER_I` to LOW(25mW).
- Adjust `TX_POWER_I_ARMED` as needed. This helps prevent overheating during bench testing when there might not be adequate cooling.

### ASUS (Measured) Power Table
Please note that the following power values apply only to ASUS AC56-USB Wi-Fi cards and may not be applicable to other cards:

- TX Power Index 19: 10-12 mW
- TX Power Index 25: 25-30 mW
- TX Power Index 30: 45-50 mW
- TX Power Index 35: 70-80 mW
- TX Power Index 37: 100-110 mW
- TX Power Index 40: 120-140 mW
- TX Power Index 45: 200-230 mW
- TX Power Index 50: 280-320 mW
- TX Power Index 55: 380-400 mW
- TX Power Index 58: 420-450 mW

### Custom Aliexpress Cards

Please note that the AC180 Cards from aliexpress behave very strange/different:

- TX Power Index 20: low(ish power)
- TX Power Index 22: medium(ish power)
- TX Power Index 26: high power
- TX Power Index 30: maximum(dangerous power)

**NOTE**: It is not possible to use these cards legally in most of the countries, so be cautious

## Other Wi-Fi Cards

Please be aware that while RTL8812AU/RTL8812BU cards are fully supported in OpenHD Evo with detailed power tables and guidance, other cards may function differently. It is advisable to exercise caution and perform testing when using non-RTL8812AU/RTL8812BU cards to ensure they operate as expected.
