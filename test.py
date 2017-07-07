from mcpi import minecraft
import time

"""
- automatically stop day/night cycle (but allow override via settings)
- Make it more of a survival game, first lesson is dying, second lesson is how to avoid death and find out where you were (recording positions)

- Revert hashmap change, keep it a single array, just filter it when returning it to the user based on the name they supplied

"""

server_address = "158.69.221.37"
my_player_name = "bob"

mc = minecraft.Minecraft.create(name=my_player_name)

my_id = mc.getPlayerEntityId(my_player_name)

def tnt_trap(pos):
    mc.setBlock(pos.x, pos.y-1, pos.z, 46)
    mc.setBlock(pos.x, pos.y-2, pos.z, 152) #Redstone

def clear(pos):
    mc.setBlocks(pos.x+2, pos.y+2, pos.z+2, pos.x-2, pos.y-2, pos.z-2, 0)

active_spell = "tnt_trap"

while True:


    for blockhit in mc.player.pollProjectileHits():
        print "AAAAAY1", blockhit
        #AAAAAY1 BlockEvent(BlockEvent.HIT, -23, -4, 46, 1, 773)
        #Worked, but only on hitting entity, not block

        pos = blockhit.pos
        #clear(pos)

        mc.player.setPos(pos.x, pos.y, pos.z)
        print "sb1"


    for blockhit in mc.player.pollBlockHits():
        pos = blockhit.pos
        clear(pos)
        print "sb1"

    for chatpost in mc.player.pollChatPosts():

        if chatpost.message.lower() == "clear":
            pos = mc.player.getPos()
            clear(pos)


    time.sleep(.1)