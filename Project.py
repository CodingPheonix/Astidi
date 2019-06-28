from tkinter import *

import serial;

root = Tk()

prt = "/dev/ttyACM0"
s1 = serial.Serial(prt, 9600)
s1.flushInput()
while True:
    if(s1.inWaiting()>0):
        Input = ord(s1.read(1));
def switch(req):
    if (req=="Home"):
        w.delete("all")
        btn = Button(root, text = "Monitor Plants", command=lambda:switch("MonitorPlants"), bg="OliveDrab2")
        btn2 = Button(root, text = "Add Plants", command=lambda:switch("AddPlants"), bg="OliveDrab2")
        btn_window = w.create_window(W/2,H/2-25,anchor=CENTER,window=btn)
        btn2_window = w.create_window(W/2,H/2+25,anchor=CENTER,window=btn2)
        w.pack()
    elif(req=="MonitorPlants"):
        w.delete("all")
        w.create_rectangle(10,25,262.5+10/3,455)
        lb1 = Label(root, text = "Shelf 1")
        lb1_window = w.create_window(135,25,anchor=CENTER,window=lb1)
        txt1 = Label(root, text = "Soil Moisture:")
        txt1_window = w.create_window(135,75,anchor=CENTER,window=txt1)
        button = Button(root, text="Add Moisture", bg="OliveDrab2");
        button_window = w.create_window(135,97.5,anchor=CENTER,window=button)
        button1 = Button(root, text="Reduce Moisture", bg="OliveDrab2");
        button1_window = w.create_window(135,120,anchor=CENTER,window=button1)
        light1 = Label(root, text = "Amount of light recieved:")
        light1_window = w.create_window(135,200,anchor=CENTER,window=light1)
        humidity1 = Label(root, text = "Amount of humidity recieved: "+data["Hum1"])
        humidity1_window = w.create_window(135,300,anchor=CENTER,window=humidity1)

        w.create_rectangle(262.5-10/3,25,525+10/3,455)
        lb2 = Label(root, text = "Shelf 2")
        lb2_window = w.create_window(397.5+10/3,25,anchor=CENTER,window=lb2)
        txt2 = Label(root, text = "Soil Moisture:")
        txt2_window = w.create_window(397.5+10/3,75,anchor=CENTER,window=txt2)
        button2 = Button(root, text="Add Moisture", bg="OliveDrab2");
        button2_window = w.create_window(397.5+10/3,97.5,anchor=CENTER,window=button2)
        button3 = Button(root, text="Reduce Moisture", bg="OliveDrab2");
        button3_window = w.create_window(397.5+10/3,120,anchor=CENTER,window=button3)
        light2 = Label(root, text = "Amount of light recieved:")
        light2_window = w.create_window(397.5+10/3,200,anchor=CENTER,window=light2)
        humidity2 = Label(root, text = "Amount of humidity recieved: "+data["Hum2"])
        humidity2_window = w.create_window(397.5+10/3,300,anchor=CENTER,window=humidity2)

        w.create_rectangle(525-10/3,25,792.5,455)
        lb3 = Label(root, text = "Shelf 3")
        lb3_window = w.create_window(650+20/3,25,anchor=CENTER,window=lb3)
        txt3 = Label(root, text = "Soil Moisture:")
        txt3_window = w.create_window(650+20/3,75,anchor=CENTER,window=txt3)
        button4 = Button(root, text="Add Moisture", bg="OliveDrab2");
        button4_window = w.create_window(650+20/3,97.5,anchor=CENTER,window=button4)
        button5 = Button(root, text="Reduce Moisture", bg="OliveDrab2");
        button5_window = w.create_window(650+20/3,120,anchor=CENTER,window=button5)
        light3 = Label(root, text = "Amount of light recieved:")
        light3_window = w.create_window(650+20/3,200,anchor=CENTER,window=light3)
        humidity3 = Label(root, text = "Amount of humidity recieved: "+data["Hum3"])
        humidity3_window = w.create_window(650+20/3,300,anchor=CENTER,window=humidity3)
        

        btn = Button(root, text = "Back", command=lambda:switch("Home"), bg="OliveDrab2")    
        btn_window = w.create_window(W/2,H-25,anchor=CENTER,window=btn)

        w.pack()

d = open("Data.txt","r").read().split("\n")
data = {}
for x in d:
    X=x.split(".")
    for i in range(len(X)):
        data[str(X[i].split(":")[0])]=X[i].split(":")[1]
print(data)
root.title("Astidi")        
W = 800
H = 480

w = Canvas(root, width=W, height=H, bg = "Sea Green")
w.pack()

global btn
btn = Button(root, text = "Welcome to ASTIDI Interactive User Interface", command=lambda:switch("Home"), bg="OliveDrab2")
global btn_window
btn_window = w.create_window(W/2,H/2,anchor=CENTER,window=btn)

mainloop()
