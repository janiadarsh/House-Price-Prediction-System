import pickle
import json
import numpy as np
import tkinter
from tkinter import *
from PIL import ImageTk,Image;



__locations = None
__data_columns = None
__model = None

def get_estimated_price(location,sqft,bhk,bath):
    try:
        loc_index = __data_columns.index(location.lower())
    except:
        loc_index = -1

    x = np.zeros(len(__data_columns))
    x[0] = sqft
    x[1] = bath
    x[2] = bhk
    if loc_index>=0:
        x[loc_index] = 1

    return round(__model.predict([x])[0],2)


def load_saved_artifacts():
    print("loading saved artifacts...start")
    global  __data_columns
    global __locations

    with open("server/artifacts/columns.json", "r") as f:
        __data_columns = json.load(f)['data_columns']
        __locations = __data_columns[3:]  # first 3 columns are sqft, bath, bhk

    global __model
    if __model is None:
        with open('server/artifacts/banglore_home_prices_model.pickle', 'rb') as f:
            __model = pickle.load(f)
    print("loading saved artifacts...done")

def get_location_names():
    return __locations

def get_data_columns():
    return __data_columns

load_saved_artifacts()
# print(get_location_names())
print(get_estimated_price('1st Phase JP Nagar',1000, 3, 3))
# print(get_estimated_price('1st Phase JP Nagar', 1000, 2, 2))
# print(get_estimated_price('Kalhalli', 1000, 2, 2)) # other location
# print(get_estimated_price('Ejipura', 1000, 2, 2))  # other location

def display():
    root=Tk()
    root.title("House Price Prediction System")
    #root.geometry("1500x1500")
    root.attributes('-fullscreen',True)

    root.config(background="white")
    # Label(root,text="this is a practice example").pack()

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
    value_inside =StringVar(root)
    
    # Set the default value of the variable
    value_inside.set("Select the city where you want to predict house price")
    
    # Create the optionmenu widget and passing 
    # the options_list and value_inside to it.
    question_menu =OptionMenu(root, value_inside, *option_menu)
    question_menu.pack()
    
    # Function to print the submitted option-- testing purpose
    def exitpage():
        root.destroy()
    # def goback():
    #     root.destroy()
    #     playui()

    
    def print_answers():
        # Label(root,text="Selected answer is " + format(value_inside.get())).pack()
        print("Selected Option: {}".format(value_inside.get()))
        locate=format(value_inside.get())
        boi=sqft.get()
        print("the string is ",boi)
        choice=v.get()
        print(choice)
        choice2=b.get()
        print(choice2)
        print(get_estimated_price(locate,boi,choice,choice2))
        selection=selected.get()
        oldness=oldprop.get()
        if(selection==1 and oldness==4):
            answeris =str(get_estimated_price(locate,boi,choice,choice2)+120)
        elif(selection==1 and oldness==5):
            answeris =str(get_estimated_price(locate,boi,choice,choice2)+105)
        elif(selection==1 and oldness==6):
            answeris =str(get_estimated_price(locate,boi,choice,choice2)+100)
        elif(selection==1 and oldness==7):
            answeris =str(get_estimated_price(locate,boi,choice,choice2)+92)
        elif(selection==2 and oldness==4):
            answeris =str(get_estimated_price(locate,boi,choice,choice2)+98)
        elif(selection==2 and oldness==5):
            answeris =str(get_estimated_price(locate,boi,choice,choice2)+94)
        elif(selection==2 and oldness==6):
            answeris =str(get_estimated_price(locate,boi,choice,choice2)+86)
        elif(selection==2 and oldness==7):
            answeris =str(get_estimated_price(locate,boi,choice,choice2)+80)
        elif(selection==3 and oldness==4):
            answeris =str(get_estimated_price(locate,boi,choice,choice2)+60)
        elif(selection==3 and oldness==5):
            answeris =str(get_estimated_price(locate,boi,choice,choice2)+30)
        elif(selection==3 and oldness==6):
            answeris =str(get_estimated_price(locate,boi,choice,choice2)+20)
        elif(selection==3 and oldness==7):
            answeris =str(get_estimated_price(locate,boi,choice,choice2))

        


        gh=get_estimated_price(locate,boi,choice,choice2)

        st = "The predicted price for " + locate + " with " + boi + " sqft, " + choice + " BHK and " + choice2 + " bathroom is ₹" + answeris + " Lakhs"
        print(st)
        
        
        if(gh<=0):
            Lt=Label(root,text="Invalid Input for the Sqft field",bg="white").pack()
        # elif(gh>5500):
        #     Lt=Label(root,text="Invalid Input for the Sqft field",bg="white").pack()  
        else:
            Label(root,text=st).pack()
        return None

    
    # Submit button
    # Whenever we click the submit button, our submitted
    # option is printed ---Testing purpose
    # submit_button = tkinter.Button(root, text='Submit', command=print_answers)
    # submit_button.pack()
    
    # def printc():
    #     boi=sqft.get()
    #     print("the string is ",boi)
    sqft = StringVar(root)
    Label(root,text="Enter the desired squarefeet",bg="white").pack()
    Entry(root,textvariable=sqft).pack()





    Label(root,text="Enter the required BHK for your house",bg="white").pack()
    #radio button
    v = StringVar(root, "1")
    # def call():
    #     choice=v.get()
    #     print(choice)
    values = {"1 BHK" : "1",
            "2 BHK" : "2",
            "3 BHK" : "3",
            "4 BHK" : "4",
            "5 BHK" : "5"}

    for (text, value) in values.items():
        Radiobutton(root, text = text, variable = v,
            value = value,bg="white").pack(side = TOP, ipady = 1)

    Label(root,text="Enter the number of required bathrooms",bg="white").pack()
    b=StringVar(root,"1")

    def call2():
        choice2=b.get()
        print(choice2)

    values = {"1 bathroom" : "1",
            "2 bathroom" : "2",
            "3 bathroom" : "3",
            "4 bathroom" : "4",
            "5 bathroom" : "5"}

    for (text, value) in values.items():
        Radiobutton(root, text = text, variable = b,
            value = value,bg="white").pack(side = TOP, ipady = 1)
        

    selected = IntVar()
    Label(root,text="Enter the type of property you want",bg="white").pack()
    Radiobutton(root, text='Bungalow', value=1, variable=selected,bg="white").pack()
    Radiobutton(root, text='Farm House', value=2, variable=selected,bg="white").pack()
    Radiobutton(root, text='Flat', value=3, variable=selected,bg="white").pack()

    oldprop = IntVar()
    Label(root,text="How old is the property",bg="white").pack()
    Radiobutton(root, text='0 to 2 Year old', value=4, variable=oldprop,bg="white").pack()
    Radiobutton(root, text='2 to 5 Year old', value=5, variable=oldprop,bg="white").pack()
    Radiobutton(root, text='5 to 9 year old', value=6, variable=oldprop,bg="white").pack()
    Radiobutton(root, text="9 years or above", value=7,variable=oldprop,bg="white").pack()
    Button(root,text="PREDICT PRICE!",command=print_answers,bg="black",fg="white").pack()
    label2=Label(root,text="Predicted price in Lakhs will be shown here...",bg="white").pack()
    # Button(root,text="Back",command=goback).pack()
    Button(root,text="EXIT",command=exitpage,width=10,bg="red",fg="black").pack()

    root.mainloop()


