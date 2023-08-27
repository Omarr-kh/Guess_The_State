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
    user_input = screen.textinput("Guess a state", "Enter a State: ")

    if user_input:
        pass

turtle.mainloop()