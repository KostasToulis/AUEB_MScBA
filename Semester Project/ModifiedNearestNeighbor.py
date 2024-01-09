from Setup import *
from sol_checker import Node
import math
import numpy as np

def CalculateNewDistMatrix(nodes):
    distMatrix = np.zeros((len(nodes), len(nodes)))
    for i in range(len(nodes)):
        for j in range(i,len(nodes)):
            distMatrix[nodes[i].newID, nodes[j].newID] = CalculateDistance(nodes[i], nodes[j]) #* (node1.demand + node2.demand)
    return distMatrix

def CalculateNeighborCost(target, neighbor):
    return CalculateDistance(target,neighbor)/(1+neighbor.demand) #*DemandAll-DemandSelected

def SelectClosestNeighbor(targetNode, nodes):
    minCost = 100000
    minNode = None
    for node in nodes:
        cost = CalculateNeighborCost(targetNode, node)
        if cost<minCost and cost != 0:
            minCost = cost
            minNode = node
    return minNode


def NearestNeighbor(nodes):
    depot = nodes[0]
    node_len = len(nodes)
    sortedNodes = [depot]
    nodes.remove(depot)

    nextNode = SelectClosestNeighbor(depot, nodes)
    nextNode.newVisited = True
    while len(sortedNodes) < node_len:
        sortedNodes.append(nextNode)
        nodes.remove(nextNode)
        nextNode = SelectClosestNeighbor(nextNode, nodes)
    return sortedNodes