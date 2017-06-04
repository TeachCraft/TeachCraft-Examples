"""
Code as spells! To invoke, execute file, then type spell name into Minecraft chat.

Offensive Spells:

1) nuke [player]
    - Surround target player with active TNT blocks.

2) lavaswim [player]
    - Replace the floor under target player with lava.

Defensive Spells:

1) shield
    - Surrounds you in bedrock, then after 4 seconds turns it into glass so you can re-assess the situation.

2) imonfire
    - Spawns water right above you which pours over you, then removes the water after a couple seconds.

"""
from mcpi import minecraft
import time

server_address = "199.96.85.3"
my_player_name = "steve"

# Open a connection to the minecraft server
mc = minecraft.Minecraft.create(address=server_address, name=my_player_name)

#We first need to get our player ID, so we can focus on just listening to messages posted by us in chat
my_id = mc.getPlayerEntityId(my_player_name)

#Watch for chat messages
while True:

    #For each chat message since the last time we checked...
    for chatpost in mc.events.pollChatPosts():

        #Was the chat message sent by me?
        if chatpost.entityId == my_id:

            # If message was "shield", surround myself in bedrock.
            #   After four seconds, change it to glass so I can re-assess the situation.
            if chatpost.message.lower() == "shield":
                mc.postToChat("Shield activated!")
                pos = mc.player.getPos()
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

            # If message was "imonfire", assume I need water and spawn water over me.
            #   After 3 seconds, replace water with air to cleanup after self.
            elif chatpost.message.lower() == "imonfire":
                mc.postToChat("Pouring water over you!")

                pos = mc.player.getPos()
                water_block_id = 8
                mc.setBlock(pos.x, pos.y+3, pos.z, water_block_id)

                time.sleep(3)

                air_block_id = 0
                mc.setBlock(pos.x, pos.y+3, pos.z, air_block_id)

            # If message was "nuke [player]", surround victim with TNT blocks,
            #   and then put live Redstone under the TNT blocks to activate them.
            elif "nuke" in chatpost.message.lower():
                who = chatpost.message.lower().split(' ')
                if len(who) > 1:
                    who = who[1]
                    mc.postToChat("Nuking "+who+"!")
                    mc_victim = minecraft.Minecraft.create(address=server_address, name=who)
                    victim_pos = mc_victim.player.getPos()

                    #TNT
                    mc.setBlock(victim_pos.x+2, victim_pos.y, victim_pos.z-2, 46)
                    mc.setBlock(victim_pos.x-2, victim_pos.y, victim_pos.z+2, 46)
                    mc.setBlock(victim_pos.x+2, victim_pos.y, victim_pos.z+2, 46)
                    mc.setBlock(victim_pos.x-2, victim_pos.y, victim_pos.z-2, 46)

                    #Redstone
                    mc.setBlock(victim_pos.x+2, victim_pos.y-1, victim_pos.z-2, 152)
                    mc.setBlock(victim_pos.x-2, victim_pos.y-1, victim_pos.z+2, 152)
                    mc.setBlock(victim_pos.x+2, victim_pos.y-1, victim_pos.z+2, 152)
                    mc.setBlock(victim_pos.x-2, victim_pos.y-1, victim_pos.z-2, 152)

            # If message was "lavaswim [player]", replace floor under target
            #   with lava and let them learn how to swim.
            elif "lavaswim" in chatpost.message.lower():
                who = chatpost.message.lower().split(' ')
                if len(who) > 1:
                    who = who[1]
                    mc.postToChat("Created swimming pool of lava for " +who+"!")
                    mc_victim = minecraft.Minecraft.create(address=server_address, name=who)
                    victim_pos = mc_victim.player.getPos()

                    x = victim_pos.x-1
                    y = victim_pos.y-1
                    z = victim_pos.z-1

                    x2 = x + 2
                    y2 = y
                    z2 = z + 2

                    lava_block_id = 10
                    mc.setBlocks(x, y, z, x2, y2, z2, lava_block_id)


    time.sleep(.1)