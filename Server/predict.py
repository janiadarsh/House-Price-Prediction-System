import tkinter
from tkinter import *
import json

root=Tk()
root.title("House Price Prediction System")
root.geometry("1500x500")
Label(root,text="this is a practice example").pack()

with open('server/artifacts/columns.json', encoding='utf8') as JSONFile:
    data = json.load(JSONFile)
    length=len(data['data_columns'][3:])
    option_menu = data['data_columns'][3:]
print("the length is", length)
print(length)
# print(len(data['data_columns'][3:]))
# print(length)
options_list = ["Option 1", "Option 2", "Option 3", "Option 4"]
# option_list = list()
# for i in range(lenght):
#     option_list.append(data)


# Variable to keep track of the option
# selected in OptionMenu
value_inside = tkinter.StringVar(root)
  
# Set the default value of the variable
value_inside.set("Select an Option")
  
# Create the optionmenu widget and passing 
# the options_list and value_inside to it.
question_menu = tkinter.OptionMenu(root, value_inside, *option_menu)
question_menu.pack()
  
# Function to print the submitted option-- testing purpose
  
  
def print_answers():
    Label(root,text="Selected answer is " + format(value_inside.get())).pack()
    print("Selected Option: {}".format(value_inside.get()))
    locate=format(value_inside.get())
    print(locate)
    boi=sqft.get()
    print("the string is ",boi)
    choice=v.get()
    print(choice)
    choice2=b.get()
    print(choice2)
    return None
  
  
# Submit button
# Whenever we click the submit button, our submitted
# option is printed ---Testing purpose
# submit_button = tkinter.Button(root, text='Submit', command=print_answers)
# submit_button.pack()
sqft = StringVar()
def printc():
    boi=sqft.get()
    print("the string is ",boi)

Label(root,text="squarefeet").pack()
Entry(root,textvariable=sqft).pack()






#radio button
v = StringVar(root, "1")
# def call():
#     choice=v.get()
#     print(choice)
values = {"RadioButton 1" : "1",
        "RadioButton 2" : "2",
        "RadioButton 3" : "3",
        "RadioButton 4" : "4",
        "RadioButton 5" : "5"}

for (text, value) in values.items():
    Radiobutton(root, text = text, variable = v,
        value = value).pack(side = TOP, ipady = 5)

Label(root,text="enter bathrooms").pack()
b=StringVar(root,"1")

def call2():
    choice2=b.get()
    print(choice2)

values = {"RadioButton 1" : "1",
        "RadioButton 2" : "2",
        "RadioButton 3" : "3",
        "RadioButton 4" : "4",
        "RadioButton 5" : "5"}

for (text, value) in values.items():
    Radiobutton(root, text = text, variable = b,
        value = value).pack(side = TOP, ipady = 5)

Button(root,text="give",command=print_answers).pack()

root.mainloop()


