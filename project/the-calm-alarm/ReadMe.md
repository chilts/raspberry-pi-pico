# The Calm Alarm #

Just a small alarm clock which is nice and easy to set up.

## Raspberry Pi Pico Pinout ##

[![raspberry-pi-pico-pinout.png](https://i.postimg.cc/jdsgFxbX/raspberry-pi-pico-pinout.png)](https://postimg.cc/Th4JyXhL)

## Setup ##

Connection Pins:

| Pico   | ESP8266 |
| ------ | ------- |
| 0 (TX) | 3 (RX)  |
| 1 (RX) | 1 (TX)  |
| 2      | RST     |
| GND    | GND     |

The ESP8266 can be powered from the Pico, or a separate power source can be
used but retaining the common GND connection. Pico pin 2 is used to reset the
ESP8266.


(Ends)
