import opc
import time
from time import sleep

leds = [(20,20,20)]*360

client = opc.Client('localhost:7890')
client.put_pixels(leds)
client.put_pixels(leds)

def red():
    for led in range(0,15):
        leds[led] = (255,0,0)
    for led in range(60,75):
        leds[led] = (255,0,0)
    for led in range(120,135):
        leds[led] = (255,0,0)
    for led in range(180,195):
        leds[led] = (255,0,0)
    for led in range(240,255):
        leds[led] = (255,0,0)
    for led in range(300,315):
        leds[led] = (255,0,0)
        client.put_pixels(leds)


def blue():
    for led in range(15,30):
        leds[led] = (0,0,255)
    for led in range(75,90):
        leds[led] = (0,0,255)
    for led in range(135,150):
        leds[led] = (0,0,255)
    for led in range(195,210):
        leds[led] = (0,0,255)
    for led in range(255,270):
        leds[led] = (0,0,255)
    for led in range(315,330):
        leds[led] = (0,0,255)
        client.put_pixels(leds)


def yellow():
    for led in range(30,45):
        leds[led] = (255,255,0)
    for led in range(90,105):
        leds[led] = (255,255,0)
    for led in range(150,165):
        leds[led] = (255,255,0)
    for led in range(210,225):
        leds[led] = (255,255,0)
    for led in range(270,285):
        leds[led] = (255,255,0)
    for led in range(330,345):
        leds[led] = (255,255,0)
        client.put_pixels(leds)


def green():
    for led in range(45,60):
        leds[led] = (0,255,0)
    for led in range(105,120):
        leds[led] = (0,255,0)
    for led in range(165,180):
        leds[led] = (0,255,0)
    for led in range(225,240):
        leds[led] = (0,255,0)
    for led in range(285,300):
        leds[led] = (0,255,0)
    for led in range(345,360):
        leds[led] = (0,255,0)
        client.put_pixels(leds)

def white():
    for led in range(0,360):
        leds[led] = (20,20,20)
        client.put_pixels(leds)

def first():
    leds[59] = (255,0,0)
    leds[119] = (255,0,0)
    leds[179] = (255,0,0)
    leds[239] = (255,0,0)
    leds[299] = (255,0,0)
    leds[359] = (255,0,0)
    client.put_pixels(leds)


def second():
    leds[58] = (255,0,0)
    leds[118] = (255,0,0)
    leds[178] = (255,0,0)
    leds[238] = (255,0,0)
    leds[298] = (255,0,0)
    leds[358] = (255,0,0)
    leds[239] = (255,0,0)
    client.put_pixels(leds)
    
def third():
    leds[57] = (255,0,0)
    leds[117] = (255,0,0)
    leds[177] = (255,0,0)
    leds[237] = (255,0,0)
    leds[297] = (255,0,0)
    leds[357] = (255,0,0)
    leds[238] = (255,0,0)
    leds[239] = (255,0,0)
    client.put_pixels(leds)

def fourth():
    leds[56] = (255,0,0)
    leds[116] = (255,0,0)
    leds[176] = (255,0,0)
    leds[236] = (255,0,0)
    leds[296] = (255,0,0)
    leds[356] = (255,0,0)
    leds[237] = (255,0,0)
    leds[238] = (255,0,0)
    leds[239] = (255,0,0)
    client.put_pixels(leds)

def fifth():
    leds[55] = (255,0,0)
    leds[115] = (255,0,0)
    leds[175] = (255,0,0)
    leds[235] = (255,0,0)
    leds[295] = (255,0,0)
    leds[355] = (255,0,0)
    leds[236] = (255,0,0)
    leds[237] = (255,0,0)
    leds[238] = (255,0,0)
    leds[239] = (255,0,0)
    client.put_pixels(leds)

def sixth():
    leds[54] = (255,0,0)
    leds[114] = (255,0,0)
    leds[174] = (255,0,0)
    leds[234] = (255,0,0)
    leds[294] = (255,0,0)
    leds[354] = (255,0,0)
    leds[235] = (255,0,0)
    leds[236] = (255,0,0)
    leds[237] = (255,0,0)
    leds[238] = (255,0,0)
    leds[239] = (255,0,0)
    leds[59] = (255,0,0)
    leds[119] = (255,0,0)
    leds[179] = (255,0,0)
    leds[239] = (255,0,0)
    leds[299] = (255,0,0)
    leds[359] = (255,0,0)
    client.put_pixels(leds)
    
    

first()
sleep(.1)
leds = [(20,20,20)]*360
sleep(.1)
second()
sleep(.1)
leds = [(20,20,20)]*360
sleep(.1)
third()
sleep(.1)
leds = [(20,20,20)]*360
sleep(.1)
fourth()
sleep(.1)
leds = [(20,20,20)]*360
sleep(.1)
fifth()
sleep(.1)
leds = [(20,20,20)]*360
sleep(.1)
sixth()

    
