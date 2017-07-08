# TeachCraft-Examples

[Trail Demo](https://www.youtube.com/watch?v=DONjswBR4dI)

[Algorithm Demo](https://www.youtube.com/watch?v=IJPpqOIl1LQ)

[SpellCraft Demo](http://imgur.com/x4ptEB8)



## MCPI api (TeachCraft version)

Click a function name to see an example.

<details>
  <summary>
mc = minecraft.Minecraft.create(address="127.0.0.1", name="steve")
  </summary>

> Connect to a minecraft world

```python

from mcpi import minecraft

#Connect to minecraft server 127.0.0.1 as player 'steve'
mc = minecraft.Minecraft.create(address="127.0.0.1", name="steve")

#Get current player's position
pos = mc.player.getPos()
print pos.x, pos.y, pos.z

```

</details>

<details>
  <summary>
mc.setBlock(x, y, z, block_id, [block_data])
  </summary>

> Set the block at coordinates X/Y/Z to block_id

```python

from mcpi import minecraft

#Connect to minecraft server 127.0.0.1 as player 'steve'
mc = minecraft.Minecraft.create(address="127.0.0.1", name="steve")

#Get current player's position
pos = mc.player.getPos()

#This is the minecraft block ID of the glass block.
#To see what other block IDs are available, go here in your browser: http://minecraft-ids.grahamedgecombe.com/
glass_block_id = 20

#Set the block underneath the player to be glass
mc.setBlock(pos.x, pos.y-1, pos.z, glass_block_id)

#Set the block to the side of player to be wood of a specific subtype
wood_block_id = 5
wood_data = 1 #subtype
mc.setBlock(pos.x+1, pos.y, pos.z, wood_block_id, wood_data)

```

</details>

<details>
  <summary>
mc.getBlock(x, y, z)
  </summary>

> Get the block at coordinates X/Y/Z, returning its block ID

```python

from mcpi import minecraft

# Connect to minecraft server 127.0.0.1 as player 'steve'
mc = minecraft.Minecraft.create(address="127.0.0.1", name="steve")

# Get current player's position
pos = mc.player.getPos()

# Get the block underneath the player
block_id_under_player = mc.getBlock(pos.x, pos.y-1, pos.z)
grass_block_id = 2

if block_id_under_player == grass_block_id:
    print "Player is standing on grass"

```

</details>



<details>
  <summary>
mc.getBlockWithData(x, y, z)
  </summary>

> Get the block at coordinates X/Y/Z, returning its block ID & data field (e.g. for wool color)

```python

from mcpi import minecraft

# Connect to minecraft server 127.0.0.1 as player 'steve'
mc = minecraft.Minecraft.create(address="127.0.0.1", name="steve")

# Get current player's position
pos = mc.player.getPos()

# Get the block underneath the player
block_under_player = mc.getBlockWithData(pos.x, pos.y-1, pos.z)
print "block id", block_under_player.id
print "block data", block_under_player.data

```

</details>


<details>
  <summary>
mc.setBlocks(x1, y1, z1, x2, y2, z2, block_id, [block_data])
  </summary>

> Set a cuboid of blocks between two opposite corners (x1/y1/z1 and x2/y2/z2)

```python

from mcpi import minecraft

#Connect to minecraft server 127.0.0.1 as player 'steve'
mc = minecraft.Minecraft.create(address="127.0.0.1", name="steve")

#Get current player's position
pos = mc.player.getPos()

#This is the minecraft block ID of the glass block.
#To see what other block IDs are available, go here in your browser: http://minecraft-ids.grahamedgecombe.com/
glass_block_id = 20

#Build a glass cube next to the player
mc.setBlocks(pos.x+3, pos.y, pos.z, pos.x+8, pos.y+5, pos.z+5, glass_block_id)

#Build a wood cube of a specific subtype next to the player, then make it hollow by building a smaller cube of air inside
wood_block_id = 5
wood_data = 1 #subtype
mc.setBlocks(pos.x-3, pos.y, pos.z, pos.x-8, pos.y+5, pos.z-5, wood_block_id, wood_data)

air_block_id = 0
mc.setBlocks(pos.x-2, pos.y+1, pos.z-1, pos.x-7, pos.y+4, pos.z-4, air_block_id)

```

</details>


<details>
  <summary>
mc.getBlocks(x1, y1, z1, x2, y2, z2)
  </summary>

> Get a cuboid of blocks between two opposite corners (x1/y1/z1 and x2/y2/z2)

```python

from mcpi import minecraft

#Connect to minecraft server 127.0.0.1 as player 'steve'
mc = minecraft.Minecraft.create(address="127.0.0.1", name="steve")

#Get current player's position
pos = mc.player.getPos()

blocks = mc.getBlocks(pos.x+3, pos.y, pos.z, pos.x+8, pos.y+5, pos.z+5)
for block_id in blocks:
    print block_id


```

</details>


<details>
  <summary>
mc.player.getPos()
  </summary>

> Get current player's position exactly (decimals)

```python

from mcpi import minecraft

#Connect to minecraft server 127.0.0.1 as player 'steve'
mc = minecraft.Minecraft.create(address="127.0.0.1", name="bob")

#Get current player's position
pos = mc.player.getPos()

# Returns Vec3(18.3814903971,6.0,25.6063951368)
# Can be accessed as pos.x, pos.y, and pos.z
print pos.x, pos.y, pos.z

```

</details>


<details>
  <summary>
mc.player.setPos()
  </summary>

> Set current player's position exactly (supports decimals)

```python

from mcpi import minecraft

#Connect to minecraft server 127.0.0.1 as player 'steve'
mc = minecraft.Minecraft.create(address="127.0.0.1", name="bob")

#Get current player's position
pos = mc.player.getPos()

#Set current player's position 100 blocks in the air
mc.player.setPos(pos.x, pos.y+100, pos.z)

```

</details>

<details>
  <summary>
mc.player.getTilePos()
  </summary>

> Get current player's position rounded to the block (integer)

```python

from mcpi import minecraft

#Connect to minecraft server 127.0.0.1 as player 'steve'
mc = minecraft.Minecraft.create(address="127.0.0.1", name="bob")

#Get current player's position
pos = mc.player.getTilePos()

# Returns Vec3(52, 4, -10)
# Can be accessed as pos.x, pos.y, and pos.z
print pos.x, pos.y, pos.z

```

</details>


<details>
  <summary>
mc.player.setTilePos()
  </summary>

> Set current player's position rounded to the block (supports integers)

```python

from mcpi import minecraft

#Connect to minecraft server 127.0.0.1 as player 'steve'
mc = minecraft.Minecraft.create(address="127.0.0.1", name="bob")

#Get current player's position
pos = mc.player.getTilePos()

#Set current player's position 100 blocks in the air
mc.player.setTilePos(pos.x, pos.y+100, pos.z)

```

</details>


<details>
  <summary>
mc.getHeight(x, z)
  </summary>

> Given an x/z coordinate, find the highest non-air block (y coordinate)

```python

from mcpi import minecraft

#Connect to minecraft server 127.0.0.1 as player 'steve'
mc = minecraft.Minecraft.create(address="127.0.0.1", name="bob")

#Get current player's position
pos = mc.player.getTilePos()

highest_block_y_coordinate = mc.getHeight(pos.x, pos.y)
print highest_block_y_coordinate

```

</details>

<details>
  <summary>
mc.postToChat("Hello World!")
  </summary>

> Post any text string to chat in-game

```python

from mcpi import minecraft

#Connect to minecraft server 127.0.0.1 as player 'steve'
mc = minecraft.Minecraft.create(address="127.0.0.1", name="bob")

mc.postToChat("Hello World!")

```

</details>


<details>
  <summary>
mc.player.pollBlockHits()
  </summary>

> Perform an action wherever the player right clicks with a sword

```python

from mcpi import minecraft

#Connect to minecraft server 127.0.0.1 as player 'steve'
mc = minecraft.Minecraft.create(address="127.0.0.1", name="bob")

while True:

    for blockhit in mc.player.pollBlockHits():

        #Get coordinates for block that player right clicked with sword
        pos = blockhit.pos

        #Clear out a cube of blocks at that location
        air_block_id = 0
        mc.setBlocks(pos.x+2, pos.y+2, pos.z+2, pos.x-2, pos.y-2, pos.z-2, air_block_id)

```

</details>

<details>
  <summary>
mc.player.pollProjectileHits()
  </summary>

> Perform an action wherever the player shoots with an arrow

```python

from mcpi import minecraft

#Connect to minecraft server 127.0.0.1 as player 'steve'
mc = minecraft.Minecraft.create(address="127.0.0.1", name="bob")

while True:

    for blockhit in mc.player.pollProjectileHits():

        #Get coordinates for block that player shot with an arrow
        pos = blockhit.pos

        #Teleport player to where arrow landed
        mc.player.setPos(pos.x, pos.y, pos.z)

```

</details>

<details>
  <summary>
mc.player.pollChatPosts()
  </summary>

> Perform an action whenever the player types something in chat

```python

from mcpi import minecraft

#Connect to minecraft server 127.0.0.1 as player 'steve'
mc = minecraft.Minecraft.create(address="127.0.0.1", name="bob")

while True:

    for chatpost in mc.player.pollChatPosts():

        #If I type explode into chat...
        if chatpost.message.lower() == "explode":

            #Get my position
            pos = mc.player.getPos()

            #Put TNT at my position
            mc.setBlock(pos.x, pos.y, pos.z, 46)

            #And put a redstone block under the TNT to activate it
            mc.setBlock(pos.x, pos.y-1, pos.z, 152)

```

</details>


<details>
  <summary>
mc.events.clearAll()
  </summary>

> Clear all events that have happened since the events where last retrieved

```python

from mcpi import minecraft

#Connect to minecraft server 127.0.0.1 as player 'steve'
mc = minecraft.Minecraft.create(address="127.0.0.1", name="bob")

mc.events.clearAll()

```

</details>


<details>
  <summary>
mc.player.getDirection()
  </summary>

> Get unit vector of x,y,z for the player's direction

```python

from mcpi import minecraft

#Connect to minecraft server 127.0.0.1 as player 'steve'
mc = minecraft.Minecraft.create(address="127.0.0.1", name="bob")

#Get current player's direction
direction = mc.player.getDirection()

# Returns Vec3(-0.935271308082,-0.271442436324,-0.227126801679)
# Can be accessed as direction.x, direction.y, and direction.z
print direction.x, direction.y, direction.z

```

</details>

<details>
  <summary>
mc.player.getPitch()
  </summary>

> Get the pitch angle (-90 to 90) for the player

```python

from mcpi import minecraft

#Connect to minecraft server 127.0.0.1 as player 'steve'
mc = minecraft.Minecraft.create(address="127.0.0.1", name="bob")

#Get current player's pitch
pitch = mc.player.getPitch()

# Returns 15.750118 (or something like that)
print pitch

```

</details>

<details>
  <summary>
mc.player.getRotation()
  </summary>

> Get the rotational angle (0 to 360) for the player

```python

from mcpi import minecraft

#Connect to minecraft server 127.0.0.1 as player 'steve'
mc = minecraft.Minecraft.create(address="127.0.0.1", name="bob")

#Get current player's rotation
rotation = mc.player.getRotation()

# Returns -256.3502 (or something like that)
print rotation

```

</details>



https://github.com/martinohanlon/minecraft-stuff