import tkinter

window=tkinter.Tk()
window.title('My first GUI program')
window.minsize(width=500, height=200)
window.config(padx=100, pady=100)

my_label=tkinter.Label(text='I am a label')
#my_label.place(x=400, y=100)
my_label.grid(column=0, row=0)
my_label.config(padx=20, pady=100)

button=tkinter.Button(text='New button')
button.grid(column=3, row=0)

button=tkinter.Button(text='Click me')
button.grid(column=1, row=1)

input=tkinter.Entry()
input.grid(column=3, row=2)

window.mainloop()