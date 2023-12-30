from tkinter import *
from data import number, symbol, alfa
import random
from tkinter import messagebox
import pyperclip
import json



# ---------------------------- Search------------------------------- #
def search():
    web_site = write_box_web.get().capitalize()
    try:
        with open("password_file.json", "r") as file:
            data = json.load(file)
            try:
                emile_sh = data[f"{web_site}"]["emile"]
                password_sh = data[f"{web_site}"]["password"]
                messagebox.showinfo(title=f"{web_site}", message=f"emile: {emile_sh} \n password: {password_sh} ")
            except KeyError:
                messagebox.showinfo(title="Search info",
                                    message=f"Dont found site \n maybe you not add or write wrong name of site!")

    except FileNotFoundError:
        messagebox.showinfo(title="Warning!", message="Dont found a file with password!\nPlease Create file first")


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def convert_pass():
    list_pass = []
    write_box_pass.delete(0, 'end')
    for i in range(3):
        list_pass.append(str(random.choice(alfa)))
        list_pass.append(str(random.choice(symbol)))
        list_pass.append(str(random.choice(number)))
        random.shuffle(list_pass)
    list_pass = ''.join(list_pass)
    pyperclip.copy(list_pass)
    write_box_pass.insert(0, string=list_pass)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    web_site = write_box_web.get().capitalize()
    emile = write_box_emile.get()
    password = write_box_pass.get()
    new_data = {
        web_site: {
            "emile": emile,
            "password": password,
        }
    }

    if len(password) == 0 or len(web_site) == 0:
        messagebox.showinfo(title="Empty info", message="Please don`t let any field`s empty")
    else:
        try:
            with open("password_file.json", "r") as file:
                # read a new_data
                data = json.load(file)
                # update data
        except FileNotFoundError:
            with open("password_file.json", "w") as file:
                # write data
                json.dump(new_data, file, indent=4)
        else:
            data.update(new_data)
            with open("password_file.json", "w") as update_file:
                # write data
                json.dump(data, update_file, indent=4)
        finally:
            write_box_web.delete(0, 'end')
            write_box_pass.delete(0, 'end')


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
picture = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=picture)
canvas.grid(column=1, row=0, )

# wrote text program label
web_lab = Label(text="Website:")
web_lab.grid(column=0, row=2)
emile_lab = Label(text="Emile/username: ")
emile_lab.grid(column=0, row=3)
password_lab = Label(text="Password: ")
password_lab.grid(column=0, row=4)

# button widget
gen_pass_button = Button(text="Gen pass", width=8, command=convert_pass)
gen_pass_button.grid(column=2, row=4, )
add_button = Button(text="Add", width=36, command=save)
add_button.grid(column=1, row=5, columnspan=2)
search_button = Button(text="Search", width=8, command=search)
search_button.grid(column=2, row=2)

# entry widget
write_box_web = Entry(width=26)
write_box_web.focus()
write_box_web.grid(column=1, row=2)
write_box_emile = Entry(width=38)
write_box_emile.insert(END, string="robur1994@google.com")
write_box_emile.grid(column=1, row=3, columnspan=2)
emile_get = write_box_emile.get()
write_box_pass = Entry(width=26)
write_box_pass.grid(column=1, row=4)
pass_get = write_box_pass.get()

window.mainloop()
