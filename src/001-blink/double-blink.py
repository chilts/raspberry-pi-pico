from machine import Pin
from time import sleep

led = Pin(25, Pin.OUT)
led.off()

n = 0
while True:
    n = n + 1
    print("n is {}".format(n))
    led.toggle()
    sleep(0.1)
    led.toggle()
    sleep(0.1)
    led.toggle()
    sleep(0.1)
    led.toggle()
    sleep(0.7)
