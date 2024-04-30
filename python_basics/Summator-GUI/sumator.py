import tkinter as tk


class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)

        self.pack()
        self.create_widgets()

    def create_widgets(self):
        # create widgets
        self.firstNumberEntry = tk.Entry()
        self.minusSign = tk.Label(text="-")
        self.secondNumberEntry = tk.Entry()
        self.equalSign = tk.Label(text="=")
        self.resultLabel = tk.Label(text="Result...", bg="yellow", fg="white")
        self.calculateButton = tk.Button(text="Сметни", command=self.calculate)

        # place widgets
        self.firstNumberEntry.pack(side="left")
        self.minusSign.pack(side="left")
        self.secondNumberEntry.pack(side="left")
        self.equalSign.pack(side="left")
        self.resultLabel.pack(side="left")
        self.calculateButton.pack(side="left")


    def calculate(self):
        try:
            first_value = float(self.firstNumberEntry.get())
            second_value = float(self.secondNumberEntry.get())
            result = first_value - second_value
            self.resultLabel.config(text=str(result), bg="green", fg="black")
        except ValueError:
            self.resultLabel.config(text="Не е число/числа.", bg="red", fg="black")


    # create the application

app = Application()
app.master.title("Изваждане на две числа")
app.master.minsize(width=400, height=50)

# start the program
app.mainloop()





