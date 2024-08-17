import tkinter as tk
import time
# from util import *
# from screen1 import *
from screen2 import *
#from screen3 import *
from PIL import ImageTk,Image;

window=Tk()
window.title("House Price Prediction System")
#window.geometry("1500x750")
window.attributes('-fullscreen',True)
def destroyscreen1():
    time.sleep(0)
    window.destroy()
    display3()

# def destroyscreen2():
#     time.sleep(0)
#     window.destroy()
#     display2()

# def destroyscreen3():
#     time.sleep(0)
#     window.destroy()
#     display3()

# def destroyscreen4():
#     time.sleep(0)
#     window.destroy()
#     display4()

img = ImageTk.PhotoImage(Image.open("server/mainhouse.gif"))

# v = Scrollbar(window, orient='vertical')
# v.pack(side = RIGHT, fill = Y)


img=Image.open("server/houseupdates.gif")
img1=img.resize((1530,820))
img2=ImageTk.PhotoImage(img1)
panel = tk.Label(window, image = img2)
panel.pack()
btn =Button(window,text="Next ->",command=destroyscreen1,width=500,height=2, background='#F6C646').pack()
# btn1=Button(window,text="Predict Price!",command=destroyscreen2,width=500,height=2).pack()
# btn2=Button(window,text="Predict Price!",command=destroyscreen3,width=500,height=2).pack()
# btn3=Button(window,text="Predict Price!",command=destroyscreen4,width=500,height=2).pack()
# hold1 = Image.open("wallpaper_winter.jpg")
# hold12=hold1.resize((1000,500))
# hold123 = ImageTk.PhotoImage(hold12)
# panel1=tk.Label(window,image=hold123).pack()


window.mainloop()
