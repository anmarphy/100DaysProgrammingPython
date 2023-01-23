import tkinter
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 15
reps=0
my_timer=None

# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    window.after_cancel(my_timer)
    canvas.itemconfig(timer_text, text='00:00')
    my_label.config(text='Timer', fg=GREEN)
    check_marks.config(text='✔')
    global reps
    reps=0


# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps+=1
    long_break_secs = LONG_BREAK_MIN * 60
    work_sec = WORK_MIN * 60
    short_break_secs = SHORT_BREAK_MIN * 60

    if reps % 8==0:
        count_down(long_break_secs)
        my_label.config(text='Long break', fg=RED)
    elif reps % 2==0:
        count_down(short_break_secs)
        my_label.config(text='Short break', fg=PINK)
    else:
        count_down(work_sec)
        my_label.config(text='Work', fg=GREEN)



# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    count_minutes=math.floor(count / 60)
    count_secs=count % 60

    canvas.itemconfig(timer_text, text=f'{count_minutes}:{str(count_secs).zfill(2)}')
    if count>0:
        global my_timer
        my_timer=window.after(1000, count_down, count-1)
    else:
        start_timer()
        mark='✔'
        work_sessions=math.floor(reps/2)
        for _ in range(work_sessions):
            mark+='✔'
        check_marks.config(text=mark)


# ---------------------------- UI SETUP ------------------------------- #
window=tkinter.Tk()
window.title('Pomodoro')
window.config(padx=100, pady=50, bg=YELLOW)

canvas=tkinter.Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img=tkinter.PhotoImage(file='tomato.png')
canvas.create_image(100, 112, image=tomato_img)
timer_text=canvas.create_text(130, 132, text='00:00',fill='white', font=(FONT_NAME, 21, 'bold'))
canvas.grid(column=1, row=1)

my_label=tkinter.Label(text='Timer', font=(FONT_NAME, 24, 'bold'), fg=GREEN, bg=YELLOW)
my_label.grid(column=1, row=0)

start_button=tkinter.Button(text='Start', highlightthickness=0, command=start_timer)
start_button.grid(column=0, row=3)
start_button.config(padx=10, pady=10)

reset_button=tkinter.Button(text='Reset', highlightthickness=0, command=reset_timer)
reset_button.grid(column=3, row=3)
reset_button.config(padx=10, pady=10)

check_marks=tkinter.Label(text='✔', fg=GREEN, bg=YELLOW)
check_marks.grid(column=1, row=3)


window.mainloop()