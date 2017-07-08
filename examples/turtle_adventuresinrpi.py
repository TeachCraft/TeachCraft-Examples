# These two lines are because of the folder the demos are located in, and aren't normally necessary
import os.path, sys
sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), os.pardir))

# Minecraft Turtle Example
# Ported from the scratch turtle project in "Adventures in Raspberry Pi"
from minecraftstuff import MinecraftTurtle
from mcpi import minecraft
from mcpi import block

# Connect to minecraft server 127.0.0.1 as player 'steve'
mc = minecraft.Minecraft.create(address="127.0.0.1", name="steve")

# get players position
pos = mc.player.getPos()

# create minecraft turtle
turtle = MinecraftTurtle(mc, pos)
turtle.speed(0)
turtle.setheading(90)
NumberOfSides = 5
Angle = 360 / NumberOfSides
SideLength = 20
WoolColour = 0

for count in range(24):
    for side in range(NumberOfSides):
        turtle.forward(SideLength)
        turtle.right(Angle)
    turtle.right(15)
    WoolColour += 1
    if WoolColour > 15:
        WoolColour = 0
    turtle.penblock(block.WOOL.id, WoolColour)
    # go 3d
    # turtle.sety(turtle.position.y + 1)
