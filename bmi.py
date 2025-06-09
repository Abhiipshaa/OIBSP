from tkinter import *

def getVals():
    try:
        height_cm = float(HeightValue.get())
        weight_kg = float(WeightValue.get())

        # Convert height to meters
        height_m = height_cm / 100

        # Calculate BMI
        bmi_raw = weight_kg / (height_m ** 2)
        bmi = round(bmi_raw, 2)  # rounded for display only

        # Display BMI result in the label using unrounded value for logic
        if bmi_raw < 18.5:
            message = "Underweight (BMI < 18.5):\nYou need to gain some weight — fuel your body with nutritious foods and build strength!"
        elif 18.5 <= bmi_raw <= 24.9:
            message = "Normal (BMI 18.5–24.9):\nYou're at a healthy weight — keep up the great work and stay active!"
        elif 25.0 <= bmi_raw <= 29.9:
            message = "Overweight (BMI 25–29.9):\nYou're close to your ideal weight — a little more movement and smart eating will get you there!"
        elif 30.0 <= bmi_raw <= 34.9:
            message = "Obesity Class I (BMI 30–34.9):\nTime to take charge — small, steady changes can boost your energy and health!"
        elif 35.0 <= bmi_raw <= 39.9:
            message = "Obesity Class II (BMI 35–39.9):\nYou've got this! Focus on daily habits that bring you closer to your healthiest self."
        else:
            message = "Obesity Class III (BMI 40+):\nYour journey starts now — every step you take brings you closer to feeling stronger and better!"

        result_label.config(text=f"Your BMI is: {bmi}\n{message}")

        # Write to file
        with open("records.txt", "a") as f:
            f.write(f"Height: {height_cm} cm, Weight: {weight_kg} kg, BMI: {bmi}\n")

    except ValueError:
        result_label.config(text="Please enter valid numbers.")


def clear_fields():
    HeightValue.set("")
    WeightValue.set("")
    result_label.config(text="")

root = Tk()

# Window settings
root.geometry("650x500")
root.minsize(640, 400)
root.maxsize(1000, 988)
root.title("Calculator")

# --- Label Frame using pack ---
title_frame = Frame(root)
title_frame.pack(pady=10)

bmi = Label(title_frame, text="BMI CALCULATOR", bg="Green", fg="white",
            padx=15, pady=5, font=("calibri", 19, "bold"),
            borderwidth=8, relief=GROOVE)
bmi.pack()

# --- Input Frame using grid ---
input_frame = Frame(root)
input_frame.pack(pady=20)

Height = Label(input_frame, text="Height (cm)", font=("calibri", 14))
Weight = Label(input_frame, text="Weight (kg)", font=("calibri", 14))
Height.grid(row=0, column=0, padx=10, pady=10)
Weight.grid(row=1, column=0, padx=10, pady=10)

HeightValue = StringVar()
WeightValue = StringVar()

Heightentry = Entry(input_frame, textvariable=HeightValue, font=("comicsansms", 12))
Weightentry = Entry(input_frame, textvariable=WeightValue, font=("comicsansms", 12))

Heightentry.grid(row=0, column=1, padx=10, pady=10)
Weightentry.grid(row=1, column=1, padx=10, pady=10)

btn = Button(input_frame, text="Calculate my BMI", command=getVals,
             font=("Calibri", 15, "bold"), borderwidth=5, relief="solid", bg="skyblue")
btn.grid(row=14, column=0, columnspan=2, pady=10)

clear_btn = Button(input_frame, text="Clear", command=clear_fields,
                   font=("Calibri", 12), borderwidth=2, relief="groove", bg="white")
clear_btn.grid(row=20, column=0, columnspan=2)

# --- Result Label ---
result_label = Label(root, text="Result :\n", font=("calibri", 16), fg="black", padx=10, pady=10, borderwidth=5, relief="ridge")
result_label.pack(pady=10)

root.mainloop()

