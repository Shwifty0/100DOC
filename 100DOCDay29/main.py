from tkinter import *

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

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
emailun_label = Label(text="Email/Username:")
emailun_label.grid(row=2, column=0)
pw_label = Label(text="Password:")
pw_label.grid(row=3, column=0)

# Entries
web_entry = Entry(width=35)
web_entry.grid(row=1, column=1, columnspan=2)
email_entry = Entry(width=35)
email_entry.grid(row=2, column=1, columnspan=2)
pw_entry = Entry(width=21)
pw_entry.grid(row=3, column=1, columnspan=2)

# Buttons
generate_pw = Button(text="Generate Password")
generate_pw.grid(row=3, column=2)
add = Button(text="Add", width=36)
add.grid(row=4, column=1, columnspan=2)




window.mainloop()