import turtle
from turtle import Turtle
import pandas

screen = turtle.Screen()
screen.title("U.S.States Game")

#как загрузить новую форму черепахи:
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
data = pandas.read_csv("50_states.csv")
states_list = data["state"].to_list()
# def get_mouse_click_coor(x, y):
#     print(x, y)
# #будет слушать щелчек мыши и затем выведет координаты курсора, которым я щелкаю в разных местах:
# turtle.onscreenclick(get_mouse_click_coor)

guessed_states = []
while len(guessed_states) < 50:
    answer = turtle.textinput(title=f"{len(guessed_states)}/50 States correct", prompt="What's another state's name?").title()
    state_row = data[data.state == answer]
    if answer == "Exit":
        missing_states = []
        for state in states_list:
            if state not in guessed_states:
                missing_states.append(state)
        mis_data = pandas.DataFrame(missing_states)
        mis_data.to_csv("missed_states.csv")
        break
    if answer in states_list:
        new_turtle = Turtle()
        new_turtle.hideturtle()
        new_turtle.penup()
        new_turtle.goto(int(state_row.x), int(state_row.y))
        new_turtle.write(answer)
        # или предыдущую строку можно записать как:
        # new_turtle.write(state_row.state.item())
        guessed_states.append(answer)
#удерживает открытым зкран:
turtle.mainloop()
