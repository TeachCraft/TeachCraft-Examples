# This setup is for http://teachcraft.net/lesson1
# You must change the IP address and your name in the create() call below before running!

from mcpi import minecraft
mc = minecraft.Minecraft.create(address="127.0.0.1", name="steve")

y = mc.getHeight(0, 0)
mc.setBlocks(-4, y-1, -4, 4, y+1, 4, 7)
mc.setBlocks(-3, y, -3, 3, y+20, 3, 0)
print('In your Server console, please run the following command:')
print('\tsetworldspawn 0 ' + str(y) + ' 0')
