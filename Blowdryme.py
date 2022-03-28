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
        now=now+1
        if (now>1):
            now=0
        print(now)
    if(now==0):
        pixels.fill(OFF)
        pixels.show()
    while (now==1):
        for color in range(0,len(myCOLORS),1):
            for light in range(0,12,1):
                pixels[light]=myCOLORS[color]
                pixels.show()
            if touch.value:
                now=now+1
                if (now>1):
                    now=0
                print(now)
                    
    time.sleep(0.2)
