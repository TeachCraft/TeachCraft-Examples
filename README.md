# TeachCraft-Examples

## Examples

Checkout the <a href='https://github.com/TeachCraft/TeachCraft-Examples/tree/master/examples'>/examples directory</a> in this repo!


## <a href='https://github.com/TeachCraft/TeachCraft-Examples/tree/master/mcpi'>MCPI</a> library (TeachCraft version)

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
mc.player.setPos(x, y, z)
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
mc.player.setTilePos(x, y, z)
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


## <a href='https://github.com/TeachCraft/TeachCraft-Examples/tree/master/minecraftstuff'>minecraftstuff</a> library [From Martin O'Hanlon, <a href='https://github.com/martinohanlon/minecraft-stuff'>repo</a>, <a href='http://www.stuffaboutcode.com/p/minecraft.html'>website</a>, <a href='https://www.amazon.com/gp/product/111894691X/ref=as_li_tl?ie=UTF8&camp=1789&creative=9325&creativeASIN=111894691X&linkCode=as2&tag=teachcraft-20&linkId=62f6ef5032275ace368045b4b7535c8f'>book</a>]

#### minecraftstuff.MinecraftTurtle

- <a href='http://minecraft-stuff.readthedocs.io/en/latest/minecraftturtle.html#id1'>Official Documentation</a>

<details>
  <summary>
turtle = MinecraftTurtle(mc, pos)
  </summary>

> Create a Minecraft Turtle

```python

from mcpi import minecraft
from minecraftstuff import MinecraftTurtle

#Connect to minecraft server 127.0.0.1 as player 'steve'
mc = minecraft.Minecraft.create(address="127.0.0.1", name="steve")

#Get current player's position
pos = mc.player.getPos()


# create minecraft turtle
turtle = MinecraftTurtle(mc, pos)

```

</details>


<details>
  <summary>
turtle.forward(distance)
  </summary>

> Move turtle forward [distance] number of blocks

```python

from mcpi import minecraft
from minecraftstuff import MinecraftTurtle

#Connect to minecraft server 127.0.0.1 as player 'steve'
mc = minecraft.Minecraft.create(address="127.0.0.1", name="steve")

#Get current player's position
pos = mc.player.getPos()


# create minecraft turtle
turtle = MinecraftTurtle(mc, pos)

# Move turtle forward 5 blocks
turtle.forward(5)

```

</details>

<details>
  <summary>
turtle.backward(distance)
  </summary>

> Move turtle backward [distance] number of blocks

```python

from mcpi import minecraft
from minecraftstuff import MinecraftTurtle

#Connect to minecraft server 127.0.0.1 as player 'steve'
mc = minecraft.Minecraft.create(address="127.0.0.1", name="steve")

#Get current player's position
pos = mc.player.getPos()


# create minecraft turtle
turtle = MinecraftTurtle(mc, pos)

turtle.backward(10)

```

</details>

<details>
  <summary>
turtle.right(distance)
  </summary>

> Move turtle right [distance] number of blocks

```python

from mcpi import minecraft
from minecraftstuff import MinecraftTurtle

#Connect to minecraft server 127.0.0.1 as player 'steve'
mc = minecraft.Minecraft.create(address="127.0.0.1", name="steve")

#Get current player's position
pos = mc.player.getPos()


# create minecraft turtle
turtle = MinecraftTurtle(mc, pos)

turtle.right(10)

```

</details>

<details>
  <summary>
turtle.left(distance)
  </summary>

> Move turtle left [distance] number of blocks

```python

from mcpi import minecraft
from minecraftstuff import MinecraftTurtle

#Connect to minecraft server 127.0.0.1 as player 'steve'
mc = minecraft.Minecraft.create(address="127.0.0.1", name="steve")

#Get current player's position
pos = mc.player.getPos()


# create minecraft turtle
turtle = MinecraftTurtle(mc, pos)

turtle.left(10)

```

</details>


<details>
  <summary>
turtle.up(distance)
  </summary>

> Move turtle up [distance] number of blocks

```python

from mcpi import minecraft
from minecraftstuff import MinecraftTurtle

#Connect to minecraft server 127.0.0.1 as player 'steve'
mc = minecraft.Minecraft.create(address="127.0.0.1", name="steve")

#Get current player's position
pos = mc.player.getPos()


# create minecraft turtle
turtle = MinecraftTurtle(mc, pos)

turtle.up(10)

```

</details>

<details>
  <summary>
turtle.down(distance)
  </summary>

> Move turtle down [distance] number of blocks

```python

from mcpi import minecraft
from minecraftstuff import MinecraftTurtle

#Connect to minecraft server 127.0.0.1 as player 'steve'
mc = minecraft.Minecraft.create(address="127.0.0.1", name="steve")

#Get current player's position
pos = mc.player.getPos()


# create minecraft turtle
turtle = MinecraftTurtle(mc, pos)

turtle.down(10)

```

</details>

<details>
  <summary>
turtle.home()
  </summary>

> Move turtle back to the position it started in

```python

from mcpi import minecraft
from minecraftstuff import MinecraftTurtle

#Connect to minecraft server 127.0.0.1 as player 'steve'
mc = minecraft.Minecraft.create(address="127.0.0.1", name="steve")

#Get current player's position
pos = mc.player.getPos()


# create minecraft turtle
turtle = MinecraftTurtle(mc, pos)

turtle.down(10)
turtle.right(10)
turtle.home()

```

</details>

<details>
  <summary>
turtle.speed(integer)
  </summary>

> Change the turtles speed (1 - slowest, 10 - fastest, 0 - no animation, it just draws the lines)

```python

from mcpi import minecraft
from minecraftstuff import MinecraftTurtle

#Connect to minecraft server 127.0.0.1 as player 'steve'
mc = minecraft.Minecraft.create(address="127.0.0.1", name="steve")

#Get current player's position
pos = mc.player.getPos()


# create minecraft turtle
turtle = MinecraftTurtle(mc, pos)

turtle.speed(5)
turtle.down(10)
turtle.speed(10)
turtle.right(10)
turtle.home()

```

</details>


<details>
  <summary>
turtle.penblock(block_id, [block_data])
  </summary>

> Change the turtles speed (1 - slowest, 10 - fastest, 0 - no animation, it just draws the lines)

```python

from mcpi import minecraft
from minecraftstuff import MinecraftTurtle

#Connect to minecraft server 127.0.0.1 as player 'steve'
mc = minecraft.Minecraft.create(address="127.0.0.1", name="steve")

#Get current player's position
pos = mc.player.getPos()


# create minecraft turtle
turtle = MinecraftTurtle(mc, pos)

grass_block_id = 2
turtle.penblock(grass_block_id)
turtle.down(10)

wool_block_id = 35
wool_block_data = 1 #orange

turtle.penblock(wool_block_id, wool_block_data)
turtle.right(10)

```

</details>

<details>
  <summary>
turtle.penup()
  </summary>

> Put the pen up (stop drawing when the turtle moves)

```python

from mcpi import minecraft
from minecraftstuff import MinecraftTurtle

#Connect to minecraft server 127.0.0.1 as player 'steve'
mc = minecraft.Minecraft.create(address="127.0.0.1", name="steve")

#Get current player's position
pos = mc.player.getPos()


# create minecraft turtle
turtle = MinecraftTurtle(mc, pos)

turtle.down(10)

turtle.penup()

turtle.right(10)

```

</details>

<details>
  <summary>
turtle.pendown()
  </summary>

> Put the pen down (start drawing again when the turtle moves after you called turtle.penup())

```python

from mcpi import minecraft
from minecraftstuff import MinecraftTurtle

#Connect to minecraft server 127.0.0.1 as player 'steve'
mc = minecraft.Minecraft.create(address="127.0.0.1", name="steve")

#Get current player's position
pos = mc.player.getPos()


# create minecraft turtle
turtle = MinecraftTurtle(mc, pos)

turtle.down(10)

turtle.pendown()

turtle.right(10)

turtle.penup()

turtle.up(10)

```

</details>

<details>
  <summary>
turtle.isdown()
  </summary>

> Check if the pen is down, returning a boolean

```python

from mcpi import minecraft
from minecraftstuff import MinecraftTurtle

#Connect to minecraft server 127.0.0.1 as player 'steve'
mc = minecraft.Minecraft.create(address="127.0.0.1", name="steve")

#Get current player's position
pos = mc.player.getPos()


# create minecraft turtle
turtle = MinecraftTurtle(mc, pos)

turtle.down(10)

turtle.pendown()

turtle.right(10)

if turtle.isdown():
    print "Pen is down!"

```

</details>


<details>
  <summary>
turtle.setposition(x, y, z)
  </summary>

> Reset turtle's position to a given x/y/z coordinate

```python

from mcpi import minecraft
from minecraftstuff import MinecraftTurtle

#Connect to minecraft server 127.0.0.1 as player 'steve'
mc = minecraft.Minecraft.create(address="127.0.0.1", name="steve")

#Get current player's position
pos = mc.player.getPos()


# create minecraft turtle at player's current position
turtle = MinecraftTurtle(mc, pos)

turtle.down(10)

turtle.right(10)

# Have turtle reset back to player's position
turtle.setposition(pos.x, pos.y, pos.z)

```

</details>

<details>
  <summary>
turtle.setx(x)
  </summary>

> Reset turtle's position to a given x coordinate

```python

from mcpi import minecraft
from minecraftstuff import MinecraftTurtle

#Connect to minecraft server 127.0.0.1 as player 'steve'
mc = minecraft.Minecraft.create(address="127.0.0.1", name="steve")

#Get current player's position
pos = mc.player.getPos()


# create minecraft turtle at player's current position
turtle = MinecraftTurtle(mc, pos)

turtle.down(10)

turtle.right(10)

# Have turtle reset back to player's x position
turtle.setx(pos.x)

```

</details>

<details>
  <summary>
turtle.sety(y)
  </summary>

> Reset turtle's position to a given y coordinate

```python

from mcpi import minecraft
from minecraftstuff import MinecraftTurtle

#Connect to minecraft server 127.0.0.1 as player 'steve'
mc = minecraft.Minecraft.create(address="127.0.0.1", name="steve")

#Get current player's position
pos = mc.player.getPos()


# create minecraft turtle at player's current position
turtle = MinecraftTurtle(mc, pos)

turtle.down(10)

turtle.right(10)

# Have turtle reset back to player's y position
turtle.setx(pos.y)

```

</details>

<details>
  <summary>
turtle.setz(z)
  </summary>

> Reset turtle's position to a given z coordinate

```python

from mcpi import minecraft
from minecraftstuff import MinecraftTurtle

#Connect to minecraft server 127.0.0.1 as player 'steve'
mc = minecraft.Minecraft.create(address="127.0.0.1", name="steve")

#Get current player's position
pos = mc.player.getPos()


# create minecraft turtle at player's current position
turtle = MinecraftTurtle(mc, pos)

turtle.down(10)

turtle.right(10)

# Have turtle reset back to player's z position
turtle.setx(pos.z)

```

</details>

<details>
  <summary>
turtle.position
  </summary>

> Retrieve turtle's current x/y/z position

```python

from mcpi import minecraft
from minecraftstuff import MinecraftTurtle

#Connect to minecraft server 127.0.0.1 as player 'steve'
mc = minecraft.Minecraft.create(address="127.0.0.1", name="steve")

#Get current player's position
pos = mc.player.getPos()


# create minecraft turtle at player's current position
turtle = MinecraftTurtle(mc, pos)

turtlePos = turtle.position
print turtlePos.x
print turtlePos.y
print turtlePos.z


```

</details>

<details>
  <summary>
turtle.setheading(angle)
  </summary>

> Set the turtles headings

```python

from mcpi import minecraft
from minecraftstuff import MinecraftTurtle

#Connect to minecraft server 127.0.0.1 as player 'steve'
mc = minecraft.Minecraft.create(address="127.0.0.1", name="steve")

#Get current player's position
pos = mc.player.getPos()


# create minecraft turtle at player's current position
turtle = MinecraftTurtle(mc, pos)

turtle.setheading(90)

```

</details>


<details>
  <summary>
turtle.setverticalheading(angle)
  </summary>

> Set the turtles vertical headings

```python

from mcpi import minecraft
from minecraftstuff import MinecraftTurtle

#Connect to minecraft server 127.0.0.1 as player 'steve'
mc = minecraft.Minecraft.create(address="127.0.0.1", name="steve")

#Get current player's position
pos = mc.player.getPos()


# create minecraft turtle at player's current position
turtle = MinecraftTurtle(mc, pos)

turtle.setverticalheading(90)

```

</details>

<details>
  <summary>
turtle.walk()
  </summary>

> Force the turtle to walk along the ground

```python

from mcpi import minecraft
from minecraftstuff import MinecraftTurtle

#Connect to minecraft server 127.0.0.1 as player 'steve'
mc = minecraft.Minecraft.create(address="127.0.0.1", name="steve")

#Get current player's position
pos = mc.player.getPos()


# create minecraft turtle at player's current position
turtle = MinecraftTurtle(mc, pos)

turtle.walk()

```

</details>

<details>
  <summary>
turtle.fly()
  </summary>

> Allow the turtle to fly (e.g. not be forced to move along the ground)

```python

from mcpi import minecraft
from minecraftstuff import MinecraftTurtle

#Connect to minecraft server 127.0.0.1 as player 'steve'
mc = minecraft.Minecraft.create(address="127.0.0.1", name="steve")

#Get current player's position
pos = mc.player.getPos()


# create minecraft turtle at player's current position
turtle = MinecraftTurtle(mc, pos)

turtle.fly()

```

</details>

#### minecraftstuff.MinecraftShape

- <a href='http://minecraft-stuff.readthedocs.io/en/latest/minecraftshape.html'>Official Documentation</a>

#### minecraftstuff.MinecraftDrawing

- <a href='http://minecraft-stuff.readthedocs.io/en/latest/minecraftdrawing.html#minecraftdrawing'>Official Documentation</a>

## Block IDs

- <a href='http://minecraft-ids.grahamedgecombe.com/'>Website with lookup table</a>
- <a href='http://www.stuffaboutcode.com/p/minecraft-api-reference.html'>Using a python library</a> [Scroll down to 'Blocks' section]