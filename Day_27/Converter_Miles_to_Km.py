import tkinter
FONT=('Arial', 10, 'normal')

#Screen
window=tkinter.Tk()
window.title('Mile to Km Converter')
window.minsize(width=500, height=200)
window.config(padx=50, pady=50)

#Entry
input=tkinter.Entry()
input.grid(column=0, row=0)

#Labels
miles_label=tkinter.Label(text='Miles', font=FONT)
miles_label.grid(column=1, row=0)
miles_label.config(padx=10, pady=10)

equal_label=tkinter.Label(text='is equal to', font=FONT)
equal_label.grid(column=0, row=1)
equal_label.config(padx=10, pady=10)

result_label=tkinter.Label(text= ' Km', font=FONT)
result_label.grid(column=1, row=1)
result_label.config(pady=10, padx=10)

#Button
def miles_km():
    miles=input.get()
    km=int(miles)*1.609
    result_label.config(text=f'{round(km)} Km')

button=tkinter.Button(text='Calculate', command=miles_km)
button.grid(column=0, row=2)



window.mainloop()