import numpy as N
import matplotlib as plt
from enum import Enum

def drawGraphFromFile(fileName):
    retVal = []
    with open(fileName, 'r') as file:
        for line in file:
            if line[0] != '#':
                if line.find('\n') != -1:
                    retVal.append(line[:line.find('\n')].split(" "))
                else:
                    retVal.append(line.split(" "))
    return retVal

# RING_GRAPH          = drawGraphFromFile('ringGraph.txt')
STAR_GRAPH          = drawGraphFromFile('starGraph.txt')
# MESH_GRAPH          = drawGraphFromFile('meshGraph.txt')
# ALL_CONNECTED_GRAPH = drawGraphFromFile('allConnectedGraph.txt')
# BUS_GRAPH           = drawGraphFromFile('busGraph.txt')
# HYBRID_GRAPH        = drawGraphFromFile('hybridGraph.txt')
# LINE_GRAPH          = drawGraphFromFile('lineGraph.txt')
# TREE_GRAPH          = drawGraphFromFile('treeGraph.txt')

class graphType(Enum):
    NONE          = 0
    RING          = 1
    STAR          = 2
    MESH          = 3
    ALL_CONNECTED = 4
    BUS           = 5
    HYBRID        = 6
    LINE          = 7
    TREE          = 8

class dataToDisplay:

    #this needs to be set to the type of graph (star, ring, etc)
    typeOfGraph = graphType.NONE
    
    #this represents the nodes that the virus starts at
    startNodes = []

    #this list shall contain lists of tuples representing how the virus spreads.
    # 
    # Example:
    # [[(1,2), (1,3)]
    # [(1,4), (2,5), (2,6)]]
    #
    # in this example, during the first step of the simulation the virus spreads 
    # from node 1 to node 2, and node 1 to node 3. In the second step, it spreads 
    # from node 1 to node 4, and node 2 to nodes 5 and 6
    animationSteps = []
    