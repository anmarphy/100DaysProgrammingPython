from tkinter import *
from tkinter import messagebox
from password_generator import password_generator
import pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    password=password_generator()
    password_entry.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
    website = web_entry.get()
    password = password_entry.get()
    email=user_entry.get()

    if len(website)==0 or len(password)==0:
        messagebox.askquestion(title='Empty value', message='Please check that all fields are filled')

    else:
        is_ok=messagebox.askokcancel(title=website, message=f'There are the details entered: \n website: {website}  \n password: {password}, \n email: {email} \n Is it ok to save?')

        if is_ok==True:
            with open('data.txt', 'a') as data_file:  ##Append
                data_file.write(f'\n{website} | {email} | {password}')
                web_entry.delete(0, END)
                password_entry.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #
window=Tk()
window.title('Password Manager')
window.config(padx=50, pady=50)

canvas=Canvas(height=200, width=200)
logo_image=PhotoImage(file='logo.png')
canvas.create_image(100,100,image=logo_image)
canvas.grid(column=1, row=0)

web_label=Label(text='Website')
web_label.grid(column=0, row=1)

user_label=Label(text='Email/Username')
user_label.grid(column=0, row=2)

password_label=Label(text='Password')
password_label.grid(column=0, row=3)

web_entry=Entry(width=35)
web_entry.grid(column=1, row=1, columnspan=2)

user_entry=Entry(width=35)
user_entry.grid(column=1, row=2, columnspan=2)
user_entry.insert(0, 'sete@fer.com')

password_entry=Entry(width=17)
password_entry.grid(column=1, row=3)

add_button=Button(text='Add', highlightthickness=0, width=35, command=save_password)
add_button.grid(column=1, row=4, columnspan=2)

generate_button=Button(text='Generate Password', command=generate_password )
generate_button.grid(column=2, row=3)


window.mainloop()