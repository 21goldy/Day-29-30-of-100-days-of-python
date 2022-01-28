from tkinter import messagebox
from tkinter import *
import random
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

random_letters = random.randint(1, 10)
random_numbers = random.randint(1, 10)
random_symbols = random.randint(1, 10)


def password_generator():
    pass_list = []
    for char in range(1, random_letters + 1):
        pass_list += random.choice(letters)

    for symbol in range(1, random_symbols + 1):
        pass_list += random.choice(symbols)

    for num in range(1, random_numbers + 1):
        pass_list += random.choice(numbers)

    random.shuffle(pass_list)
    generated_password = "".join(pass_list)
    input_password.delete(0, END)
    input_password.insert(0, string=generated_password)


# ---------------------------- CLEAR FIELDS ------------------------------- #
def clear_fields():
    input_website.delete(0, END)
    input_mail_username.delete(0, END)
    input_password.delete(0, END)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    a = input_website.get()
    b = input_mail_username.get()
    c = input_password.get()
    new_data = {
        a: {
            "Email/Username": b,
            "Password": c,
        }
    }

    # checking if any of the fields are left empty
    if a == "" or b == "" or c == "":
        messagebox.showinfo(title="Error", message="'Fields cannot be left empty!'")

    else:
        # checks if json file present and adds new data
        try:
            with open("Passwords.json", mode="r") as data:
                loaded_data = json.load(data)
                loaded_data.update(new_data)

            with open("Passwords.json", mode="w") as data:
                json.dump(loaded_data, data, indent=4)
                clear_fields()

        # tackles the Expecting Value Error
        except json.decoder.JSONDecodeError:
            pass

        # creates a new json file with the name "Passwords.json"
        finally:
            with open("Passwords.json", mode="w") as data:
                json.dump(new_data, data, indent=4)
                clear_fields()


# ---------------------------- SEARCH ------------------------------- #

def search():
    website_name = input_website.get()
    try:
        with open("Passwords.json", mode="r") as data:
            loaded_data = json.load(data)
            my_web_info = (loaded_data[website_name])
            email = my_web_info['Email/Username']
            password = my_web_info['Password']
            messagebox.showinfo(title="My web info", message=f"Email/Username: {email}\nPassword: {password}")

    except KeyError or json.decoder.JSONDecodeError:
        messagebox.showinfo(title="Error", message="No such website exist in data!")


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)

# canvas setup

canvas = Canvas(width=200, height=200)
logo = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo)
canvas.grid(row=0, column=1)

# ------------------------------ LABELS -------------------------------------------#

# website label

website_label = Label(text="Website: ", font=("Courier", 15))
website_label.grid()
website_label.config(pady=20)

# mail label

mail_label = Label(text="Email/Username: ", font=("Courier", 15))
mail_label.grid()
mail_label.config(pady=20)

# password label

password_label = Label(text="Password: ", font=("Courier", 15))
password_label.grid()
password_label.config(pady=20)

# ------------------------------ ENTRIES -------------------------------------------#

# website entry

input_website = Entry(width=23, font="Courier")
input_website.grid(row=1, column=1, columnspan=2)
input_website.focus()
input_website.insert(0, string="Website name")

# email/username entry

input_mail_username = Entry(width=40, font="Courier")
input_mail_username.grid(row=2, column=1, columnspan=5)
input_mail_username.focus()
input_mail_username.insert(0, string="xyz@gmail.com")

# password entry

input_password = Entry(width=23, font="Courier")
input_password.focus()
input_password.insert(0, string="Enter password")
input_password.grid(row=3, column=1, columnspan=1)

# ------------------------------ BUTTONS -------------------------------------------#

# generate password button

Generate_pass_button = Button(text="Generate New", font=("Courier", 13), command=password_generator)
Generate_pass_button.grid(row=3, column=3)
Generate_pass_button.config(width=13)

# add button

add_button = Button(text="Add+", font=("Courier", 13), command=save)
add_button.grid(row=4, column=1, columnspan=5)
add_button.config(width=41)

# search button

search_button = Button(text="Search", font=("Courier", 13), command=search)
search_button.grid(row=1, column=3)
search_button.config(width=13)

# keeps the window on

window.mainloop()

# ------------------------------ END OF THE PROGRAM -------------------------------------------#
