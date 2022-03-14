import time
import board
import neopixel
import random

p = [ 0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1,]
pixel_pin = board.D2
num_pixels = 12
pixels = neopixel.NeoPixel(pixel_pin, num_pixels, brightness=1, auto_write=False)



l = [ 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200, 210, 220, 230, 240, 250, 255]
t = [ 0, 0.2, 0.4, 0.6, 0.8, 1, 1.2, 1.4, 1.6, 1.8, 2]
OFF = (0,0,0)



while True:
    for i in range(0,12,1):
        for num in range(0,(random.choice(l)),2):
            COLOR=(num,0,254-num)
            pixels[i]=COLOR
            pixels[i+1]=COLOR
            pixels.show()
        for num in range(0,(random.choice(l)),2):
            COLOR=(254-num,0,num)
            pixels[i]=COLOR
            pixels[i+1]=COLOR
            pixels.show()
            pixels[i]=OFF
