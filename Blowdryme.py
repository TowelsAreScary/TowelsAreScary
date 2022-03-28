import board
import neopixel
from digitalio import DigitalInOut, Direction, Pull
import touchio


touch_pad = board.A0
touch = touchio.TouchIn(touch_pad)

pixel_pin = board.D2
num_pixels = 12

pixels = neopixel.NeoPixel(pixel_pin, num_pixels, brightness=0.4, auto_write=False)

pixels.fill(0, 0, 0)
pixels.show()
while True:
    if touch.value:
        for num in range(0, 200, 2):
            Blue = (num, num, 255)
            Green = (num, 255, num)
            Red = (255, num, num)
            pixels.fill(Blue)
            pixels.show()
        for num in range(0, 200, 2):
            Bne = (200 - num, 200 - num, 255)
            Gne = (200 - num, 255, 200 - num)
            Rne = (255, 200 - num, 200 - num)
            pixels.fill(Bne)
            pixels.show()
    if touch.value:
        for num in range(0, 200, 2):
            Blue = (num, num, 255)
            Green = (num, 255, num)
            Red = (255, num, num)
            pixels.fill(Green)
            pixels.show()
        for num in range(0, 200, 2):
            Bne = (200 - num, 200 - num, 255)
            Gne = (200 - num, 255, 200 - num)
            Rne = (255, 200 - num, 200 - num)
            pixels.fill(Gne)
            pixels.show()
    if touch.value:
        for num in range(0, 200, 2):
            Blue = (num, num, 255)
            Green = (num, 255, num)
            Red = (255, num, num)
            pixels.fill(Red)
            pixels.show()
        for num in range(0, 200, 2):
            Bne = (200 - num, 200 - num, 255)
            Gne = (200 - num, 255, 200 - num)
            Rne = (255, 200 - num, 200 - num)
            pixels.fill(Rne)
            pixels.show()

