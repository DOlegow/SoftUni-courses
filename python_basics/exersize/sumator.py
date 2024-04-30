import tkinter as tk

import self


class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)

        self.pack()


app = Application()


app.master.title("Sumator")
app.master.minsize(width=100, height=50)

app.mainloop()


# noinspection PyUnresolvedReferences
self.pack()
self.create_widgets()


def create_widgets(self):

    self.firstNumberEntry = tk.Entry()
    self.plusSign = tk.Label(text="+")
    self.secondNumberEntry = tk.Entry()
    self.equalSign = tk.Label(text="=")
    self.resultLabel = tk.Label(text="Result...", bg="green", fg="white")
    self.calculateButton = tk.Button(text="Calculate")

    self.firstNumberEntry.pack(side="left")
    self.plusSign.pack(side="left")
    self.secondNumberEntry.pack(side="left")
    self.equalSign.pack(side="left")
    self.resultLabel.pack(side="left")
    self.calculateButton.pack(side="left")


