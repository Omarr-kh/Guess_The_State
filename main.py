import turtle
import pandas as pd

# putting the image on the screen
us_image = "./blank_states_img.gif"
turtle.addshape(us_image)
turtle.shape(us_image)

screen = turtle.Screen()

guessed_states = []
data = pd.read_csv("./50_states.csv")
us_states = data["state"].to_list()


while len(guessed_states) < 50:
    user_input = screen.textinput(
        f"{len(guessed_states)}/50 States Guessed", "Enter a State: ").title()

    if user_input == "Exit":
        break

    if user_input in us_states and user_input not in guessed_states:
        guessed_states.append(user_input)
        tr = turtle.Turtle()
        tr.hideturtle()
        tr.penup()
        state_info = data[data["state"] == user_input]
        tr.goto(int(state_info.x), int(state_info.y))
        tr.write(user_input)
