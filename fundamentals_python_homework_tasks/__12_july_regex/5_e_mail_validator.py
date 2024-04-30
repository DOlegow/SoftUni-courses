import re
import tkinter as tk

def validate_email():
    email = entry_email.get()

    if "@" not in email:
        result = "Invalid email: Missing '@'."
    elif "." not in email:
        result = "Invalid email. Missing ','."
    else:
        pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z'
root = tk.Tk()
root.geometry("500x500")  # Window size
root.title('Email Validator')

label_instructions = tk.label(root, text="Enter an e-mail adress. It should include '@' and '.domain.")
label_instruction.pack()
entry.email.delete(0, tk.END)  # Clear field

button_validate = tk.Button(root. text="Validate Email")