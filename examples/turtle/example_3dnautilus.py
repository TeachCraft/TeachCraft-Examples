# These two lines are because of the folder the demos are located in, and aren't normally necessary
import os.path, sys
sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), os.pardir, os.pardir))

# Minecraft Turtle Example
from minecraftstuff import MinecraftTurtle
from mcpi import minecraft
from mcpi import block

# Connect to minecraft server 127.0.0.1 as player 'steve'
mc = minecraft.Minecraft.create(address="127.0.0.1", name="steve")

# get players position
pos = mc.player.getPos()

# create minecraft turtle
steve = MinecraftTurtle(mc, pos)

steve.speed(0)
steve.penblock(block.WOOL.id, 14)
S = 50
for j in range(0, 20):
    steve.up(j * 10)
    steve.forward(S)

    steve.left(90)
    steve.down(j * 10)
    steve.forward(S)

    steve.left(90)
    steve.down(j * 10)
    steve.forward(S)

    steve.left(90)
    steve.up(j * 10)
    steve.forward(S)
    steve.left(90)

    steve.left(10)
    S = 0.9 * S
