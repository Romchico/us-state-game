import turtle

screen = turtle.Screen()
screen.title("U.S States Game")

#UPLOADING IMAGES
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

#FIGURING OUT COORDINATES
def get_mouse_click_coor(x,y):
    print(x,y)

turtle.onscreenclick(get_mouse_click_coor)
""""" When we click it prints the x,y coordinates. The coordinates 
exist on 50_states.csv file."""


turtle.mainloop()