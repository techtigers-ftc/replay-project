import utime
import machine
import neopixel
max_leds = 36
def do_test(max_leds, delay = 200):
    np = neopixel.NeoPixel(machine.Pin(5), max_leds)
    colors = [(128,0,0), (0,128,0),(0,0,128)]


    for color in colors:
        for on_index in range(max_leds):
            for led_index in range(max_leds):
                np[led_index] = (0, 0, 0)
            np[on_index] = color
            np.write()
            utime.sleep_ms(delay)
def square():
    np = neopixel.NeoPixel(machine.Pin(5), max_leds)
    np[0] = (128,0,0)
    np[1] = (128,0,0)
    np[2] = (128,0,0)
    np[15] = (128,0,0)
    np[17] = (128, 0,0)
    np[18] = (128,0,0)
    np[19] = (128,0,0)
    np[20] = (128,0,0)
    np.write()
