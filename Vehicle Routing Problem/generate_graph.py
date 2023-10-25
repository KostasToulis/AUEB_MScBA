import random
import numpy as np
import matplotlib.pyplot as plt
import math

class Node:
    def __init__(self, id, x , y, demand):
        self.id = id
        self.x = x
        self.y = y
        self.demand = demand
        self.isVisited = False
        self.route = None

class Vehicle:
    def __init__(self, id, capacity):
        self.id = id
        self.capacity = capacity

def CreateNodes(nodesNum):
    random.seed(1)
    nodes = []
    depot = Node(0,50,50, 0)
    depot.isStart = True
    depot.isVisited = True
    nodes.append(depot)
    for i in range(nodesNum-1):
        nodes.append(Node(i+1, random.randint(0,100), random.randint(0,100), random.randint(2,10)))
    return nodes

def CreateVehicles(num, capacity):
    vehicles = []
    for i in range(num):
        vehicles.append(Vehicle(i, capacity))
    return vehicles

def PlotGraph(routes):
    for route in routes:
        route = np.asarray(route, dtype=np.int_)
        plt.plot(route[:,0], route[:,1], linewidth=1, marker='*', color=np.random.rand(3, ))

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