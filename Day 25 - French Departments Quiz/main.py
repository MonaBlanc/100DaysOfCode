import turtle

screen = turtle.Screen()
image = "Day 25 - French Departments Quiz/carte-de-france.gif"
screen.addshape(image)
turtle.shape(image)


def get_mouse_click_coor(x, y):
    print(x, y)

turtle.onscreenclick(get_mouse_click_coor)

turtle.mainloop()

