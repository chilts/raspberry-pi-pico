# Setup
#
# Connect an LED + Resistor.
# * LED - Pin20 / GP15 to a spare row on the breadboard
# * Resistor - from the spare row to Pin18 / GND

from machine import Pin, Timer
import time
from time import sleep
import time

# set up the power on LED
led = Pin(25, Pin.OUT)
led.value(1)

# set up the indicator timer
ledIndicatorLeft = Pin(15, Pin.OUT)
ledIndicatorLeft.value(0)
def indicatorBlink(timer):
    # print("Tick")
    ledIndicatorLeft.toggle()
indicatorTimer = Timer()
indicatorTimer.init(freq=2, mode=Timer.PERIODIC, callback=indicatorBlink)

# set up the headlights
btnHeadlights = Pin(16, Pin.IN, Pin.PULL_DOWN)
ledHeadlight1 = Pin(17, Pin.OUT)
ledHeadlight2 = Pin(18, Pin.OUT)
ledHeadlight1.value(0)
ledHeadlight2.value(0)

while True:
    ledHeadlight1.value(btnHeadlights.value())
    ledHeadlight2.value(btnHeadlights.value())
    # print(btnHeadlights.value())
    time.sleep(0.05)
