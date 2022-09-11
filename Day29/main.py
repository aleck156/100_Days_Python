from tkinter import *

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

def save_data():
    url = website_URL.get()
    email = email_address.get()
    password = password_value.get()
    print(f'{url} / {email} / {password}')

    with open('./user_data.txt', mode='a') as file:
        file.write(f'{url} | {email} | {password}\n')

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title('Password Manager')
window.config(padx=20, pady=20, bg='black')

# ROW 0
canvas = Canvas(width=200, height=200, bg='black', highlightthickness=0)
image = PhotoImage(file='./logo.png')
canvas.create_image(100, 100, image=image)
canvas.grid(column=0, row=0,columnspan=3)

# ROW 1
website_label = Label()
website_label.config(text='Website:', justify='center', bg='BLACK', fg='GRAY')
website_label.grid(column=0, row=1)

website_URL = Entry(width=55)
website_URL.config()
website_URL.focus()
website_URL.grid(column=1, columnspan=2, row=1, sticky='w')

# ROW 2
email_label = Label()
email_label.config(text='Email/Username:', justify='center', bg='BLACK', fg='GRAY')
email_label.grid(column=0, row=2)

email_address = Entry(width=55)
email_address.config()
email_address.insert(0, 'your_email@address.com')
email_address.grid(column=1, columnspan=2, row=2, sticky='w')

# ROW 3
password_label = Label()
password_label.config(text='Password:', bg='BLACK', fg='GRAY')
password_label.grid(column=0, row=3)

password_value = Entry(width=30)
password_value.config()
password_value.grid(column=1, row=3, sticky='w')

generate_password = Button(width=20)
generate_password.config(text='Generate Password')
generate_password.grid(column=2, row=3)
# ROW 4
add_button = Button(width=52)
add_button.config(text='Add', command=save_data)
add_button.grid(column=1, columnspan=2, row=4)


window.mainloop()
