def main():

    import opc
    import time
    from time import sleep
    import sys, time

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

    for char in "Hello there!":
        print(char, end='')
        sys.stdout.flush()
        time.sleep(0.2)
        
    value = input("Let's play Simon! Type in 1 and press enter to begin playing:") 


    while True:
        if value.isdigit() == True: 
             value = int(value)
             if value > 1 or value < 1: 
                 value = input("please input the number required.")
                 continue 
             else:
                 break 
        else:
            value = input("invalid input, please provide an integer:")

    if value == 1:
        print("Four colored buttons light up in a specific pattern. After displaying the pattern, the player must repeat the pattern by clicking the buttons in proper order.")
        time.sleep(6)
        print("Let's begin!")
        time.sleep(1)

    print(blue())
    sleep(.5)
    leds = [(20,20,20)]*360
    sleep(.5)
    print(red())
    sleep(.5)
    leds = [(20,20,20)]*360
    sleep(.5)
    print(yellow())
    sleep(.5)
    leds = [(20,20,20)]*360
    sleep(.5)
    print(green())
    sleep(.5)
    leds = [(20,20,20)]*360
    sleep(.5)
    print(white())
    answer = input("Enter your sequence")
    if answer == '2134':
        print('Correct!')
    else:
        print("Incorrect!")
        

    print(yellow())
    sleep(.5)
    leds = [(20,20,20)]*360
    sleep(.5)
    print(green())
    sleep(.5)
    leds = [(20,20,20)]*360
    sleep(.5)
    print(red())
    sleep(.5)
    leds = [(20,20,20)]*360
    sleep(.5)
    print(blue())
    sleep(.5)
    leds = [(20,20,20)]*360
    sleep(.5)
    print(white())
    answer = input("Enter your sequence")
    if answer == '3412':
        print('Correct!')
    else:
        print("Incorrect!")

    print(green())
    sleep(.5)
    leds = [(20,20,20)]*360
    sleep(.5)
    print(red())
    sleep(.5)
    leds = [(20,20,20)]*360
    sleep(.5)
    print(green())
    sleep(.5)
    leds = [(20,20,20)]*360
    sleep(.5)
    print(blue())
    sleep(.5)
    leds = [(20,20,20)]*360
    sleep(.5)
    print(white())
    answer = input("Enter your sequence")
    if answer == '4142':
        print('Correct!')
    else:
        print("Incorrect!")

    restart=input("Do you wish to play again?").lower()
    if restart == "yes":
        main()
        
    else:
        exit()

main() #where code starts
        
