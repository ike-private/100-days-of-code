import turtle
import csv
import pandas

screen = turtle.Screen()
screen.title("US States game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
states = pandas.read_csv("50_states.csv")
correct_guesses = []

while len(correct_guesses) < 50:
    answer = screen.textinput(title = f"Guess the state {len(correct_guesses)}/50 states correct", prompt="What is another state name?")
    state_info = states[states.state == answer.title()]
    if answer == "Exit":
        break
    if state_info is not None:
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        t.goto(int(state_info.x), int(state_info.y))
        t.write(answer.title())
        correct_guesses.append(state_info.state)

with open('remaining_states.csv', 'w') as f:
    writer = csv.writer(f)
    for s in states.state:
        if s not in correct_guesses:
            writer.writerow(s)

screen.exitonclick()