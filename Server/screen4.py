import tkinter as tk
import time
from util import *
from PIL import ImageTk,Image;


def display5():
    root=Tk()
    root.title("House Price Prediction System")
    root.geometry("1000x640")
    root.attributes('-fullscreen',True)


    def destroyscreen1():
        time.sleep(0)
        root.destroy()
        display()
    img=Image.open("server/Houseprice3.gif")
    img1=img.resize((1530,820))
    img2=ImageTk.PhotoImage(img1)
    panel = tk.Label(root, image = img2)
    panel.pack()
    btn =Button(root,text="Next ->",command=destroyscreen1,width=500,height=2).pack()

    root.mainloop()
