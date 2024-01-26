import tkinter as tk
import serial

root=tk.Tk()
root.title("GUI put On-Off")
root.geometry("300x300")
Ser=serial.Serial("com3",9600)
def TurnOn():
    Ser.write(b'o')

def TurnOff():
    Ser.write(b'x')

lab=tk.Label(root,text='Turn on and off')
lab.pack()
btn1=tk.Button(root,text='ON',command=TurnOn)
btn1.pack()
btn2=tk.Button(root,text='Off',command=TurnOff)
btn2.pack()

root.mainloop()
