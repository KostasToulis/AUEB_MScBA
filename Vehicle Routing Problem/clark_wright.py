from generate_graph import CreateNodes, CreateVehicles, CalculateDistMatrix, PlotGraph, CalculateDistance
import numpy as np
import math
import time
import itertools

class Saving:
    def __init__(self, node1, node2, value):
        self.i = node1
        self.j = node2
        self.value = value

class Route:
    def __init__(self, id, nodes):
        self.id = id
        self.nodes = nodes
        self.cost = self.CalculateCost(nodes)
        self.distance = self.CalculateRouteDistance(nodes)
        self.isAdded = False

    def CalculateCost(self, nodes):
        cost = 0
        for node in nodes:
            cost += node.demand
        return cost

    def CalculateRouteDistance(self, nodes):
        distance = 0
        for i in range(len(nodes)-1):
            distance += CalculateDistance(nodes[i], nodes[i+1])
        return distance

def CalculateSavingsMatrix(nodes, distMatrix):
    savings = []
    for i in range(1,len(nodes)):
        for j in range(i+1,len(nodes)):
            value = distMatrix[nodes[i].id][0] + distMatrix[0][nodes[j].id] - distMatrix[nodes[i].id][nodes[j].id]
            savings.append(Saving(nodes[i],nodes[j],value))
    return savings


def CheckEdgeNode(route, node):
    if(route.nodes[1].id == node.id or route.nodes[-2].id == node.id):
        return True
    else:
        return False

def CheckEdgeNodePosition(route, node):
    if (route.nodes[1].id == node.id):
        return 1
    elif (route.nodes[-2].id == node.id):
        return 2

def ConnectRoutes(route1, route2):
    id = route1.id
    route = route1.nodes[:-1]
    for i in range(1, len(route2.nodes)):
        route.append(route2.nodes[i])
    return Route(id, route)

def ReverseRoute(route):
    route.nodes.reverse()
    return route[1,:]

def UpdateRouteNodes(route):
    for node in route.nodes:
        node.route = route

nodes = CreateNodes(100)
distMatrix = CalculateDistMatrix(nodes)
capacity = 50
savings = CalculateSavingsMatrix(nodes, distMatrix)

#Create one route per customer
routes = []
for i in range(1,len(nodes)):
    route = Route(i-1,[nodes[0], nodes[nodes[i].id], nodes[0]])
    routes.append(route)
    nodes[nodes[i].id].route = route

savings.sort(key = lambda x: x.value, reverse=True)

for saving in savings:
    route1 = saving.i.route
    route2 = saving.j.route
    if (CheckEdgeNode(route1, saving.i) and CheckEdgeNode(route2, saving.j) and not (saving.i.isVisited and saving.j.isVisited) and saving.i.route.id != saving.j.route.id):
        if (route1.cost + route2.cost <= capacity):
            position1 = CheckEdgeNodePosition(route1, saving.i)
            position2 = CheckEdgeNodePosition(route2, saving.j)
            if position1 == 2 and position2 == 1:
                route = ConnectRoutes(route1, route2)
            elif position1 == 2 and position2 == 2:
                route2.nodes.reverse()
                route = ConnectRoutes(route1, route2)
            elif position1 == 1 and position2 == 1:
                route1.nodes.reverse()
                route = ConnectRoutes(route1, route2)
            elif position1 == 1 and position2 == 2:
                route = ConnectRoutes(route2, route1)
            UpdateRouteNodes(route)

finalRoutes = []
for i in range(1,len(nodes)):
    if nodes[i].route.isAdded == False:
        finalRoutes.append(nodes[i].route)
        nodes[i].route.isAdded = True

coords = []
solutionDist = 0
for route in finalRoutes:
    path = []
    solutionDist += route.distance
    for node in route.nodes:
        path.append([node.x, node.y])
    coords.append(path)

print(coords)
print(solutionDist)
PlotGraph(coords)