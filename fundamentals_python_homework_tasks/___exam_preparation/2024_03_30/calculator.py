import tkinter as tk

def button_click(symbol):
    current = result_label["text"]
    if current == "0":
        result_label["text"] = symbol
    else:
        result_label["text"] += symbol

def clear():
    result_label["text"] = "0"

def calculate():
    try:
        result_label["text"] = str(eval(result_label["text"]))
    except:
        result_label["text"] = "Error"

# Create the main window
root = tk.Tk()
root.title("Калкулатор")

# Create the result label
result_label = tk.Label(root, text="0", width=20, borderwidth=5, relief="sunken")
result_label.grid(row=0, column=0, columnspan=4)

# Define button symbols
buttons = [
    "7", "8", "9", "/",
    "4", "5", "6", "*",
    "1", "2", "3", "-",
    "0", ".", "=", "+"
]

# Create buttons
for i, symbol in enumerate(buttons):
    row = i // 4 + 1
    col = i % 4
    if symbol == "=":
        tk.Button(root, text=symbol, width=5, command=calculate).grid(row=row+4, column=col)
    elif symbol == ".":
        tk.Button(root, text=symbol, width=5, command=lambda s=symbol: button_click(s)).grid(row=row+3, column=col+1)
    elif symbol == "0":
        tk.Button(root, text=symbol, width=11, command=lambda s=symbol: button_click(s)).grid(row=row+3, column=col, columnspan=2)
    else:
        tk.Button(root, text=symbol, width=5, command=lambda s=symbol: button_click(s)).grid(row=row+3, column=col)

# Clear button
tk.Button(root, text="C", width=5, command=clear).grid(row=row+4, column=3)

root.mainloop()
