import pandas as pd
from tkinter import *
from random import choice

"""
1. I learnt to understand how the code is interpreted line by line.
2. If you want to access a variable ,declared in function A, in function B, then make that variable global
3. The most important thing is to understand how the code works line-by-line. 

"""


german_words = pd.read_csv('de_words.csv')
to_learn = german_words.to_dict(orient="records")
current_card = {}

def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = choice(to_learn)
    next_word = current_card["de"]
    canvas.itemconfig(card_title, text = "German", fill = "black")
    canvas.itemconfig(word, text = next_word, fill = "black")
    canvas.itemconfig(card_background, image = card_front)
    flip_timer = window.after(3000, flip_card)
    
def flip_card():
    canvas.itemconfig(card_title, text = "English", fill = "white")
    canvas.itemconfig(word, text = current_card["en"], fill = "white")
    canvas.itemconfig(card_background, image = card_back)
    
# =================================== Flash App UI ===================================
window = Tk()
window.title("Flash Card App")
window.config(padx=50, pady=50,bg= "#88AB8E" )

flip_timer = window.after(3000, flip_card)

card_front = PhotoImage(file="card_front.png")
card_back = PhotoImage(file="card_back.png")
right_image = PhotoImage(file="right.png")
wrong_image = PhotoImage(file="wrong.png")



# Canvas
canvas = Canvas(width=800, height=526, bg= "#88AB8E", highlightbackground="#88AB8E")
card_background = canvas.create_image(400, 256, image = card_front)
card_title = canvas.create_text(400, 150, text = "German", font=("Arial", 40, "italic"))
word = canvas.create_text(400, 263, text = "word", font=("Arial", 50, "bold"))
canvas.grid(row=0, column=0, columnspan=2)


# Buttons
right_button = Button(image=right_image, bg="#88AB8E", command=next_card)
right_button.grid(row=1, column=1)
wrong_button = Button(image=wrong_image, bg="#88AB8E", command=next_card)
wrong_button.grid(row=1, column=0)


next_card()


mainloop()