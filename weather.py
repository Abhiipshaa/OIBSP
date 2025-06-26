from tkinter import *
from tkinter import messagebox
import requests

API_KEY = "77fa02f74afd5df2ad37199d794004dd"

def get_weather():
    city = ask_to_enter.get()
    if not city:
        messagebox.showwarning("Input Error", "Please enter a city name.")
        return

    weather_url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"

    try:
        response = requests.get(weather_url)
        response.raise_for_status() # Raise an HTTPError for bad responses (4xx or 5xx)
        weather_data = response.json()

        if weather_data.get("cod") == "404":
            messagebox.showerror("City Not Found", f"Could not find weather data for '{city}'. Please check the city name.")
            clear_weather_display()
            return

        main_weather = weather_data['weather'][0]['main']
        description = weather_data['weather'][0]['description']
        temp = weather_data['main']['temp']
        feels_like = weather_data['main']['feels_like']
        humidity = weather_data['main']['humidity']
        wind_speed = weather_data['wind']['speed']
        display_city_name = weather_data['name'] # Get accurate city name from API

        city_display_label.config(text=f"Weather in {display_city_name}")
        temperature_label.config(text=f"Temperature: {temp}°C (Feels like: {feels_like}°C)")
        description_label.config(text=f"Description: {main_weather} ({description})")
        humidity_label.config(text=f"Humidity: {humidity}%")
        wind_label.config(text=f"Wind Speed: {wind_speed} m/s")

    except requests.exceptions.RequestException as e:
        messagebox.showerror("Connection Error", f"Could not connect to the weather API. Please check your internet connection or API key. Error: {e}")
        clear_weather_display()
    except KeyError as e:
        messagebox.showerror("Data Error", f"Unexpected data format from API. Missing key: {e}. Please try again later.")
        clear_weather_display()
    except Exception as e:
        messagebox.showerror("An Error Occurred", f"An unexpected error occurred: {e}")
        clear_weather_display()

def clear_fields():
    ask_to_enter.set("") # Clear the entry field
    clear_weather_display()

def clear_weather_display():
    city_display_label.config(text="")
    temperature_label.config(text="")
    description_label.config(text="")
    humidity_label.config(text="")
    wind_label.config(text="")

root = Tk()
root.geometry("600x500")
root.title("Weather")
root.config(bg="skyblue")

title_frame = Frame(root)
title_frame.pack(pady=10)

label1=Label(title_frame,text="Weather App",padx=8,pady=5,font=("Time New Roman" ,24 ,"bold"),borderwidth=10,relief="raised")
label1.pack()

msg = Frame(root, bg="#1A2B42")
msg.pack(pady=5, fill="x", expand=True) # ADDED fill="x" and expand=True
instruction_label = Label(msg, text="Want to know your weather ?\n no worries we've got you covered!\n Enter the name of your city\n in the box below! ",bg="#1A2B42", fg="white", font=("consolas", 12))
instruction_label.pack()

# --- Input Frame using grid ---
input_frame = Frame(root,bg="skyblue")
input_frame.pack(pady=20)

ask_to_enter = Label(input_frame, text="Enter the name of your city below:", font=("consolas", 14),borderwidth=6,bg="orange",relief="sunken")
ask_to_enter.grid(row=0, column=0, padx=5, pady=5)


ask_to_enter = StringVar()

name_entry=Entry(input_frame, textvariable=ask_to_enter, font=("comicsansms", 12))
name_entry.grid(row=1, column=0, padx=10, pady=10,sticky="n")

#buttons
btn = Button(input_frame, text="submit!",command=get_weather,
             font=("Consolas", 15, "bold"), borderwidth=5, relief="groove", bg="#9274E9")
btn.grid(row=5, column=0, columnspan=2, pady=8)

clear_btn = Button(input_frame, text="Clear", command=clear_fields,
                   font=("Calibri", 12), borderwidth=2, relief="groove", bg="white")
clear_btn.grid(row=30, column=0, columnspan=2)

# --- Weather Display Frame ---
weather_display_frame = Frame(root, bg="#E0FFFF", bd=5, relief="groove")
weather_display_frame.pack(pady=15, padx=20, fill="x", expand=True)

city_display_label = Label(weather_display_frame, text="", font=("Helvetica", 16, "bold"), bg="#E0FFFF", fg="#005C99")
city_display_label.pack(pady=5)

temperature_label = Label(weather_display_frame, text="", font=("Helvetica", 14), bg="#E0FFFF")
temperature_label.pack(pady=2)

description_label = Label(weather_display_frame, text="", font=("Helvetica", 14), bg="#E0FFFF")
description_label.pack(pady=2)

humidity_label = Label(weather_display_frame, text="", font=("Helvetica", 14), bg="#E0FFFF")
humidity_label.pack(pady=2)

wind_label = Label(weather_display_frame, text="", font=("Helvetica", 14), bg="#E0FFFF")
wind_label.pack(pady=2)

root.mainloop()