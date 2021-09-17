from machine import Pin, Timer

led = Pin(25, Pin.OUT)
timer = Timer()

def tick(timer):
    # global led
    led.toggle()

timer.init(freq=2.5, mode=Timer.PERIODIC, callback=tick)
