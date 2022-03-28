import time
import board
import neopixel
from digitalio import DigitalInOut, Direction, Pull
import touchio


touch_pad = board.A0 
touch = touchio.TouchIn(touch_pad)

pixel_pin = board.D2
num_pixels = 12

pixels = neopixel.NeoPixel(pixel_pin, num_pixels, brightness=0.3, auto_write=False)

RED = (255, 0, 0)
YELLOW = (255, 150, 0)
GREEN = (0, 255, 0)
CYAN = (0, 255, 255)
BLUE = (0, 0, 255)
PURPLE = (180, 0, 255)
WHITE = (255, 255, 255)
GRAY = (50, 50, 50)
OFF = (0, 0, 0)

myCOLORS = [WHITE, GRAY]

now = 0

while True:
    if touch.value:
        now = now+1
        if (now > 3):
            now = 0
        print(now)
        time.sleep(0.2)
    if(now == 0):
        pixels.fill(OFF)
        pixels.show()
    while (now == 1):
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
                now = now+1
                if (now > 1):
                    now = 2
                print(now)
                time.sleep(0.2)
    while (now == 2):
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
                now = now+1
                if (now > 2):
                    now = 3
                print(now)
                time.sleep(0.5)
    while (now == 3):
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
            if touch.value:
                now = now+1
                if (now > 3):
                    now = 0
                print(now)
                time.sleep(0.5)
    time.sleep(0.2)
