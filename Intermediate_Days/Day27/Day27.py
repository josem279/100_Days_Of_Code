############### Using Tkinter
import tkinter

window = tkinter.Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)

# Label
my_label = tkinter.Label(text="I am a label", font=("Arial", 12, "bold"))
# my_label.pack()
# my_label["text"] = "New Text"
my_label.config(text="New Text")
# my_label.place(x=100, y=0)
my_label.grid(column=0, row=0)

# Buttons
def button_click():
    print("I got clicked")
    new_text = input.get()
    my_label.config(text=new_text)

button = tkinter.Button(text="Click Me!", command=button_click)
# button.pack()
button.grid(column=1, row=1)

new_button = tkinter.Button(text="New Button")
new_button.grid(column=3, row=0)

# Entry
input = tkinter.Entry(width=10)
# input.pack()
input.grid(column=4, row=4)
print(input.get())


window.mainloop()