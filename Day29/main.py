import json
from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
#Password Generator Project
def create_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(0, randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(0, randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(0, randint(2, 4))]
    password_list = password_letters + password_symbols + password_numbers

    shuffle(password_list)

    password = "".join(password_list)

    print(f"Your new password is: {password}")
    if password_value.get():
        password_value.delete(0, 'end')
    password_value.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #

def save_data():
    url = website_URL.get()
    email = email_address.get()
    password = password_value.get()

    new_data = {url: {
        'email': email,
        'Password': password
        }
    }

    if len(url) == 0 or len(email)==0 or len(password)==0:
        messagebox.showinfo(title='Missing fields',message='You\'ve left some fields empty!')
        return

    with open('./user_data.json', mode='w') as file:
        json.dump(fp=file,  obj=new_data)

    website_URL.delete(0, 'end')
    email_address.delete(0, 'end')
    password_value.delete(0, 'end')
    website_URL.focus()


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
generate_password.config(text='Generate Password', command=create_password)
generate_password.grid(column=2, row=3)
# ROW 4
add_button = Button(width=52)
add_button.config(text='Add', command=save_data)
add_button.grid(column=1, columnspan=2, row=4)


window.mainloop()
