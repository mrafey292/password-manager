from tkinter import *
from tkinter import messagebox
from random import randint, choice, shuffle
import pyperclip
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for char in range(randint(8, 10))]
    password_symbols = [choice(symbols) for symbol in range(randint(2, 4))]
    password_numbers = [choice(numbers) for number in range(randint(2, 4))]

    password_list = password_numbers + password_symbols + password_letters
    shuffle(password_list)

    password = "".join(password_list)
    password_input.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #


def save():
    website = web_input.get()
    email = email_input.get()
    password = password_input.get()
    new_data = {
        website: {
            "email": email,
            "password": password,
        }
    }

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Please don't leave any of the fields empty.")
    else:
        try:
            with open("data.json", "r") as f:
                data = json.load(f)
        except FileNotFoundError:
            with open("data.json", "w") as f:
                json.dump(new_data, f, indent=4)
        else:
            with open("data.json", "w") as f:
                data.update(new_data)
                json.dump(data, f, indent=4)
        finally:
            web_input.delete(0, END)
            password_input.delete(0, END)


# ---------------------------------- FIND PASSWORD ------------------------------------- #


def find_password():
    website = web_input.get()
    try:
        with open("data.json", "r") as f:
            data = json.load(f)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No Data File Found. ")
    else:
        if website in data:
            web_data = data[website]
            email = web_data["email"]
            password = web_data["password"]
            messagebox.showinfo(title="Website Details", message=f"Email: {email}\nPassword: {password}")
        else:
            messagebox.showinfo(title="Error", message="No details for the website exist.")


# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

# IMAGE

canvas = Canvas(width=200, height=200)
logo_img = PhotoImage(file="C:/usb/old-code/PycharmProjects/python/password-manager/logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=2, row=1)

# LABELS

website_label = Label(text="Website: ")
website_label.grid(column=1, row=2)

email_label = Label(text="Email/Username: ")
email_label.grid(column=1, row=3)

password_label = Label(text="Password: ")
password_label.grid(column=1, row=4)

# INPUTS

web_input = Entry(width=27)
web_input.grid(column=2, row=2, columnspan=1)
web_input.focus()

email_input = Entry(width=45)
email_input.grid(column=2, row=3, columnspan=2)
email_input.insert(0, "mrafey292@gmail.com")

password_input = Entry(width=27)
password_input.grid(column=2, row=4)

# BUTTONS

pass_gen = Button(text="Generate Password", command=generate_password)
pass_gen.grid(column=3, row=4)

add_pass = Button(text="Add", width=38, command=save)
add_pass.grid(column=2, row=5, columnspan=2)

search = Button(text="Search", width=14, command=find_password)
search.grid(column=3, row=2)

window.mainloop()
