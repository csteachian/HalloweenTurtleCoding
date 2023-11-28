# adapted from https://www.codetoday.co.uk/post/create-a-halloween-animation-with-python-a-tutorial

import turtle
import time
import random

pumpkin_colour = "orange"
pumpkin_size = 200
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

def carve_mouth(startx, starty):
  carver.penup()
  carver.setposition(startx, starty)
  carver.setheading(45)
  carver.pendown()
  carver.pensize(1)
  carver.begin_fill()
  for index in range(5):
     carver.forward(pumpkin_size/13.3)
     carver.right(90)
     carver.forward(pumpkin_size/13.3)
     carver.left(90)
  carver.setheading(260)
  carver.forward(pumpkin_size/10)
  carver.setheading(180)
  carver.forward((pumpkin_size/2)-1)
  carver.end_fill()

def carve_nose():
  carver.penup()
  
  carver.setposition(0, 0)
  carver.setheading(90)
  carver.shape("triangle")
  carver.stamp()

def carve_pumpkin(colour):
  carver.color(colour) 
  carve_eye((pumpkin_size/4)*-1, (pumpkin_size/10), 1) # 4. Carve left eye
  carve_eye((pumpkin_size/4), (pumpkin_size/10), -1) # 5. Carve right eye
  carve_mouth((pumpkin_size/4)*-1, (pumpkin_size/6.5)*-1) # 6. Carve mouth
  carve_nose() # 7. Carve nose

def light_up():
  window.tracer(0)
  start = time.time()
  count = 0
  colours = ["yellow", "gray", "red", "black"]
  delay = []
  for x in range(5):
    delay.append(random.randint(1,5)/50)
  while True:
    if time.time() - start > delay[count % 5]:
        carve_pumpkin(colours[count % 4])
        window.update()
        count += 1
        start = time.time() # Reset timer

# main program
window = turtle.Screen()
window.bgcolor("black")
window.setup(screen_width, screen_height)

# The turtle to "carve" the pumpkin
carver = turtle.Turtle()
size = carver.turtlesize()
multiplier = pumpkin_size / 200
carver.shapesize(size[0]*multiplier, size[1]*multiplier, int(size[2])*multiplier)

make_pumpkin() # 1. Draw whole pumpkin
carve_base() # 2. Carve base of pumpkin
carve_top() # 3. Carve top of pumpkin
carve_pumpkin("black") # 4. Carve eyes, nose and mouth of pumpkin
light_up()


turtle.done()