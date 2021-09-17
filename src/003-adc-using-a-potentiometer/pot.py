# Uses GP26.
#
# Setup
#
# 1. Connect the POT's lower PIN to GND.
# 2. Connect the POT's Wiper to PIN31 / GP26
# 3. Connect the POT's upper PIN to PIN36 / 3V3(OUT)

import machine
import utime

pot = machine.ADC(26)

while True:
    print(pot.read_u16())
    utime.sleep(0.25)
