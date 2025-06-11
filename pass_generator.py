from tkinter import *
import random
import string
from tkinter import messagebox

# --- Color Palette (Defined early for use throughout) ---
COLOR_DARK_BLUE = "#1A2B42"
COLOR_ACCENT_GREEN = "#4CAF50"
COLOR_TEXT_LIGHT = "white"
COLOR_TEXT_DARK = "#333333"
COLOR_LIGHT_GREY_BG = "#EEEEEE"
COLOR_BLACK = "black"
COLOR_FRAME_BG = "#333333"

# --- Function Definitions (MUST be defined before they are used by widgets) ---

# Global variables for Checkbutton states and output display (need to be defined before the function uses them)
# These will be initialized as Tkinter variables (IntVar, StringVar) after Tk() is created.
# We declare them here so the function knows they exist, but their actual Tkinter creation is below.
num_of_char_entry_var = None
include_symbols = None
include_digits = None
include_letters = None
generated_password_var = None


def generate_password():
    try:
        length = int(num_of_char_entry_var.get())
        if length <= 0:
            messagebox.showerror("Invalid Input", "Password length must be a positive number.")
            return
        if length < 8:
            messagebox.showwarning("Weak Password", "For optimal security, a minimum of 8 characters is recommended.")
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid number for password length.")
        return

    if not (include_symbols.get() or include_digits.get() or include_letters.get()):
        messagebox.showwarning("No Character Types Selected",
                               "Please select at least one character type (symbols, digits, letters) to include in your password.")
        return

    character_pool = ""
    if include_symbols.get():
        character_pool += string.punctuation
    if include_digits.get():
        character_pool += string.digits
    if include_letters.get():
        character_pool += string.ascii_lowercase + string.ascii_uppercase

    if not character_pool:
        messagebox.showerror("Error", "No characters available to generate password. Check your selections.")
        return

    password = ''.join(random.choice(character_pool) for _ in range(length))
    generated_password_var.set(password)


# --- Main Tkinter Window Setup ---
root = Tk()
root.geometry("650x600")
root.minsize(640, 400)
root.maxsize(1000, 988)

root.title("pass_generator")
root.config(bg="#1A2B42")

# --- UI Element Definitions (using the Tk() instance) ---

# Title Frame
title_frame = Frame(root, bg="darkblue")
title_frame.pack(pady=10)

password_label = Label(title_frame, text="PASSWORD GENERATOR", bg="black", fg="white",padx=15, pady=5, font=("consolas", 19, "bold"),borderwidth=8, relief=GROOVE)
password_label.pack()

# Instructions Frame
instruction_frame = Frame(root, bg="#1A2B42") # Renamed from title2 for clarity
instruction_frame.pack(pady=5)
instruction_label = Label(instruction_frame, text="i)For optimal security, it is highly recommended\nthat your password consists of a minimum of eight characters.\n\nii)To significantly enhance password strength,\n please include a combination of digits, special characters, and symbols.\n\niii)You have full control to customize your password\n by selecting the specific character types you wish to include.", bg="#1A2B42", fg="white", font=("calibri", 12))
instruction_label.pack()

# Input Frame for character entry and checkboxes
input_frame = Frame(root, bg=COLOR_FRAME_BG, padx=20, pady=15, relief=RIDGE, borderwidth=3)
input_frame.pack(pady=15, padx=20, fill=X)

# --- Declare Tkinter Variables (now that root = Tk() is created) ---
num_of_char_entry_var = StringVar()
include_symbols = IntVar()
include_digits = IntVar()
include_letters = IntVar()
generated_password_var = StringVar()
generated_password_var.set("Your password will appear here.") # Initial placeholder text

# --- Widgets using the declared variables ---

# Number of characters input field
num_of_char_label = Label(input_frame, text="Enter the number of characters:", font=("consolas", 14), bg=COLOR_FRAME_BG, fg="WHITE")
num_of_char_label.grid(row=0, column=0, padx=5, pady=5, sticky="w")

num_of_char_entry = Entry(input_frame, textvariable=num_of_char_entry_var, width=10, font=("consolas", 14))
num_of_char_entry.grid(row=0, column=1, padx=5, pady=5, sticky="e")

# Define the list of checkbox options
checkbox_options = [
    ("Do you want to include special characters in your password?", include_symbols),
    ("Do you want to include digits in your password?", include_digits),
    ("Do you want to include letters (a-z, A-Z) in your password?", include_letters)
]

# Loop to place checkboxes correctly
for i, (text, var) in enumerate(checkbox_options):
    chk = Checkbutton(input_frame,
                      text=text,
                      variable=var,
                      bg=COLOR_FRAME_BG,
                      fg="white",
                      font=("calibri", 12),
                      selectcolor=COLOR_DARK_BLUE,
                      activebackground=COLOR_FRAME_BG, activeforeground="white",
                      relief=FLAT
                      )
    chk.grid(row=i + 1, column=0, columnspan=2, padx=5, pady=5, sticky="w")


# Submit button
submit_button_row = len(checkbox_options) + 1
submit_button = Button(input_frame, text="Submit to create your password!",
                       font=("roboto", 15, "bold"), bg="darkgreen", fg="white",
                       command=generate_password) # NOW generate_password is defined!
submit_button.grid(row=submit_button_row, column=0, columnspan=2, pady=25)


# Output Display Label
password_display_label_row = submit_button_row + 1
password_display_label = Label(input_frame, textvariable=generated_password_var,
                               font=("Consolas", 16, "bold"), bg="#EEEEEE", fg="#333333",
                               wraplength=450, justify=CENTER, relief=SUNKEN, borderwidth=2, padx=10, pady=10)
password_display_label.grid(row=password_display_label_row, column=0, columnspan=2, pady=(20, 0), sticky="ew")


root.mainloop()