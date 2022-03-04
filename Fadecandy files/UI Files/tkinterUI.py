from tkinter import*
import sys
import tkinter as tk


class App(threading.Thread):       #Threading to avoid block to code due to GUI 

    def __init__(self, tk_w):
        self.w = tk_w
        threading.Thread.__init__(self)   
        self.start()

    def run(self):
        loop_active = True
        while loop_active:
            main()
            
            
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

def Y():
    return

def B():
    return

def R():
    return

def G():
    return
    
label =Label(w,bg='#141414',fg='white',
             text= "Four colored blocks will \nlight up in a specific pattern. \nAfter displaying the pattern, \nthe player must repeat the pattern \nby clicking the buttons in proper order.").place(x=45,y=0)
bttn(0,222,"Y E L L O W",'#ffff00',"#141414",Y)
bttn(0,259,"B L U E",'#25dae9',"#141414",B)
bttn(0,296,"R E D",'#ff0000',"#141414",R)
bttn(0,333,"G R E E N",'#00ff00',"#141414",G)

display=Label(w,
             bg='#141414',fg='white',text = 'Hello there').place(x=135,y=80)

btn_enter = Button(w,
                   bg='grey',text='Enter').place(x=118,y=450)

w.mainloop()
