import turtle
import pandas as pd

df = pd.read_csv("50_states.csv")
screen = turtle.Screen()
screen.title("U.S States Game")

#UPLOADING IMAGES
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
true_ans = 0
while true_ans < 51:
    answer_state = screen.textinput(title=f"{true_ans}/50 States Correct", prompt="What's the another state's name?")
    if answer_state == None: # In case you choose cancel
        break
    answer_state = answer_state.lower()
    if len(df[df["state"] == answer_state]) == 1:
        true_ans += 1

        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        x_cor = int(df["x"][df["state"] == answer_state].iloc[0])
        y_cor = int(df["y"][df["state"] == answer_state].iloc[0])
        t.goto(x_cor, y_cor)
        t.write(answer_state.lower())
        df = df[df["state"] != answer_state]

df.to_csv("not_learnt_states.csv", index=False)


turtle.mainloop()
