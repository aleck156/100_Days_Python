from tkinter import *

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title('Password Manager')
window.config(padx=20, pady=20)
window.minsize(width=200, height=200)

# ROW 0
canvas = Canvas(width=200, height=200, bg='white')
image = PhotoImage(file='./logo.png')
canvas.create_image(100, 100, image=image)
canvas.grid(column=1, row=0)

# ROW 1
website_label = Label()
website_label.config(text='Website:', justify='center')
website_label.grid(column=0, row=1)

website_URL = Entry()
website_URL.config(width=35)
website_URL.grid(column=1, columnspan=2, row=1)

# ROW 2
email_label = Label()
email_label.config(text='Email/Username:', justify='center')
email_label.grid(column=0, row=2)

email_address = Entry()
email_address.config(width=35)
email_address.grid(column=1, columnspan=2, row=2)

# ROW 3
password_label = Label()
password_label.config(text='Password:')
password_label.grid(column=0, row=3)

password_value = Entry()
password_value.config(width=21)
password_value.grid(column=1, row=3)

generate_password = Button()
generate_password.config(text='Generate Password', width=14)
generate_password.grid(column=2, row=3)
# ROW 4
add_button = Button()
add_button.config(width=36, text='Add')
add_button.grid(column=1, columnspan=2, row=4)


window.mainloop()
