from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def password_generator():

    password_entry.delete(0, END)
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    new_letter = [choice(letters) for _ in range(randint(8, 10))]

    new_symbol = [choice(symbols) for _ in range(randint(2, 4))]

    new_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = new_symbol + new_numbers + new_letter
    shuffle(password_list)

    password = "".join(password_list)

    password_entry.insert(0, f"{password}")

    pyperclip.copy(password)
# ---------------------------- SAVE PASSWORD ------------------------------- #


def save():

    website = website_entry.get()
    email = mail_entry.get()
    password = password_entry.get()

    new_data = {
        website: {
            "email": email,
            "password": password
        }
    }

    if website == "" or password == "" or email == "":
        messagebox.showwarning(title="Oops", message="Please don't leave any empty fields!")

    else:
        try:
            with open("data.json", "r") as file:
                data = json.load(file)
                data.update(new_data)
        except FileNotFoundError:
            with open("data.json", "w") as file:
                json.dump(new_data, file, indent=4)
        else:
            data.update(new_data)
            with open("data.json", "w") as file:
                json.dump(data, file, indent=4)
        finally:
            website_entry.delete(0, END)
            password_entry.delete(0, END)


def find_password():

    website = website_entry.get()

    if website == "":
        messagebox.showwarning(title="Oops", message="Please, Enter the website that you want to search!")

    else:
        try:
            with open("data.json") as file:
                find_data = json.load(file)
        except FileNotFoundError:
            messagebox.showinfo(title="Alert", message="No records found")
        else:
            if website in find_data:
                email = find_data[website]["email"]
                password = find_data[website]["password"]
                messagebox.showinfo(title=website, message=f"E-mail: {email}\nPassword: {password}")
            else:
                messagebox.showinfo(title="Alert", message="No records found")


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)

canvas = Canvas(width=200, height=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0)


website_label = Label(text="Website:")
website_label.grid(column=0, row=1)

mail_label = Label(text="E-mail/Username:")
mail_label.grid(column=0, row=2)

password_label = Label(text="Password:")
password_label.grid(column=0, row=3)


generate_button = Button(text="Generate Password", command=password_generator)
generate_button.grid(column=2, row=3)

add_button = Button(text="Add", width=44)
add_button.config(command=save)
add_button.grid(column=1, row=4, columnspan=2)

search_button = Button(text="Search", width=15, command=find_password)
search_button.grid(column=2, row=1)


website_entry = Entry(width=33)
website_entry.focus()
website_entry.grid(column=1, row=1)

mail_entry = Entry(width=52)
mail_entry.insert(0, "karthi.sk1467@gmail.com")
mail_entry.grid(column=1, row=2, columnspan=2)

password_entry = Entry(width=33)
password_entry.grid(column=1, row=3)


window.mainloop()
