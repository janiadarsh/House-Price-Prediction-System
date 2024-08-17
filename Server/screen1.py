import tkinter as tk
import time
from screen3 import *
from userinterface import *
from PIL import ImageTk,Image;


def display2():
    root1=Tk()
    root1.title("House Price Prediction System")
    root1.geometry("1000x1000")

    # def back():
    def destroyscreen1():
        time.sleep(0)
        root1.destroy()
        display4()

    # Button(root,text="Back",command=back()).pack()
    img=Image.open("server/OIP.gif")
    img1=img.resize((1000,600))
    img2=ImageTk.PhotoImage(img1)
    panel = tk.Label(window, image = img2)
    panel.pack()
    btn =Button(window,text="Predict Price!",command=destroyscreen1,width=500,height=2).pack()
    root1.mainloop()
