# These two lines are because of the folder the demos are located in, and aren't normally necessary
import os.path, sys
sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), os.pardir))

# Minecraft Turtle Example
from minecraftstuff import MinecraftTurtle
from mcpi import minecraft
from mcpi import block
import random


def tree(branchLen, t):
    if branchLen > 6:
        t.penblock(block.WOOL.id, random.randint(0, 15))

        # for performance
        x, y, z = t.position.x, t.position.y, t.position.z
        # draw branch
        t.forward(branchLen)

        t.up(20)
        tree(branchLen - 2, t)

        t.right(90)
        tree(branchLen - 2, t)

        t.left(180)
        tree(branchLen - 2, t)

        t.down(40)
        t.right(90)
        tree(branchLen - 2, t)

        t.up(20)

        # go back
        # t.backward(branchLen)
        # for performance - rather than going back over every line
        t.setposition(x, y, z)

# Connect to minecraft server 127.0.0.1 as player 'steve'
mc = minecraft.Minecraft.create(address="127.0.0.1", name="steve")

# get players position
pos = mc.player.getPos()

# create minecraft turtle
turtle = MinecraftTurtle(mc, pos)

# point up
turtle.setverticalheading(90)

# set speed
turtle.speed(0)

# call the tree fractal
tree(20, turtle)
