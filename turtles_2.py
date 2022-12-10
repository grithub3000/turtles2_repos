'''
This program takes an integer as a command line argument and will draw that
many mini versions of the scene with a house, 2 trees, and a sun. Typing
an invalid character or string as the argument will return an error message,
and then exit. Each mini scene will be exactly half the size of the last.
Putting 0 in the command line will simply draw the scene once it its original
size.
'''

import turtle
import sys

def triangle(ted, side_length):
    '''Draws a triangle.'''
    ted.forward(int(side_length))
    ted.rt(120)
    ted.forward(int(side_length))
    ted.rt(120)
    ted.forward(int(side_length))

def rectangle(ted, height, width):
    '''Draws a rectangle.'''
    for _ in range(2):
        ted.rt(90)
        ted.forward(height)
        ted.rt(90)
        ted.forward(width)

def circle(ted, diameter):
    '''Draws a circle.'''
    for _ in range(360):
        ted.forward(diameter / 120)
        ted.rt(1)

def scene_scaled(size):
    '''Draws the entire scene, with its size multiplied by 'size'.'''
    ted = turtle.Turtle()
    turtle.screensize(canvwidth = 1000, canvheight = 1000)
    window = turtle.Screen()
    window.bgcolor("light blue")

    ted.rt(60)

    ted.pencolor("black")
    ted.fillcolor("brown")
    ted.begin_fill()
    triangle(ted, 200 * size)
    ted.end_fill()
    #Draws the roof.

    ted.backward(200 * size)
    ted.lt(30)

    ted.pencolor("light grey")
    ted.fillcolor("tan")
    ted.begin_fill()
    rectangle(ted, 200 * size, 200 * size)
    ted.end_fill()
    #Draws the house.

    ted.backward(200 * size)
    ted.rt(90)
    ted.forward(66 * size)
    ted.lt(180)

    ted.pencolor("tan")
    ted.fillcolor("grey")
    ted.begin_fill()
    rectangle(ted, 125 * size, 66 * size)
    ted.end_fill()
    #Draws the door.

    ted.backward(50 * size)
    ted.rt(90)
    ted.penup()
    ted.forward(60 * size)
    ted.pendown()

    ted.pencolor("black")
    ted.fillcolor("black")
    ted.begin_fill()
    circle(ted, 7.5 * size)
    ted.end_fill()
    #Draws the doorknob.

    ted.penup()
    ted.rt(90)
    ted.forward(17 * size)
    ted.lt(90)
    ted.forward(225 * size)
    ted.rt(90)
    ted.backward(66 * size)
    ted.pendown()
    ted.lt(90)

    ted.pencolor("black")
    ted.fillcolor("light grey")
    ted.begin_fill()
    rectangle(ted, 66 * size, 66 * size)
    ted.end_fill()
    #Draws the window.

    ted.rt(90)
    ted.forward(33 * size)
    ted.rt(90)
    ted.forward(66 * size)
    ted.backward(33 * size)
    ted.rt(90)
    ted.forward(33 * size)
    ted.backward(66 * size)
    #Draws lines on window.

    ted.penup()
    ted.lt(90)
    ted.forward(242 * size)
    ted.rt(90)
    ted.forward(300 * size)
    ted.pendown()

    ted.pencolor("brown")
    ted.fillcolor("brown")
    ted.begin_fill()
    rectangle(ted, 125 * size, 66 * size)
    ted.end_fill()
    #Draws tree-trunk 1.

    ted.rt(90)
    ted.penup()
    ted.forward(90 * size)
    ted.rt(90)
    ted.forward(33 * size)
    ted.pendown()
    ted.lt(120)

    ted.pencolor("black")
    ted.fillcolor("green")
    ted.begin_fill()
    triangle(ted, 150 * size)
    ted.end_fill()
    #Draws tree leaves 1.

    ted.penup()
    ted.lt(30)
    ted.forward(90 * size)
    ted.lt(90)
    ted.forward(400 * size)
    ted.rt(180)
    ted.pendown()

    ted.pencolor("brown")
    ted.fillcolor("brown")
    ted.begin_fill()
    rectangle(ted, 125 * size, 66 * size)
    ted.end_fill()
    #Draws tree-trunk 2.

    ted.penup()
    ted.rt(90)
    ted.forward(100 * size)
    ted.rt(90)
    ted.forward(33 * size)
    ted.rt(135)
    ted.pendown()

    ted.pencolor("green")
    ted.fillcolor("green")
    ted.begin_fill()
    rectangle(ted, 80 * size, 80 * size)
    ted.end_fill()
    #Draws tree leaves 2.

    ted.rt(135)
    ted.penup()
    ted.forward(400 * size)
    ted.rt(90)
    ted.pendown()

    ted.pencolor("black")
    ted.fillcolor("yellow")
    ted.begin_fill()
    circle(ted, 200 * size)
    ted.end_fill()
    #Draws sun.

def main():
    '''The main program.'''

    try:
        argument = int(sys.argv[1])

    except ValueError:
        print("Command line argument must be a  positive integer")
        return

    if argument < 0:
        print("Command line argument must be a positive integer")
        return

    scene_scaled(1)

    i = 0.5
    for _ in range(argument):
        scene_scaled(i)
        i *= 0.5

    turtle.mainloop()
if __name__ == "__main__":
    main()
