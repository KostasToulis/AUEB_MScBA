import random
import math
import numpy as np
from generate_graph import CreateNodes, PlotGraph, Node, SelectStartNode, CalculateDistMatrix, CalculateSolutionDistance
import time

def SelectInsertion(nodes, sortedNodes, distMatrix):
    for node in nodes:

        if node.isVisited:
            continue
        minDist = 10000000
        nextNode = -1
        minIndex = -1
        for i in range(len(sortedNodes)-1):
            distAdded = distMatrix[sortedNodes[i].id][node.id] + distMatrix[node.id][sortedNodes[i+1].id]
            distRemoved = distMatrix[sortedNodes[i].id][sortedNodes[i+1].id]
            dist = distAdded - distRemoved
            if dist < minDist:
                minDist = dist
                nextNode = node
                minIndex = i+1
    return nextNode, minIndex

#
# node1 = Node(0,50,50)
# node2 = Node(1,55,45)
# node3 = Node(2,20,89)
# node4 = Node(3,78,23)
# node5 = Node(4,40,84)
# nodes = [node1, node2, node3, node4, node5]
# startNode = node1
#

nodes = CreateNodes(500)
sortedNodes = []
distMatrix = CalculateDistMatrix(nodes)
startNode = SelectStartNode(nodes)
sortedNodes.append(startNode)
sortedNodes.append(startNode)
startTime = time.time()
while len(sortedNodes) < len(nodes)+1:
    nextNode, index = SelectInsertion(nodes, sortedNodes, distMatrix)
    nextNode.isVisited = True
    sortedNodes.insert(index, nextNode)

endTime = time.time()
print('Minimum insertion time elapsed: ', endTime-startTime)
print('Minimum insertion distance: ', CalculateSolutionDistance(sortedNodes))
PlotGraph(sortedNodes)