"""
This file gives you super powers in game!

They can be activated by:
- right clicking a block with a sword
- shooting an arrow
- typing specific messages into chat

"""

# These two lines are because of the folder the demos are located in, and aren't normally necessary
import os.path, sys
sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), os.pardir))

import mcpi.minecraft as minecraft
import time

# Connect to minecraft server 127.0.0.1 as player 'steve'
mc = minecraft.Minecraft.create(address="127.0.0.1", name="steve")

while True:

    for blockhit in mc.player.pollProjectileHits():
        # When I shoot an arrow, teleport me to where the arrow lands
        pos = blockhit.pos
        mc.player.setPos(pos.x, pos.y, pos.z)


    for blockhit in mc.player.pollBlockHits():
        # When I right click a block with my sword, clear out space
        pos = blockhit.pos
        mc.setBlocks(pos.x+2, pos.y+2, pos.z+2, pos.x-2, pos.y-2, pos.z-2, 0)

    for chatpost in mc.player.pollChatPosts():

        if chatpost.message.lower() == "shield":
            # Surround myself in bedrock. After 4 seconds, change it to glass.
            mc.postToChat("Shield activated!")
            pos = mc.player.getTilePos()
            mc.player.setPos(pos.x, pos.y, pos.z) #Put player on center of block
            x = pos.x-1
            y = pos.y-1
            z = pos.z-1

            x2 = x + 2
            y2 = y + 3
            z2 = z + 2

            bedrock_block_id = 7
            mc.setBlocks(x, y, z, x2, y2, z2, bedrock_block_id)

            air_block_id = 0
            mc.setBlocks(x+1, y+1, z+1, x2-1, y2-1, z2-1, air_block_id)

            time.sleep(4)

            bedrock_block_id = 20
            mc.setBlocks(x, y, z, x2, y2, z2, bedrock_block_id)

            air_block_id = 0
            mc.setBlocks(x+1, y+1, z+1, x2-1, y2-1, z2-1, air_block_id)

        elif chatpost.message.lower() == "imonfire":
            # Pour water over me, then replace water with air to cleanup after self.
            mc.postToChat("Pouring water over you!")

            pos = mc.player.getPos()
            water_block_id = 8
            mc.setBlock(pos.x, pos.y+3, pos.z, water_block_id)

            time.sleep(3)

            air_block_id = 0
            mc.setBlock(pos.x, pos.y+3, pos.z, air_block_id)

    time.sleep(.1)
