import random
import math
import numpy as np
from generate_graph import CreateNodes, PlotGraph, Node
import time


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

def SelectClosestNeighbor(distMatrix, targetNode, sortedNodes):
   neighbors = distMatrix[targetNode.id]
   min = 1000000
   minIndex = -1
   nodeIds = [node.id for node in sortedNodes]
   for i,dist in enumerate(neighbors):
      if (dist < min and dist != 0 and i not in nodeIds):
         min = dist
         minIndex = i
   return minIndex

nodes = CreateNodes(20)
sortedNodes = []
tempNodes = nodes[:]
distMatrix = CalculateDistMatrix(nodes)
startNode = SelectStartNode(nodes)
tempNodes.remove(startNode)
sortedNodes.append(startNode)
startTime = time.time()
nextNode = nodes[SelectClosestNeighbor(distMatrix, startNode, sortedNodes)]
while len(tempNodes) > 0:
   tempNodes.remove(nextNode)
   sortedNodes.append(nextNode)
   nextNode = nodes[SelectClosestNeighbor(distMatrix, nextNode, sortedNodes)]

endTime = time.time()
print('Nearest neighbor time elapsed: ', endTime-startTime)
sortedNodes.append(startNode)
PlotGraph(sortedNodes)



