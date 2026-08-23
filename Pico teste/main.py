from machine import Pin
from neopixel import NeoPixel
import time

led = NeoPixel(Pin(16), 1)


def set_color(red, green, blue):
    led[0] = (red, green, blue)
    led.write()


while True:
    set_color(80, 0, 0)
    time.sleep(0.5)

    set_color(0, 0, 0)
    time.sleep(0.5)

    set_color(0, 80, 0)
    time.sleep(0.5)

    set_color(0, 0, 0)
    time.sleep(0.5)

    set_color(0, 0, 80)
    time.sleep(0.5)

    set_color(0,10, 20)
    time.sleep(4)
