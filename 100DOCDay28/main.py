from tkinter import *
import tkinter.messagebox
FONT = 'DS-Digital'
FG = "white"
BG = '#161A30'
WORK_MIN = 1
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

reps = 0
timer = None
""" This code below is for resetting the timer"""
def reset_timer():
    window.after_cancel(timer)
    timer_label.config(text='25:00')
    global reps
    reps = 0

""" This code below is for starting the timer"""
def start_timer():
    global reps
    reps += 1
    work_sec = WORK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60 
    
    show_task()
    
    if reps % 8 == 0:
        count_down(long_break_sec)
        tkinter.messagebox.showinfo(title="Long Break", message='Time for a 20 Minute break!')
    elif reps % 2 == 0:
        count_down(short_break_sec)
        tkinter.messagebox.showinfo(title="Short Break", message='Time for a 5 Minute break!')
    else:
        count_down(work_sec)

""" This code below is the counting mechanism"""
def count_down(count):
    seconds = count % 60
    minutes = int(count / 60) % 3600
    text = f"{minutes:02}:{seconds:02}"
    timer_label.config(text=text)
    
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count-1)
    else:
        start_timer()
        mark = ''
        work_sessions = reps/2
        for _ in range(work_sessions):
            mark += ":)"

def show_task():
    task_label.config(text= task_entry.get(), font=(FONT, 20, 'italic'), fg=FG)

""" This code below is for UI of the POMODORO App"""
window = Tk()
window.title('Pomodoro App')
window.config(padx=100, pady=50)
window.config(bg=BG)


timer_label = Label(text=f"25:00", font=(FONT, 25, 'bold'),fg='red', bg=BG)
timer_label.grid(row=2, column=3)

task_entry = Entry()
task_entry.grid(row=3, column=3, pady = 10)

start_button = Button(width=5,text='Start Pomodoro', command= start_timer, padx=25, pady=1, fg=FG ,bg=BG)
start_button.grid(row=4, column=1)

reset_button = Button(width=5,text='Reset', command= reset_timer, padx=25, pady=1,fg=FG,bg=BG)
reset_button.grid(row=4, column=4)

current_task = Label(text="Current Task:", fg=FG,bg=BG)
current_task.grid(row=2, column=1)

task_label = Label(text="", fg=FG,bg=BG)
task_label.grid(row=3, column=1)



window.mainloop()