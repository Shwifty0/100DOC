from turtle import Turtle, Screen
import pandas as pd

screen = Screen()
image = 'blank_states_img.gif'
screen.addshape(image)
screen.title('U.S. States Game')

turtle = Turtle(shape=image)
state_turtle = Turtle()

states_data = pd.read_csv('50_states.csv')

states = list(states_data.state)
states_count = len(states_data['state'])
guessed_states = []
while states_count != 0:
    user_input = screen.textinput(f'{len(guessed_states)}/50:', 'State Name:')
    for state in states:
        correct_form = user_input.title()
        if correct_form == state:
            if correct_form not in guessed_states:
                guessed_states.append(correct_form)
                state_row = states_data[states_data.state == correct_form]
                state_turtle.ht()
                state_turtle.penup()
                state_turtle.goto(int(state_row.x), int(state_row.y))
                state_turtle.write(correct_form, font=('Arial', 10, 'bold'))
                states_count -= 1
    if user_input == 'Exit':
        missing_states = []
        for state in states:
            if state not in guessed_states:
                missing_states.append(state)
        new_data = pd.DataFrame(missing_states)
        new_data.to_csv('states_to_learn.csv')
        break

