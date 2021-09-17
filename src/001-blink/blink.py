from machine import Pin
from time import sleep

led = Pin(25, Pin.OUT)

n = 0
while True:
    n = n + 1
    print("n is {}".format(n))
    led.toggle()
    sleep(0.5)
    led.toggle()
    sleep(0.5)
