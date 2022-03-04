from tkinter import*
import sys
import tkinter as tk
import threading
import time
from time import sleep
from LEDs import *

class App(threading.Thread):

    def __init__(self, tk_w):
        self.w = tk_w
        threading.Thread.__init__(self)
        self.start()

    def run(self):
        loop_active = True
        while loop_active:
            main()#do something here to start when lets go displays

w=Tk()
w.geometry('300x500')
w.configure(bg="#141414")
w.title('Simon Game')

            
def bttn(x,y,text,bcolor,fcolor,cmd):

    def on_enter(e):
        mybutton['background']=bcolor
        mybutton['foreground']=fcolor

    def on_leave(e):
        mybutton['background']=fcolor
        mybutton['foreground']=bcolor

    mybutton=Button(w,width=42,height=2,text=text,
                    fg=bcolor,
                    bg=fcolor,
                    border=0,
                    activeforeground=fcolor,
                    activebackground=bcolor,
                    command=cmd,)
    
    mybutton.bind("<Enter>", on_enter)
    mybutton.bind("<Leave>", on_leave)

    mybutton.place(x=x,y=y)
    
list1=[]
list2=[]

def Y():
    list1.append('yellow')

def B():
    list1.append('blue')
    
def R():
    list1.append('red')

def G():
    list1.append('green')

def yes():
    if list2==['intro']:
        replace1()
    elif list2==['final']:
        main()

def no():
    if list2==['intro']:
        end_anim()
        quit()
        
    elif list2==['final']:
        replace2()

def replace1():
    myLabel.config(text= "Let's go!")

def replace2():
    myLabel.config(text= "Thank you for playing!")

myLabel=tk.Label(w,text="Would you like to play the Simon Game?",bg='#141414',fg='#d3d3d3')
myLabel.place(x=45,y=140)

bits = ( (80,0,0), (0,255,0) )

def end_anim():

    for i in range(1):
            # Flash each strip in turn
            for strip in range(12):
                    pixels = [ (90,90,90) ] * 512 #change 360 to higher number
                    for i in range(16):
                            pixels[strip * 32 + i * 2] = (200,200,200)

                    # Label all strips always
                    for s in range(12):
                            pixels[s * 32 + 0] = bits[(s >> 2) & 1]
                            pixels[s * 32 + 1] = bits[(s >> 1) & 1]
                            pixels[s * 32 + 2] = bits[(s >> 0) & 1]

                    client.put_pixels(pixels)
                    time.sleep(0.5)
    

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

    def too_long():
        for i in range(0,30):
                pixels = [ (0,0,0) ] * 361
                pixels[i] = (255,192,203)
                client.put_pixels(pixels)
                time.sleep(0.01)


    list2.append('intro')
    sleep(15)
    list2.clear()

    myLabel.config(text= "First Sequence")
    sleep(1)

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
    sleep(.1)
    white()

    
    myLabel.config(text= "Enter your sequence")
    time.sleep(8) 
    if list1==['blue','red','yellow','green']:
        myLabel.config(text= "Correct!")
        for i in range(20):
            right()
            time.sleep(0.05) 
            client.put_pixels(black)
            time.sleep(0.05)
    elif list1==[]:
        myLabel.config(text= "Oops, took too long")
        for i in range(20):
            too_long()
            time.sleep(0.05) 
            client.put_pixels(black)
            time.sleep(0.05)
    else:
        myLabel.config(text= "Incorrect!")
        for i in range(20):
            wrong()
            time.sleep(0.05) 
            client.put_pixels(black)
            time.sleep(0.05)

    leds = [(20,20,20)]*360
    time.sleep(1)
    list1.clear()

    myLabel.config(text= "Second Sequence")
    sleep(1)

    yellow()
    sleep(.3)
    leds = [(20,20,20)]*360
    sleep(.3)
    green()
    sleep(.3)
    leds = [(20,20,20)]*360
    sleep(.3)
    red()
    sleep(.3)
    leds = [(20,20,20)]*360
    sleep(.3)
    blue()
    sleep(.3)
    leds = [(20,20,20)]*360
    sleep(.3)
    yellow()
    sleep(.3)
    leds = [(20,20,20)]*360
    sleep(.3)
    white()
    
    myLabel.config(text= "Enter your sequence")
    list1.clear()
    time.sleep(10)
    if list1 == ['yellow','green','red','blue','yellow']:
        myLabel.config(text= "Correct!")
        for i in range(20):
            right()
            time.sleep(0.05) 
            client.put_pixels(black)
            time.sleep(0.05)
    elif list1==[]:
        myLabel.config(text= "Oops, took too long")
        for i in range(20):
            too_long()
            time.sleep(0.05) 
            client.put_pixels(black)
            time.sleep(0.05)
    else:
        myLabel.config(text= "Incorrect!")
        for i in range(20):
            wrong()
            time.sleep(0.05) 
            client.put_pixels(black)
            time.sleep(0.05)
            
    leds = [(20,20,20)]*360
    time.sleep(1)
    list1.clear()

    myLabel.config(text= "Third Sequence")
    sleep(1)

    green()
    sleep(.3)
    leds = [(20,20,20)]*360
    sleep(.3)
    red()
    sleep(.3)
    leds = [(20,20,20)]*360
    sleep(.5)
    green()
    sleep(.3)
    leds = [(20,20,20)]*360
    sleep(.3)
    blue()
    sleep(.3)
    leds = [(20,20,20)]*360
    sleep(.3)
    red()
    sleep(.3)
    leds = [(20,20,20)]*360
    sleep(.3)
    blue()
    sleep(.3)
    leds = [(20,20,20)]*360
    sleep(.3)
    white()
    
    myLabel.config(text= "Enter your sequence")
    list1.clear()
    time.sleep(12)
    if list1==['green','red','green','blue','red','blue']:
        myLabel.config(text= "Correct!")
        for i in range(20):
            right()
            time.sleep(0.05) 
            client.put_pixels(black)
            time.sleep(0.05)
    elif list1==[]:
        myLabel.config(text= "Oops, took too long")
        for i in range(20):
            too_long()
            time.sleep(0.05) 
            client.put_pixels(black)
            time.sleep(0.05)
    else:
        myLabel.config(text= "Incorrect!")
        for i in range(20):
            wrong()
            time.sleep(0.05) 
            client.put_pixels(black)
            time.sleep(0.05)

    leds = [(20,20,20)]*360
    time.sleep(1)
    list1.clear()


    myLabel.config(text= "Do you wish to play again?")
    list2.append('final')
            

    list2.clear()

    
label =Label(w,bg='#141414',fg='white',
             text= "Four colored blocks will \nlight up in a specific pattern. \nAfter displaying the pattern, \nthe player must repeat the pattern \nby clicking the buttons in proper order.").place(x=45,y=0)
bttn(0,222,"Y E L L O W",'#ffff00',"#141414",Y)
bttn(0,259,"B L U E",'#25dae9',"#141414",B)
bttn(0,296,"R E D",'#ff0000',"#141414",R)
bttn(0,333,"G R E E N",'#00ff00',"#141414",G)

btn_Yes = Button(w,
                   bg='grey',text='Yes',command=yes).place(x=90,y=450)
btn_No = Button(w,
                   bg='grey',text='No',command=no).place(x=180,y=450)



APP = App(w)
w.mainloop()
