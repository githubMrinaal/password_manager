from tkinter import *
from tkinter import messagebox
import pyperclip
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
import random

def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_letters = [random.choice(letters) for _ in range(nr_letters)]
    password_symbols = [random.choice(symbols) for _ in range(nr_symbols)]
    password_numbers = [random.choice(numbers) for _ in range(nr_numbers)]


    password_list = password_letters + password_symbols + password_numbers

    random.shuffle(password_list)

    password = "".join(password_list)

    password_entry.insert(0,password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #

def save_pass():
    web_name = website_entry.get()
    mail_name = email_entry.get()
    pass_name = password_entry.get()
    new_data = {
        web_name:{
            "email":mail_name,
            "password":pass_name,
        }
    }

    if len(web_name) == 0 or len(pass_name) == 0:
        messagebox.showinfo(title="Oops",message="Please don't leave any fields empty!")
    else:
        try:
            with open("/Users/mrinaalnahata/CODE/Python 100 days/password manager/data.json","r") as file:
                data = json.load(file)
        except FileNotFoundError:
            with open("/Users/mrinaalnahata/CODE/Python 100 days/password manager/data.json","w") as file:
                json.dump(new_data,file,indent=4)
        else:

            data.update(new_data)

            with open("/Users/mrinaalnahata/CODE/Python 100 days/password manager/data.json","w") as file:
                json.dump(data, file,indent=4)
        
        finally:
            website_entry.delete(0,END)
            password_entry.delete(0,END)
        
        
def find_password():
    web_name = website_entry.get()
    try:
        with open("/Users/mrinaalnahata/CODE/Python 100 days/password manager/data.json") as file:
            data = json.load(file)
    except FileNotFoundError:
        messagebox.showinfo("filenotfound","No Data file found")
    if web_name in data:
        email = data[web_name]["email"]
        password = data[web_name]["password"]
        messagebox.showinfo({web_name},f"Email:{email}\n Password:{password}")
    else:
        messagebox.showinfo("NA","No details for the website exists")



# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50,pady=50)

canvas = Canvas(width=200,height=200,highlightthickness=0)
pass_img = PhotoImage(file='/Users/mrinaalnahata/CODE/Python 100 days/password manager/logo.png')
canvas.create_image(100,100,image=pass_img)
canvas.grid(column=1,row=1)

website = Label(text="Website:")
website.grid(column=0,row=2)

email = Label(text="Email/Username:")
email.grid(column=0,row=3)

password = Label(text="Password:")
password.grid(column=0,row=4)

website_entry = Entry(width=35)
website_entry.grid(column=1,row=2,columnspan=2)
website_entry.focus()

email_entry = Entry(width=35)
email_entry.grid(column=1,row=3,columnspan=2)
email_entry.insert(0, "test1234@gmail.com")

password_entry = Entry(width=21)
password_entry.grid(column=1,row=4)

genpass = Button(text="Generate Password",command=generate_password)
genpass.grid(column=2,row=4)

add = Button(text="Add",width=36,command=save_pass)
add.grid(column=1,row=5,columnspan=2)

search = Button(text="Search",command=find_password)
search.grid(column=2,row=2)







window.mainloop()