from tkinter import *
import tkinter.messagebox
from random import choice, randint, shuffle
import json
import os
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def password_generator():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
    
    password_letters = [choice(letters) for char in range(randint(8, 10))]
    password_symbols = [choice(symbols) for char in range(randint(2, 4))]
    password_numbers = [choice(numbers) for char in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers

    shuffle(password_list)

    password = "".join(password_list)


    pw_entry.delete(0, END)
    pw_entry.insert(0, password)
# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = web_entry.get()
    email = email_entry.get()
    password = pw_entry.get()
    new_data = {
        website :{
            'email': email,
            'password':password
        }
    }

    try:
        with open('data.json', 'r') as f:
            data = json.load(f)
    except FileNotFoundError:
        with open('data.json', 'w') as f:
            json.dump(new_data, f, indent=4)
            tkinter.messagebox.showinfo("Confirmation", message="Password has been saved!") 
    else:
        data.update(new_data)
        with open('data.json', 'w') as f:
            json.dump(data, f, indent=4)
            tkinter.messagebox.showinfo("Confirmation", message="Password added!")
    finally:
        web_entry.delete(0,'end')
        pw_entry.delete(0,'end')

# ---------------------------- SEARCH PASSWORD ------------------------------- #
def search_password():
    website = web_entry.get()
    try:
        with open('data.json', 'r') as db:
            data = json.load(db)
    except FileNotFoundError:
        tkinter.messagebox.showinfo(message="File Not Found")
    else:
        if website in data:    
            email = data[website]['email']
            pw = data[website]['password']
            tkinter.messagebox.showinfo("Confirmation", message=f"Password: {pw}\nEmail: {email}")
        else:
            tkinter.messagebox.showinfo("Confirmation", message=f"No password for: {website}")
        
# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.config(padx=50, pady=50)
window.title('Password Manager')

canvas = Canvas(width=200, height=200)
image = PhotoImage(file= 'logo.png')
canvas.create_image(100, 100, image = image)
canvas.grid(row=0, column=1)

# Labels
website_label = Label(text="Website:")
website_label.grid(row=1, column=0)

email_label = Label(text="Email/Username:")
email_label.grid(row=2, column=0)
pw_label = Label(text="Password:")
pw_label.grid(row=3, column=0)

# Entries
web_entry = Entry(width=35)
web_entry.grid(row=1, column=1, columnspan=2)
web_entry.focus()
email_entry = Entry(width=35)
email_entry.insert(0, 'ozairmohammad12@gmail.com')
email_entry.grid(row=2, column=1, columnspan=2)
pw_entry = Entry(width=30)
pw_entry.grid(row=3, column=1)

# Buttons
generate_pw = Button(text="Generate Password", command= password_generator)
generate_pw.grid(row=3, column=2)
add = Button(text="Add", width=36, command=save)
add.grid(row=4, column=1, columnspan=2)
search = Button(text="Search", command=search_password)
search.grid(row =1 , column=3)


window.mainloop()