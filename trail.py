import mcpi.minecraft as minecraft
import time

server_address = "199.96.85.3"
my_player_name = "steve"

# Open a connection to the minecraft server
mc = minecraft.Minecraft.create(address=server_address, name=my_player_name)

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