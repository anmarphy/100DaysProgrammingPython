from tkinter import *
import pandas as pd
import random

BACKGROUND_COLOR = "#B1DDC6"
FONT_NAME = "Arial"
try:
    data=pd.read_csv('data/words_to_learn.csv')

except FileNotFoundError:
    data=pd.read_csv('data/french_words.csv')

to_learn=data.to_dict(orient='records')
current_card={}

def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    canvas.itemconfig(card_title, text='French')
    canvas.itemconfig(card_word, text=current_card['French'], fill='black')
    canvas.itemconfig(card_background, image=card_front_img)
    flip_timer=window.after(3000, func=flip_card)

def flip_card():
    canvas.itemconfig(card_title, text='English')
    canvas.itemconfig(card_word, text=current_card['English'], fill='white')
    canvas.itemconfig(card_background, image=card_back_img)

def is_known():
    to_learn.remove(current_card)
    data=pd.DataFrame(to_learn)
    data.to_csv('data/words_to_learn.csv', index=False)

    next_card()



##UI

window=Tk()
window.title('Flash cards')
window.config(padx=100, pady=50, bg=BACKGROUND_COLOR)
flip_timer=window.after(3000, func=flip_card)

canvas=Canvas(width=800, height=526)
card_front_img=PhotoImage(file="images/card_front.png")
card_back_img=PhotoImage(file="images/card_back.png")
card_background=canvas.create_image(400, 263, image=card_front_img)
card_title=canvas.create_text(400, 150, text='Title', font=(FONT_NAME, 40, 'italic'))
card_word=canvas.create_text(400, 263, text='word', font=(FONT_NAME, 60, 'bold'))
canvas.grid(row=0, column=0, columnspan=2)

my_image_right = PhotoImage(file="images/right.png")
right_button=Button(image=my_image_right, highlightthickness=0, command=is_known)
right_button.grid(column=0, row=2)
right_button.config(padx=10, pady=10)


my_image_wrong = PhotoImage(file="images/wrong.png")
wrong_button=Button(image=my_image_wrong, highlightthickness=0, command=next_card)
wrong_button.grid(column=1, row=2)
wrong_button.config(padx=50, pady=50)

next_card()

window.mainloop()