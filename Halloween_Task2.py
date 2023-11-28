# adapted from https://www.codetoday.co.uk/post/create-a-halloween-animation-with-python-a-tutorial

import turtle

pumpkin_colour = "orange"
pumpkin_size = 250
screen_width = 300
screen_height = 300

# Make pumpkin
def make_pumpkin():
  pumpkin = turtle.Turtle()
  pumpkin.hideturtle()
  pumpkin.color(pumpkin_colour)
  pumpkin.dot(pumpkin_size)

def carve_base():
  carver.penup()
  carver.setposition((screen_width/2)*-1, (pumpkin_size/2)*-1)
  carver.pensize(pumpkin_size*0.1)
  carver.pendown()
  carver.forward(600)
  carver.pensize(2)

def carve_top():
  carver.penup()
  carver.setposition((screen_width/2)*-1, (pumpkin_size/2))
  carver.pensize(pumpkin_size*0.1)
  carver.pendown()
  carver.forward(600)
  carver.pensize(2)

def carve_eye(startx, starty, orientation):
  carver.setheading(0)
  carver.penup()
  carver.setposition(startx,starty)
  carver.pendown()
  carver.begin_fill()
  #carver.forward(orientation * 40)
  carver.forward(orientation * (pumpkin_size/5))
  carver.setheading(orientation * 135)
  carver.forward(orientation * (pumpkin_size/2.8))
  carver.end_fill()

# main program
window = turtle.Screen()
window.bgcolor("black")
window.setup(screen_width, screen_height)

# The turtle to "carve" the pumpkin
carver = turtle.Turtle()

make_pumpkin() # 1. Draw whole pumpkin
carve_base() # 2. Carve base of pumpkin
carve_top() # 3. Carve top of pumpkin
#carve_eye(-50, 20, 1)
#carve_eye(50, 20, -1) 
carve_eye((pumpkin_size/4)*-1, (pumpkin_size/10), 1)
carve_eye((pumpkin_size/4), (pumpkin_size/10), -1)

turtle.done()