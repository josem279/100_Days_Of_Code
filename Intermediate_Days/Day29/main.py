from tkinter import *
from tkinter import messagebox
import random
import pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def generate_password():
    #Password Generator Project
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [random.choice(letters) for _ in range(random.randint(8, 10))]
    password_symbols = [random.choice(symbols) for _ in range(random.randint(2, 4))]
    password_numbers = [random.choice(numbers) for _ in range(random.randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    random.shuffle(password_list)

    password = "".join(password_list)

    pw_text.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #

def save():
    
    website = website_text.get()
    email = email_text.get()
    password = pw_text.get()
    
    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Please make sure you haven't left any field empty.")
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered:\Email: {email}" f"\nPassword: {password} \nIs it ok to save?")
        
        if is_ok:
            with open('data.txt', 'a') as data_file:
                data_file.write(f"{website} | {email} | {password}")
                website_text.delete(0, END)
                pw_text.delete(0, END)
        

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
lock_image = PhotoImage(file=r"Intermediate_Days\Day29\logo.png")
canvas.create_image(100, 100, image=lock_image)
canvas.grid(row=0, column=1)

# Labels
website_label = Label(text="Website")
website_label.grid(row=1, column=0)
email_user_label = Label(text="Email/Username:")
email_user_label.grid(row=2, column=0)
pw_label = Label(text="Password:")
pw_label.grid(row=3, column=0)

# Entries
website_text = Entry(width=35)
website_text.grid(row=1, column=1, columnspan=2, sticky="W")
website_text.focus()

email_text = Entry(width=35)
email_text.grid(row=2, column=1, columnspan=2, sticky="W")
email_text.insert(0, "johnsmith@email.com")

pw_text = Entry(width=21)
pw_text.grid(row=3, column=1, sticky="W")

# buttons 
add_button = Button(text="Add", width=36, command=save)
add_button.grid(row=4, column=1, columnspan=2, sticky="W")

gen_button = Button(text="Generate Password", command=generate_password)
gen_button.grid(row=3, column=2, columnspan=2)

window.mainloop()