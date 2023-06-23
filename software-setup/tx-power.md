NOTE: When setting the TX power, it is your own responsibility to follow your countries rules !

OpenHD evo lets you change the tx power of wifi cards that support changing the tx power ar run time.
Furthermore, rtl8812au users can specify different TX power levels when the FC is armed / disarmed.

RTL8812AU
On RTL8812AU, you can change the so-called "TX power index" - a unitless value that specifies the output
power of the wifi chip (before amplification). There are a couple of things to note though:
1) The actual TX power in mW depends on what card using rtl8812au you bought - e.g. if and which amplifiers the cards uses
2) The TX power are unitless values in the range [0..63] where 63 is the highest output power rtl8812au can do
3) TOO HIGH TX POWER VALUES CAN DESTROY YOUR ALIEXPRESS CARDS !
  - If you select a tx power index too high and therefore feed too much power into the amplifiers on your card, your card WILL be damaged.
    Please look at the website of your seller if you bought a special (aliexpress) card before changing the tx power. 
    For ASUS card users, [0..63] can be safely used
4) High TX power requires adequate power supply and cooling - follow the recommendations in hardware on how to power your wifi cards.  
5) Your TX power set is local to your air / ground unit - change the air tx power under OpenHD / AIR and the ground tx power under OpenHD / GND
6) High packet loss - too high power indices at given bitrate (MCS) can result in overamplification and increased packet loss. Make sure to
   not use 53 or higher on ASUS when flying with MCS 4 or higher (in general, <=MCS 3 is used, though)
7) Default TX power: OpenHD defaults to <=25mW (or rather, a tx power index that is measured to commonly output <=25mW) to comply with all countrie(s) regulations. 
  You need to change the tx power after flashing yourself !

Using the armed / disarmed TX power feature:
On rtl8812au, you can specify different TX power levels for armed / disarmed state. To do so, leave TX_POWER_I on LOW(25mW) and change TX_POWER_I_ARMED accordingly.
This avoids overheating on the bench, where there might be no adequate cooling.

ASUS (measured) power table - 
NOTE: This is only for ASUS RTL8812AU, not any RTL8812AU !
//19: 10-12 mW
//25: 25-30 mW
//30: 45-50 mW
//35: 70-80 mW
//37: 100-110 mW
//40: 120-140 mW
//45: 200-230 mW
//50: 280- 320 mW
//55: 380-400 mW
//58: 420-450 mW

Non-RTL8812AU
It is hard to say what tx power card(s) other than rtl8812au produce. For all cards other than rtl8812au, OpenHD offers the option to set the
tx power in mW (which is then applied via linux kernel iw command). If your card accepts tx power at all, or always sends on the same tx power,
depends on the manufacturer / firmware running on the card. However, if you are running on an openhd image, we have removed the linux kernel tx
power restrictions (crda) such that some cards might change tx power accordingly / can be used on their maximum tx power.
