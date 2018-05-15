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

STAR_GRAPH = drawGraphFromFile('starGraph.txt')

class graphType(Enum):
    NONE = 0
    STAR = 1
    TREE = 2

class dataToDisplay:
    typeOfGraph = graphType.NONE
    startNodes = []