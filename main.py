from tkinter import *
import tkinter as tk
from geopy.geocoders import Nominatim
from tkinter import ttk, messagebox
from timezonefinder import TimezoneFinder
from datetime import *
import requests
import random
import pytz
from PIL import Image, ImageTk

login_bg = "#caf0ff"
login_text = "black"
login_bg2 = "#fff"
login = Tk()
login.title("Authentication Window")
login.geometry("500x400+500+200")
login.resizable(False, False)
login.config(bg=login_bg)

def logUser():
    user = username.get()
    pwd = password.get()
    if user != "demo" or pwd != "demo":
        messagebox.showwarning("Login Error", "Invalid username or password")
        username.delete(0, tk.END)
        password.delete(0, tk.END)
    else:
        login.destroy()
        root=Tk()
        root.title("Weather App")
        root.geometry("890x470+300+200")
        random_number = random.randint(1, 4)
        bg = PhotoImage(file=f"./backgrounds/{random_number}.png")
        bgimg = Label(root, image=bg)
        bgimg.place(x=0, y=0)
        root.configure (bg="#57adff")
        root.resizable (False, False)
        def getWeather():
            city=textfield.get()
            geolocator= Nominatim (user_agent="geoapiExercises")
            location= geolocator.geocode (city)
            obj = TimezoneFinder()
            if location == None:
                messagebox.showerror("Error", "Location does not exist!")
                return
            result = obj.timezone_at (lng=location.longitude, lat=location.latitude)
            timezone.config(text=result)
            long_lat.config(text=f"{round (location.latitude,4)}°N, {round (location.longitude,4)}°E")
            home = pytz.timezone (result)
            local_time = datetime.now(home)
            current_time=local_time.strftime ("%I: %M %p")
            clock.config(text=current_time)

            api= "https://api.openweathermap.org/data/2.5/forecast?lat="+str(location.latitude)+"&lon="+str(location.longitude)+"&exclude=hourly,daily&appid=f733af53d79626f7924e4e19640924cb"
            json_data = requests.get(api).json()
            
            temp = json_data["list"][0]["main"]["temp"]
            humidity = json_data["list"][0]["main"]["humidity"]
            pressure = json_data["list"][0]["main"]["pressure"]
            wind= json_data["list"][0]["wind"]["speed"]
            description = json_data["list"][0]["weather"][0]["description"]

            t.config(text=(temp,"°C"))
            h.config(text=(humidity,"%"))
            p.config(text=(pressure,"hPa"))
            w.config(text=(wind,"m/s"))
            d.config(text = description)

            firstdayimage = json_data["list"][0]["weather"][0]["icon"]
            photo1 = ImageTk.PhotoImage(file=f"./icon/{firstdayimage}@2x.png")
            firstimage.config(image=photo1)
            firstimage.image = photo1

            seconddayimage = json_data["list"][8]["weather"][0]["icon"]
            img = (Image.open(f"icon/{seconddayimage}@2x.png"))
            resized_image = img.resize((40, 40))
            photo2 = ImageTk.PhotoImage(resized_image)
            secondimage.config(image=photo2)
            secondimage.image = photo2

            thirddayimage = json_data["list"][16]["weather"][0]["icon"]
            img = (Image.open(f"icon/{thirddayimage}@2x.png"))
            resized_image = img.resize((40, 40))
            photo3 = ImageTk.PhotoImage(resized_image)
            thirdimage.config(image=photo3)
            thirdimage.image = photo3

            fourthdayimage = json_data["list"][24]["weather"][0]["icon"]
            img = (Image.open(f"icon/{fourthdayimage}@2x.png"))
            resized_image = img.resize((40, 40))
            photo4 = ImageTk.PhotoImage(resized_image)
            fourthimage.config(image=photo4)
            fourthimage.image = photo4

            fifthdayimage = json_data["list"][32]["weather"][0]["icon"]
            img = (Image.open(f"icon/{fifthdayimage}@2x.png"))
            resized_image = img.resize((40, 40))
            photo5 = ImageTk.PhotoImage(resized_image)
            fifthimage.config(image=photo5)
            fifthimage.image = photo5


            first = datetime.fromtimestamp(json_data["list"][0]["dt"])
            second = datetime.fromtimestamp(json_data["list"][8]["dt"])
            third = datetime.fromtimestamp(json_data["list"][16]["dt"])
            fourth = datetime.fromtimestamp(json_data["list"][24]["dt"])
            fifth = datetime.fromtimestamp(json_data["list"][32]["dt"])
            day1.config(text=first.strftime("%A"))
            day2.config(text=second.strftime("%A"))
            day3.config(text=third.strftime("%A"))
            day4.config(text=fourth.strftime("%A"))
            day5.config(text=fifth.strftime("%A"))

            temp1d = round(json_data["list"][0]["main"]["temp_max"] - 273.15,2)
            temp1n = round(json_data["list"][0]["main"]["temp_min"] - 273.15,2)
            temp2d = round(json_data["list"][8]["main"]["temp_max"] - 273.15,2)
            temp2n = round(json_data["list"][8]["main"]["temp_min"] - 273.15,2)
            temp3d = round(json_data["list"][16]["main"]["temp_max"] - 273.15,2)
            temp3n = round(json_data["list"][16]["main"]["temp_min"] - 273.15,2)
            temp4d = round(json_data["list"][24]["main"]["temp_max"] - 273.15,2)
            temp4n = round(json_data["list"][24]["main"]["temp_min"] - 273.15,2)
            temp5d = round(json_data["list"][32]["main"]["temp_max"] - 273.15,2)
            temp5n = round(json_data["list"][32]["main"]["temp_min"] - 273.15,2)

            d1temp.config(text=str(temp1d) + "°C")
            n1temp.config(text=str(temp1n)+ "°C")
            d2temp.config(text=str(temp2d)+ "°C")
            n2temp.config(text=str(temp2n)+ "°C")
            d3temp.config(text=str(temp3d)+ "°C")
            n3temp.config(text=str(temp3n)+ "°C")
            d4temp.config(text=str(temp4d)+ "°C")
            n4temp.config(text=str(temp4n)+ "°C")
            d5temp.config(text=str(temp5d)+ "°C")
            n5temp.config(text=str(temp5n)+ "°C")
        image_icon = PhotoImage (file="Images/logo.png")
        root.iconphoto (False, image_icon)
        Round_box=PhotoImage(file="Images/Rounded Rectangle 1.png")
        Label (root, image=Round_box, bg="#57adff").place(x=30, y=110)
        #label
        label1=Label (root, text="Temperature", font=('Helvetica',11), fg="white", bg="#203243")
        label1.place(x=50, y=120)
        label2=Label (root, text="Humidity", font=('Helvetica', 11), fg="white", bg="#203243")
        label2.place(x=50,y=140)
        label3=Label (root, text="Pressure", font = ('Helvetica',11), fg="white", bg="#203243")
        label3.place(x=50, y=160)
        label4=Label (root, text="Wind Speed", font=('Helvetica',11),fg="white", bg="#203243")
        label4.place(x=50, y=180)
        label5=Label (root, text="Description", font=('Helvetica',11), fg="white", bg="#203243")
        label5.place(x=50, y=200)

        myimage=Label(height=3, width=65 ,bg="#203243")
        myimage.place(x=270, y=135)
        weat_image = PhotoImage( file="Images/Layer 7.png")
        weatherimage=Label (root, image=weat_image, bg="#203243")
        weatherimage.place(x=292, y=139)
        textfield=tk.Entry (root, justify='center',width=15, font=('poppins', 25, 'bold'), bg="#203243", border=0,fg="white")
        textfield.place (x=370, y=139)
        textfield. focus()
        Search_icon=PhotoImage(file="Images/Layer 6.png")
        myimage_icon=Button(image=Search_icon, borderwidth=0, cursor="hand2", bg="#203243", command=getWeather)
        myimage_icon.place(x=645, y=133)

        frame=Frame (root, width=900,height=180, bg="#212120")
        frame.pack(side=BOTTOM)

        clock=Label (root, font=("Helvetica", 30, 'bold'), fg="white", bg="#57adff")
        clock.place(x=30, y=20)
        #timezone
        timezone=Label (root, font = ("Helvetica", 20), fg="white", bg="#57adff")
        timezone.place(x=700, y=20)
        long_lat=Label (root, font = ("Helvetica", 10), fg="white", bg="#57adff")
        long_lat.place(x=700, y=50)

        t=Label (root,text="--", font=("Helvetica",11),fg="white",bg="#203243")
        t.place(x=150, y=120)
        h=Label(root,text="--", font=("Helvetica", 11), fg="white", bg="#203243")
        h.place(x=150, y=140)
        p=Label (root,text="--", font=("Helvetica",11), fg="white", bg="#203243")
        p.place(x=150, y=160)
        w=Label(root,text="--", font=("Helvetica",11), fg="white", bg="#203243")
        w.place (x=150, y=180)
        d=Label (root,text="--", font=("Helvetica",11),fg="white", bg="#203243")
        d.place(x=150, y=200)

        firstframe = Frame(root, width = 230, height = 132, bg = "#282829")
        firstframe.place(x=30, y=315)
        day1 = Label(firstframe,text="Saturday", font="arial 20", bg="#282829", fg="white")
        day1.place(x=100, y=5)
        firstimage = Label(firstframe, bg="#282829")
        firstimage.place(x=0, y=10)
        d1templabel = Label(firstframe,text="Day  :", font="arial 15", bg="#282829", fg="white")
        d1templabel.place(x=100, y=50)
        d1temp = Label(firstframe,text="--", bg="#282829", fg="#fff", font="ariel 15 bold")
        d1temp.place(x=160, y=50)
        n1templabel = Label(firstframe,text="Night : ", font="arial 15", bg="#282829", fg="white")
        n1templabel.place(x=100, y=80)
        n1temp = Label(firstframe,text="--", bg="#282829", fg="#fff", font="ariel 15 bold")
        n1temp.place(x=160, y=80)

        secondframe = Frame(root, width =120, height = 132, bg = "#282829")
        secondframe.place(x=300, y=315)
        day2 = Label(secondframe,text="Saturday", font="arial 15", bg="#282829", fg="white")
        day2.place(x=10, y=5)
        secondimage = Label(secondframe, bg="#282829")
        secondimage.place(x=40, y=35)
        d2templabel = Label(secondframe,text="Day  :", font="arial 10", bg="#282829", fg="white")
        d2templabel.place(x=20, y=75)
        d2temp = Label(secondframe,text="--", bg="#282829", fg="#fff", font="ariel 10")
        d2temp.place(x=60, y=75)
        n2templabel = Label(secondframe,text="Night : ", font="arial 10", bg="#282829", fg="white")
        n2templabel.place(x=20, y=100)
        n2temp = Label(secondframe,text="--", bg="#282829", fg="#fff", font="ariel 10")
        n2temp.place(x=60, y=100)

        thirdframe = Frame(root, width = 120, height = 132, bg = "#282829")
        thirdframe.place(x=456, y=315)
        day3 = Label(thirdframe,text="Saturday", font="arial 15", bg="#282829", fg="white")
        day3.place(x=10, y=5)
        thirdimage = Label(thirdframe, bg="#282829")
        thirdimage.place(x=40, y=35)
        d3templabel = Label(thirdframe,text="Day  :", font="arial 10", bg="#282829", fg="white")
        d3templabel.place(x=20, y=75)
        d3temp = Label(thirdframe,text="--", bg="#282829", fg="#fff", font="ariel 10")
        d3temp.place(x=60, y=75)
        n3templabel = Label(thirdframe,text="Night : ", font="arial 10", bg="#282829", fg="white")
        n3templabel.place(x=20, y=100)
        n3temp = Label(thirdframe,text="--", bg="#282829", fg="#fff", font="ariel 10")
        n3temp.place(x=60, y=100)

        fourthframe = Frame(root, width = 120, height = 132, bg = "#282829")
        fourthframe.place(x=600, y=315)
        day4 = Label(fourthframe,text="monday", font="arial 15", bg="#282829", fg="white")
        day4.place(x=10, y=5)
        fourthimage = Label(fourthframe, bg="#282829")
        fourthimage.place(x=40, y=35)
        d4templabel = Label(fourthframe,text="Day  :", font="arial 10", bg="#282829", fg="white")
        d4templabel.place(x=20, y=75)
        d4temp = Label(fourthframe,text="--", bg="#282829", fg="#fff", font="ariel 10")
        d4temp.place(x=60, y=75)
        n4templabel = Label(fourthframe,text="Night : ", font="arial 10", bg="#282829", fg="white")
        n4templabel.place(x=20, y=100)
        n4temp = Label(fourthframe,text="--", bg="#282829", fg="#fff", font="ariel 10")
        n4temp.place(x=60, y=100)

        fifthframe = Frame(root, width = 120, height = 132, bg = "#282829")
        fifthframe.place(x=750, y=315)
        day5 = Label(fifthframe,text="Saturday", font="arial 15", bg="#282829", fg="white")
        day5.place(x=10, y=5)
        fifthimage = Label(fifthframe, bg="#282829")
        fifthimage.place(x=40, y=35)
        d5templabel = Label(fifthframe,text="Day  :", font="arial 10", bg="#282829", fg="white")
        d5templabel.place(x=20, y=75)
        d5temp = Label(fifthframe,text="--", bg="#282829", fg="#fff", font="ariel 10")
        d5temp.place(x=60, y=75)
        n5templabel = Label(fifthframe,text="Night : ", font="arial 10", bg="#282829", fg="white")
        n5templabel.place(x=20, y=100)
        n5temp = Label(fifthframe,text="--", bg="#282829", fg="#fff", font="ariel 10")
        n5temp.place(x=60, y=100)

        root.mainloop()

title = Label(login, text="Login", font=("poppins", 40, "bold"), bg=login_bg, fg=login_text)
title.place(relx=0.5, rely=0.15, anchor=tk.CENTER)

unameLabel = Label(login, text="Username ", font=("poppins", 20), bg=login_bg, fg=login_text)
unameLabel.place(x=40, rely=0.3)
username = Entry(width=15, font=("poppins", 20), bg=login_bg2)
username.place(x=190, rely=0.3)

passwordLabel = Label(login, text="Password ", font=("poppins", 20), bg=login_bg, fg=login_text)
passwordLabel.place(x=40, rely=0.45)
password = Entry(login, width=15, font=("poppins", 20), bg=login_bg2, show="•")
password.place(x=190, rely=0.45)

loginButton = Button(login, text="Login", padx=2, pady=2, font=("poppins", 15, "bold"), command=logUser)
loginButton.place(relx=0.5, rely=0.7, anchor=tk.CENTER)

creds = Label(login, text="Designed by PyPros", pady=10, bg=login_bg, fg=login_text)
creds.pack(side="bottom")

login.mainloop()
