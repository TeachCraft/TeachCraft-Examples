# These two lines are because of the folder the demos are located in, and aren't normally necessary
import os.path, sys
sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), os.pardir))

# Minecraft Turtle Example
from minecraftstuff import MinecraftTurtle
from mcpi import minecraft

# Connect to minecraft server 127.0.0.1 as player 'steve'
mc = minecraft.Minecraft.create(address="127.0.0.1", name="steve")

# get players position
pos = mc.player.getPos()

# create minecraft turtle
turtle = MinecraftTurtle(mc, pos)

turtle.speed(10)

# draw a square
turtle.forward(10)
turtle.right(90)
turtle.forward(10)
turtle.right(90)
turtle.forward(10)
turtle.right(90)
turtle.forward(10)

# draw a square on the floor
turtle.walk()
turtle.forward(11)
turtle.right(90)
turtle.forward(10)
turtle.right(90)
turtle.forward(10)
turtle.right(90)
turtle.forward(10)
