import mcpi.minecraft as minecraft

server_address = "199.96.85.3"
my_player_name = "steve"

# Open a connection to the minecraft server
mc = minecraft.Minecraft.create(address=server_address, name=my_player_name)

#This is the minecraft block ID of the diamond block.
#To see what other block IDs are available, go here in your browser: http://minecraft-ids.grahamedgecombe.com/
block = 57
pos = mc.player.getPos()

for i in range(5):
    x = pos.x + i
    y = pos.y + i
    z = pos.z + i

    x2 = x + 8 - (i*2)
    y2 = y
    z2 = z + 8 - (i*2)
    mc.setBlocks(x, y, z, x2, y2, z2, block)