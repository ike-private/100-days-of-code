from tkinter import *
from tkinter import messagebox
from random import *
import pyperclip
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
# Password Generator Project

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

def generate_password():
    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    password = "".join(password_list)
    password_entry.insert(0,password)
    pyperclip.copy(password)
    return password


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_entry.get()
    email = email_entry.get()
    password_ent = password_entry.get()
    new_data = {
        website: {
            "email": email,
            "password": password_ent,
        }
    }

    is_okay = False

    if len(website) == 0 or len(email) == 0 or len(password_ent) == 0:
        messagebox.showinfo(title="Empty fields", message="Please dont leave any fields empty")
    else:
        try:
            with open("data.json", "r") as file:
                data = json.load(file)
        except FileNotFoundError:
            with open("data.json", "w") as file:
                json.dump(new_data, file, indent=4)
        else:
            data.update(new_data)
            with open("data.json", "w") as file:
            # file.writelines(f"{website} | {email} | {password_ent} \n")
                json.dump(data, file, indent=4)
        finally:
                website_entry.delete(0, END)
                password_entry.delete(0, END)


def search_websites():
    website = website_entry.get()
    try:
        with open("data.json", "r") as file:
            data = json.load(file)
    except FileNotFoundError:
        messagebox.showinfo(title="File does not exist", message="No Datafile found")
    else:
        try:
            messagebox.showinfo(title=f"{website} details", message=f"Email: {data[website]['email']} \n Password: {data[website]['password']}")
        except KeyError:
            messagebox.showinfo(title="Website does not exist", message="You dont have a password for this website yet")

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
pass_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=pass_img)
canvas.grid(column=1, row=0)

website_label = Label(text="website: ")
website_label.grid(column=0, row=1, )

website_entry = Entry(width=21)
website_entry.grid(column=1, row=1)
website_entry.focus()

email_label = Label(text="email/username: ")
email_label.grid(column=0, row=2)

email_entry = Entry(width=38)
email_entry.grid(column=1, row=2, columnspan=2)
email_entry.insert(0, "olagunjuikeoluwa@yahoo.co.uk")

password_label = Label(text="password: ")
password_label.grid(column=0, row=3)

password_entry = Entry(width=21)
password_entry.grid(column=1, row=3)

password_button = Button(text="Generate password", command=generate_password)
password_button.grid(row=3, column=2)

search_button = Button(text="Search", command=search_websites, width=14)
search_button.grid(row=1, column=2)

add_button = Button(text="Add", width=36, command=save)
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()
