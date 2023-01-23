import tkinter

def button_clicked():
    new_text=input.get()
    my_label.config(text=new_text)
button=tkinter.Button(text='Click me', command=button_clicked)
button.pack()

window=tkinter.Tk()
window.title('My first GUI program')
window.minsize(width=500, height=200)

#label
my_label=tkinter.Label(text='New Label', font=('Arial', 24, 'normal') )
my_label.pack(side='left', expand=True)

my_label['text']='Changed text'
my_label.config(text='Other way to change')

#button
#def button_clicked():
#    my_label.config(text='Button Got Clicked')

#button=tkinter.Button(text='Click me', command=button_clicked)
#button.pack()

#Entry
input=tkinter.Entry()
input.pack()




window.mainloop()