import opc
import time
import random

leds = [(255,255,255)]*360 #white

client = opc.Client('localhost:7890')
client.put_pixels(leds)
client.put_pixels(leds)

#for led in leds: # pick out an element: led = (255,255,255)
#for led in range(60): #pick out indices: led = 0,1,2,3....
#   leds[led] = (255,0,0)
#   time.sleep(.1)
#   client.put_pixels(leds)

#led = 0
#while led<60:
#    leds[led] = (0,255,0)
#    time.sleep(.1)
#    client.put_pixels(leds)
#    led = led + 1 #or reverse if you want

led = 0
while led<60:
    for rows in range(3):
        leds[led + rows*60] = (0,0,255)
    for rows in range(3,6):
        leds[59-led + rows*60] = (rows*20,50,255)
    client.put_pixels(leds)
    time.sleep(.1)
    led = led + 1

    
while True:
    for led in range(0, 360, 60):
        leds = [(255,255,255)]*360
        leds[355-led] = (0,0,255)
        leds[355-led+1] = (0,0,255)
        leds[355-led+2] = (0,0,255)
        leds[355-led+3] = (0,0,255)
        leds[355-led+4] = (0,0,255)
        if led == 355:
            led = 0
        client.put_pixels(leds)
        time.sleep(0.02)
    




