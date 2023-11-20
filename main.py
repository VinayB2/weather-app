from tkinter import *
import tkinter as tk
from tkinter import ttk, messagebox
import requests

# Colors
login_bg = "#fff"
login_bg2 = "#ececec"

dashboard_bg = "#fff"

login = Tk()
login.title("Login Window")
login.geometry("500x400+500+200")
login.resizable(False, False)
login.config(bg=login_bg)

def logUser():
    user = username.get()
    pwd = password.get()
    if user != "" or pwd != "":
        messagebox.showwarning("Login Error", "Invalid username or password")
        username.delete(0, tk.END)
        password.delete(0, tk.END)
    else:
        login.destroy()
        root = Tk()
        root.title("Weather App")
        root.geometry("900x500+300+200")
        root.resizable(False, False)
        root.config(bg=dashboard_bg)

        def getWeather():
            city = textfield.get()
            api = "https://api.openweathermap.org/data/2.5/weather?q="+city+"&appid=f733af53d79626f7924e4e19640924cb"
            json_data = requests.get(api).json()
            if json_data['cod'] != 200:
                messagebox.showerror("Error", "Location does not exist!")
                return

            condition_data = json_data['weather'][0]['main']
            description_data = json_data['weather'][0]['description']
            temp_data = int(json_data['main']['temp'] - 273.15)
            pressure_data = json_data['main']['pressure']
            humidity_data = json_data['main']['humidity']
            wind_speed_data = json_data['wind']["speed"]
        
            cityWdg.config(text=city)
            temp.config(text=str(temp_data) + "°")
            condition.config(text=condition_data + " | Feels Like " + str(temp) + "°")
            wind.config(text=str(wind_speed_data))
            humidity.config(text=str(humidity_data) + "%")
            description.config(text=description_data)
            pressure.config(text=str(pressure_data))

        # Search Area

        textfield = Entry(justify="center", width=17, font=("poppins", 25, "bold"), bg="#cdcdcd", border=0, fg="black")
        textfield.place(relx=0.5, rely=0.1, anchor=tk.CENTER)
        textfield.focus()

        search = Button(text="Fetch", font=("cursive", 10, "bold"), height=1, width=6, cursor="hand2", padx=5, pady=5,
                        bg="#b0adb8", fg="#170056", command=getWeather)
        search.place(relx=0.5, rely=0.2, anchor=tk.CENTER)

        # Middle Left box

        name = Label(text="Current Weather", font=("cursive", 15, "bold"), fg="#ee666d", bg=dashboard_bg)
        name.place(x=130, y=200)
        cityWdg = Label(text="---",font=("cursive", 15), fg="#ee666d", bg=dashboard_bg)
        cityWdg.place(x=130, y=230)

        # Middle right box

        temp = Label(text="---", font=("arial", 70, "bold"), fg="#ee666d", bg=dashboard_bg)
        temp.place(x=550, y=150)
        condition = Label(text="---", font=("arial", 15, 'bold'), bg=dashboard_bg)
        condition.place(x=550, y=250)

        # Bottom most two rows
        # Upper Row
        label1 = Label(text="WIND", font=("Helvetica", 15, 'bold'), fg="black", bg=dashboard_bg)
        label1.place(x=120, y=350)
        label2 = Label(text="HUMIDITY", font=("Helvetica", 15, 'bold'), fg="black", bg=dashboard_bg)
        label2.place(x=250, y=350)
        label3 = Label(text="DESCRIPTION", font=("Helvetica", 15, 'bold'), fg="black", bg=dashboard_bg)
        label3.place(x=430, y=350)
        label4 = Label(text="PRESSURE", font=("Helvetica", 15, 'bold'), fg="black", bg=dashboard_bg)
        label4.place(x=650, y=350)

        # Bottom row
        wind = Label(text="...", font=("arial", 20, "bold"), bg=dashboard_bg)
        wind.place(x=120, y=400)
        humidity = Label(text="...", font=("arial", 20, "bold"), bg=dashboard_bg)
        humidity.place(x=280, y=400)
        description = Label(text="...", font=("arial", 15, "bold"), bg=dashboard_bg)
        description.place(x=450, y=400)
        pressure = Label(text="...", font=("arial", 20, "bold"), bg=dashboard_bg)
        pressure.place(x=670, y=400)

        root.mainloop()

title = Label(login, text="Login", font=("poppins", 40, "bold"), bg=login_bg)
title.place(relx=0.5, rely=0.15, anchor=tk.CENTER)

unameLabel = Label(login, text="Username ", font=("poppins", 20), bg=login_bg)
unameLabel.place(x=40, rely=0.3)
username = Entry(width=15, font=("poppins", 20), bg=login_bg2)
username.place(x=190, rely=0.3)

passwordLabel = Label(login, text="Password ", font=("poppins", 20), bg=login_bg)
passwordLabel.place(x=40, rely=0.45)
password = Entry(login, width=15, font=("poppins", 20), bg=login_bg2, show="*")
password.place(x=190, rely=0.45)

loginButton = Button(login, text="Login", padx=2, pady=2, font=("poppins", 15, "bold"), command=logUser)
loginButton.place(relx=0.5, rely=0.7, anchor=tk.CENTER)

creds = Label(login, text="Designed by PyPros", pady=10, bg=login_bg)
creds.pack(side="bottom")

login.mainloop()
