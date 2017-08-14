# These two lines are because of the folder the demos are located in, and aren't normally necessary
import os.path, sys
sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), os.pardir))

#Example Source from: https://github.com/martinohanlon/minecraft-renderObjv2

#from minecraftstuff import MinecraftDrawing
import mcpi.minecraft as minecraft
import mcpi.block as block
import time
import datetime

# class to create 3d filled polygons
class MinecraftDrawing:
    def __init__(self, mc):
        self.mc = mc

    # draw point
    def drawPoint3d(self, x, y, z, blockType, blockData=None):
        self.mc.setBlock(x,y,z,blockType,blockData)
        #print("x = " + str(x) + ", y = " + str(y) + ", z = " + str(z))

    # draws a face, when passed a collection of vertices which make up a polyhedron
    def drawFace(self, vertices, blockType, blockData=None):

        # get the edges of the face
        edgesVertices = []
        # persist first vertex
        firstVertex = vertices[0]
        # loop through vertices and get edges
        vertexCount = 0
        for vertex in vertices:
            vertexCount+=1
            if vertexCount > 1:
                # got 2 vertices, get the points for the edge
                edgesVertices = edgesVertices + self.getLine(lastVertex.x, lastVertex.y, lastVertex.z, vertex.x, vertex.y, vertex.z)
                #print("x = " + str(lastVertex.x) + ", y = " + str(lastVertex.y) + ", z = " + str(lastVertex.z) + " x2 = " + str(vertex.x) + ", y2 = " + str(vertex.y) + ", z2 = " + str(vertex.z))
            # persist the last vertex found
            lastVertex = vertex
        # get edge between the last and first vertices
        edgesVertices = edgesVertices + self.getLine(lastVertex.x, lastVertex.y, lastVertex.z, firstVertex.x, firstVertex.y, firstVertex.z)

        # sort edges vertices
        def keyX( point ): return point.x
        def keyY( point ): return point.y
        def keyZ( point ): return point.z
        edgesVertices.sort( key=keyZ )
        edgesVertices.sort( key=keyY )
        edgesVertices.sort( key=keyX )

        # not very performant but wont have gaps between in complex models
        for vertex in edgesVertices:
            vertexCount+=1
            # got 2 vertices, draw lines between them
            if (vertexCount > 1):
                self.drawLine(lastVertex.x, lastVertex.y, lastVertex.z, vertex.x, vertex.y, vertex.z, blockType, blockData)
                #print("x = " + str(lastVertex.x) + ", y = " + str(lastVertex.y) + ", z = " + str(lastVertex.z) + " x2 = " + str(vertex.x) + ", y2 = " + str(vertex.y) + ", z2 = " + str(vertex.z))
            # persist the last vertex found
            lastVertex = vertex

    # draw's all the points in a collection of vertices with a block
    def drawVertices(self, vertices, blockType, blockData=None):
        for vertex in vertices:
            self.drawPoint3d(vertex.x, vertex.y, vertex.z, blockType, blockData)

    # draw line
    def drawLine(self, x1, y1, z1, x2, y2, z2, blockType, blockData):
        self.drawVertices(self.getLine(x1, y1, z1, x2, y2, z2), blockType, blockData)

    # returns points on a line
    def getLine(self, x1, y1, z1, x2, y2, z2):

        # return maximum of 2 values
        def MAX(a,b):
            if a > b: return a
            else: return b

        # return step
        def ZSGN(a):
            if a < 0: return -1
            elif a > 0: return 1
            elif a == 0: return 0

        # list for vertices
        vertices = []

        # if the 2 points are the same, return single vertice
        if (x1 == x2 and y1 == y2 and z1 == z2):
            vertices.append(minecraft.Vec3(x1, y1, z1))

        # else get all points in edge
        else:

            dx = x2 - x1
            dy = y2 - y1
            dz = z2 - z1

            ax = abs(dx) << 1
            ay = abs(dy) << 1
            az = abs(dz) << 1

            sx = ZSGN(dx)
            sy = ZSGN(dy)
            sz = ZSGN(dz)

            x = x1
            y = y1
            z = z1

            # x dominant
            if (ax >= MAX(ay, az)):
                yd = ay - (ax >> 1)
                zd = az - (ax >> 1)
                loop = True
                while(loop):
                    vertices.append(minecraft.Vec3(x, y, z))
                    if (x == x2):
                        loop = False
                    if (yd >= 0):
                        y += sy
                        yd -= ax
                    if (zd >= 0):
                        z += sz
                        zd -= ax
                    x += sx
                    yd += ay
                    zd += az
            # y dominant
            elif (ay >= MAX(ax, az)):
                xd = ax - (ay >> 1)
                zd = az - (ay >> 1)
                loop = True
                while(loop):
                    vertices.append(minecraft.Vec3(x, y, z))
                    if (y == y2):
                        loop=False
                    if (xd >= 0):
                        x += sx
                        xd -= ay
                    if (zd >= 0):
                        z += sz
                        zd -= ay
                    y += sy
                    xd += ax
                    zd += az
            # z dominant
            elif(az >= MAX(ax, ay)):
                xd = ax - (az >> 1)
                yd = ay - (az >> 1)
                loop = True
                while(loop):
                    vertices.append(minecraft.Vec3(x, y, z))
                    if (z == z2):
                        loop=False
                    if (xd >= 0):
                        x += sx
                        xd -= az
                    if (yd >= 0):
                        y += sy
                        yd -= az
                    z += sz
                    xd += ax
                    yd += ay

        return vertices

def load_obj(filename, defaultBlock, materials) :
    V = [] #vertex
    T = [] #texcoords
    N = [] #normals
    F = [] #face indexies
    MF = [] #materials to faces

    currentMaterial = defaultBlock

    fh = open(filename)
    for line in fh :
        if line[0] == '#' : continue
        line = line.strip().split(' ')
        if line[0] == 'v' : #vertex
            V.append(line[1:])
        elif line[0] == 'vt' : #tex-coord
            T.append(line[1:])
        elif line[0] == 'vn' : #normal vector
            N.append(line[1:])
        elif line[0] == 'f' : #face
            face = line[1:]
            for i in range(0, len(face)) :
                face[i] = face[i].split('/')
                # OBJ indexies are 1 based not 0 based hence the -1
                # convert indexies to integer
                for j in range(0, len(face[i])) :
                    if face[i][j] != "":
                        face[i][j] = int(face[i][j]) - 1
            #append the material currently in use to the face
            F.append(face)
            MF.append(currentMaterial)

        elif line[0] == 'usemtl': # material

            usemtl = line[1]
            if (usemtl in materials.keys()):
                currentMaterial = materials[usemtl]
            else:
                currentMaterial = defaultBlock
                print("Warning: Couldn't find '" + str(usemtl) + "' in materials using default")

    return V, T, N, F, MF

# strips the x,y,z co-ords from a vertex line, scales appropriately, rounds and converts to int
def getVertexXYZ(vertexLine, scale, startCoord, swapYZ):
    # convert, round and scale
    x = int((float(vertexLine[0]) * scale) + 0.5)
    y = int((float(vertexLine[1]) * scale) + 0.5)
    z = int((float(vertexLine[2]) * scale) + 0.5)
    # add startCoord to x,y,z
    x = x + startCoord.x
    y = y + startCoord.y
    z = z + startCoord.z
    # swap y and z coord if needed
    if swapYZ == True:
        swap = y
        y = z
        z = swap
    return x, y, z

# main program
if __name__ == "__main__":

    print(datetime.datetime.now())

    # Connect to minecraft server 127.0.0.1 as player 'steve'
    mc = minecraft.Minecraft.create(address="127.0.0.1", name="steve")

    #Create minecraft drawing class
    mcDrawing = MinecraftDrawing(mc)

    """
    Load objfile and set constants

     COORDSSCALE = factor to scale the co-ords by
     STARTCOORD = where to start the model, the relative position 0
     CLEARAREA1/2 = 2 points the program should clear an area in between to put the model in
     SWAPYZ = True to sway the Y and Z dimension
     MATERIALS = a dictionary object which maps materials in the obj file to blocks in minecraft
     DEFAULTBLOCK = the default type of block to build the model in, used if a material cant be found
    """

    what_to_build = "shuttle" #Valid values: shuttle, skyscraper, or farmhouse

    if what_to_build == "shuttle":
        COORDSSCALE = 6

        #Build model 20 blocks above player
        pos = mc.player.getTilePos()
        STARTCOORD = minecraft.Vec3(pos.x,pos.z,pos.y+20)
        SWAPYZ = True
        #Note: Y and Z are swapped in this 3d model compared to the MC universe

        DEFAULTBLOCK = [block.WOOL.id,0]
        MATERIALS = {"glass": [block.GLASS.id, 0],
                     "bone": [block.WOOL.id, 0],
                     "fldkdkgrey": [block.WOOL.id, 7],
                     "redbrick": [block.WOOL.id, 14],
                     "black": [block.WOOL.id, 15],
                     "brass": [block.WOOL.id, 1],
                     "dkdkgrey": [block.WOOL.id, 7]}
        vertices,textures,normals,faces,materials = load_obj("resources/shuttle.obj", DEFAULTBLOCK, MATERIALS)

    if what_to_build == "skyscraper":
        COORDSSCALE = 1.4
        #Build model 20 blocks to size of player
        pos = mc.player.getTilePos()
        STARTCOORD = minecraft.Vec3(pos.x,pos.y,pos.z+20)
        SWAPYZ = False
        DEFAULTBLOCK = [block.IRON_BLOCK, 0]
        MATERIALS = {"glass": [block.GLASS.id, 0],
                     "bone": [block.WOOL.id, 0],
                     "fldkdkgrey": [block.WOOL.id, 7],
                     "redbrick": [block.WOOL.id, 14],
                     "black": [block.WOOL.id, 15],
                     "brass": [block.WOOL.id, 1],
                     "dkdkgrey": [block.WOOL.id, 7]}

        MATERIALS = {
            "brass": [block.WOOL.id, 1],
            "bone": [block.WOOL.id, 0],
            "black": [block.WOOL.id, 15],
            "bluteal": [block.IRON_BLOCK, 0],
            "tan": [24, 2],
            "blutan": [42, 0],
            "brown": [5, 1],
            "ltbrown": [5, 3],
        }

        vertices,textures,normals,faces,materials = load_obj("resources/skyscraper.obj", DEFAULTBLOCK, MATERIALS)

    if what_to_build == "farmhouse":
        COORDSSCALE = 1
        #Build model 20 blocks to size of player
        pos = mc.player.getTilePos()
        STARTCOORD = minecraft.Vec3(pos.x,pos.y,pos.z+20)
        DEFAULTBLOCK = [block.IRON_BLOCK, 0]
        MATERIALS = {}
        SWAPYZ = False
        vertices,textures,normals,faces,materials = load_obj("resources/farmhouse.obj", DEFAULTBLOCK, MATERIALS)

    print("obj file loaded")

    #Post a message to the minecraft chat window
    mc.postToChat("Started 3d render...")

    faceCount = 0
    # loop through faces
    for face in faces:
        faceVertices = []

        # loop through vertex's in face and call drawFace function
        for vertex in face:
            #strip co-ords from vertex line
            vertexX, vertexY, vertexZ = getVertexXYZ(vertices[vertex[0]], COORDSSCALE, STARTCOORD, SWAPYZ)

            faceVertices.append(minecraft.Vec3(vertexX,vertexY,vertexZ))

        # draw the face
        mcDrawing.drawFace(faceVertices, materials[faceCount][0], materials[faceCount][1])
        faceCount = faceCount + 1

    mc.postToChat("Model complete.")

    print(datetime.datetime.now())
