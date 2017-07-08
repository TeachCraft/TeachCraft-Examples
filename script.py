import mcpi.minecraft as minecraft
import time

# Connect to minecraft server 127.0.0.1 as player 'steve'
mc = minecraft.Minecraft.create(address="127.0.0.1", name="steve")
# HINT: Replace the IP and username above with your own!

# Repeat every 0.2 seconds...
while True:

    #Retrieve the current player's X, Y, and Z coordinates
    pos = mc.player.getPos()

    #This is the minecraft block ID of the flower block.
    #To see what other block IDs are available, go here in your browser: http://minecraft-ids.grahamedgecombe.com/
    block = 38

    #Set the block at the x/y/z coordinates of the current player to the block id we chose above.
    mc.setBlock(pos.x, pos.y, pos.z, block)

    time.sleep(0.2)


# Checkout the Examples directoy for other examples you can run!
# In each example, you'll need to update the IP Address and your game name.