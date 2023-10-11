import random
import numpy as np
import matplotlib.pyplot as plt
import math

class Node:
    def __init__(self, id, x , y):
        self.id = id
        self.x = x
        self.y = y
        self.isVisited = False

def CreateNodes(nodesNum):
    random.seed(1)
    nodes = []
    for i in range(nodesNum):
        nodes.append(Node(i, random.randint(0,100), random.randint(0,100)))
    return nodes

def PlotGraph(nodes):
    coords = np.array([[i.x, i.y] for i in nodes])
    plt.plot(coords[:, 0], coords[:, 1], linewidth=1, marker='*', color='blue')
    plt.plot(coords[0, 0], coords[0, 1], linewidth=1, marker='*', color='red')

    plt.show()

def SelectStartNode(nodes):
   random.seed(1)
   start = random.randint(0,len(nodes)-1)
   return nodes[start]

def CalculateDistance(node1, node2):
   return math.sqrt((node1.x - node2.x)**2 + (node1.y - node2.y)**2)

def CalculateDistMatrix(nodes):
   distMatrix = np.zeros((len(nodes),len(nodes)))
   for node1 in nodes:
      for node2 in nodes:
         distMatrix[node1.id, node2.id] = CalculateDistance(node1, node2)
   return distMatrix

def CalculateSolutionDistance(nodes):
    dist = 0
    for i in range(len(nodes)-1):
        dist += CalculateDistance(nodes[i],nodes[i+1])
    return dist