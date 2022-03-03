from LEDs import * #importing hello animation from LEDs python script

def main():

    import opc
    import time
    from time import sleep
    import sys, time
    import msvcrt

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

    black = [ (0,0,0) ] * 360

    def wrong():
        leds[87] = (255,0,0)
        leds[88] = (255,0,0)
        leds[91] = (255,0,0)
        leds[92] = (255,0,0)
        leds[148] = (255,0,0)
        leds[149] = (255,0,0)
        leds[150] = (255,0,0)
        leds[151] = (255,0,0)
        leds[209] = (255,0,0)
        leds[210] = (255,0,0)
        leds[268] = (255,0,0)
        leds[269] = (255,0,0)
        leds[270] = (255,0,0)
        leds[271] = (255,0,0)
        leds[327] = (255,0,0)
        leds[328] = (255,0,0)
        leds[331] = (255,0,0)
        leds[332] = (255,0,0)
        client.put_pixels(leds)

    def right():
        leds[206] = (0,255,0)
        leds[207] = (0,255,0)
        leds[267] = (0,255,0)
        leds[268] = (0,255,0)
        leds[328] = (0,255,0)
        leds[209] = (0,255,0)
        leds[269] = (0,255,0)
        leds[150] = (0,255,0)
        leds[210] = (0,255,0)
        leds[91] = (0,255,0)
        leds[151] = (0,255,0)
        leds[32] = (0,255,0)
        leds[92] = (0,255,0)
        leds[33] = (0,255,0)
        leds[146] = (0,255,0)
        leds[145] = (0,255,0)
        client.put_pixels(leds)


            
##    class TimeoutExpired(Exception):
##        pass
##
##
##    def input_with_timeout(prompt, timeout, timer=time.monotonic):
##        """Timed input function, taken from https://stackoverflow.com/a/15533404/12892026"""
##        sys.stdout.write(prompt)
##        sys.stdout.flush()
##        endtime = timer() + timeout
##        result = []
##        while timer() < endtime:
##            if msvcrt.kbhit():
##                result.append(msvcrt.getwche()) #XXX can it block on multibyte characters?
##                if result[-1] == '\r':
##                    return ''.join(result[:-1])
##            time.sleep(0.04) # just to yield to other processes/threads
##        raise TimeoutExpired 

    

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

    blue()
    sleep(.5)
    leds = [(20,20,20)]*360
    sleep(.5)
    red()
    sleep(.5)
    leds = [(20,20,20)]*360
    sleep(.5)
    yellow()
    sleep(.5)
    leds = [(20,20,20)]*360
    sleep(.5)
    green()
    sleep(.5)
    leds = [(20,20,20)]*360
    sleep(.5)
    white()

    answer = input("Enter your sequence")
    if answer == '2134':
        print('Correct!')
        for i in range(20):
            right()
            time.sleep(0.05) 
            client.put_pixels(black)
            time.sleep(0.05)
    else:
        print("Incorrect!")
        for i in range(20):
            wrong()
            time.sleep(0.05) 
            client.put_pixels(black)
            time.sleep(0.05)

    leds = [(20,20,20)]*360

##    correctinput=2134
##
##    try:
##        answer = input("Enter your sequence: ") #5 second timer
##    
##    except TimeoutExpired:
##        print('\nSorry, time is up')
##    
        

    yellow()
    sleep(.5)
    leds = [(20,20,20)]*360
    sleep(.5)
    green()
    sleep(.5)
    leds = [(20,20,20)]*360
    sleep(.5)
    red()
    sleep(.5)
    leds = [(20,20,20)]*360
    sleep(.5)
    blue()
    sleep(.5)
    leds = [(20,20,20)]*360
    sleep(.5)
    white()
    
    answer = input("Enter your sequence")
    if answer == '3412':
        print('Correct!')
        for i in range(20):
            right()
            time.sleep(0.05) 
            client.put_pixels(black)
            time.sleep(0.05)
    else:
        print("Incorrect!")
        for i in range(20):
            wrong()
            time.sleep(0.05) 
            client.put_pixels(black)
            time.sleep(0.05)
            
    leds = [(20,20,20)]*360

    green()
    sleep(.5)
    leds = [(20,20,20)]*360
    sleep(.5)
    red()
    sleep(.5)
    leds = [(20,20,20)]*360
    sleep(.5)
    green()
    sleep(.5)
    leds = [(20,20,20)]*360
    sleep(.5)
    blue()
    sleep(.5)
    leds = [(20,20,20)]*360
    sleep(.5)
    white()
    
    answer = input("Enter your sequence")
    if answer == '4142':
        print('Correct!')
        for i in range(20):
            right()
            time.sleep(0.05) 
            client.put_pixels(black)
            time.sleep(0.05)
    else:
        print("Incorrect!")
        for i in range(20):
            wrong()
            time.sleep(0.05) 
            client.put_pixels(black)
            time.sleep(0.05)

    leds = [(20,20,20)]*360
            

    restart=input("Do you wish to play again?").lower()
    if restart == "yes":
        main()
        
    else:
        print("Thank you for playing!")
        sleep(.5)
        exit()

main() #where code starts
        
