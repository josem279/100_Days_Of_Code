############### Using Tkinter
from tkinter import *

window = Tk()
window.title("Miles to Km Converter")
window.config(padx=20, pady=20)
# window.minsize(width=500, height=300)

def get_km():
    miles = input.get()
    km = int(miles) * 1.609
    km_results_label.config(text=f"{km}")

label = Label(text="Is equal to:")
label.grid(column=0, row = 1)

input = Entry(width=7)
input.grid(column=1, row= 0)

miles_label = Label(text="Miles")
miles_label.grid(column=2, row=0)

km_results_label = Label(text="0")
km_results_label.grid(column=1, row=1)

km_label = Label(text="Km")
km_label.grid(column=2, row=1)

button = Button(text="Calculate", command=get_km)
button.grid(column=1, row=2)

window.mainloop()