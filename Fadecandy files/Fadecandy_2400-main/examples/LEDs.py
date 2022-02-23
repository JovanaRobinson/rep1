import opc
import time

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
    
