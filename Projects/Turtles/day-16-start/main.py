# import turtle
#
# # call the module and select the Turtle class with ()
# # save to a new object, () will initialize the object
# demo = turtle.Turtle()

# can shorten and write it out as such,
from turtle import Turtle, Screen

# create new turtle and screen objects
myTurtle = Turtle()
myScreen = Screen()

# get object properties
print(myScreen.canvwidth, myScreen.canvheight)