import math
import random

import numpy as np
import matplotlib.pyplot as plt
from sol_checker import calculate_route_details


# class Route:
#    def __init__(self, ID, nodes):
#       self.ID = ID
#       self.nodes = nodes
#       self.cost = self.CalculateCost(nodes)
#       self.distance = self.CalculateRouteDistance(nodes)
#       self.isAdded = False

def CalculateDistance(node1, node2):
   return math.sqrt((node1.x - node2.x)**2 + (node1.y - node2.y)**2)

def CalculateDistMatrix(nodes):
   distMatrix = np.zeros((len(nodes),len(nodes)))
   for node1 in nodes:
      for node2 in nodes:
         distMatrix[node1.ID, node2.ID] = CalculateDistance(node1, node2)*(node1.demand+node2.demand)
   return distMatrix

def PlotInitial(nodes):
   plt.plot(nodes[0].x, nodes[0].y,linewidth=0, marker='*', color='red')
   for i in range(1,len(nodes)):
      plt.plot(nodes[i].x, nodes[i].y, linewidth=0, marker='*', color='blue')
   plt.show()


def PlotGraph(routes):
   for route in routes:
      # route = np.asarray(route, dtype=np.int_)
      color = np.random.rand(3, )
      for i in range(1,len(route)):
         plt.plot(route[i-1].x, route[i].y, linewidth=1, marker='*', color=color)
   plt.show()

def PlotRoute(route):
   xcoords, ycoords = ([node.x for node in route], [node.y for node in route])
   # ycoords = []
   # for node in route:
   #    xcoords.append(node.x)
   #    ycoords.append(node.y)
   plt.plot(xcoords, ycoords, linewidth=1, marker='*', color=np.random.rand(3,))
   # plt.show()

def CalculateSolutionCost(sol):
   total_cost = 0
   for route in sol:
      # nodes_sequence = [nodes[idd] for idd in route]
      rt_tn_km, rt_load = calculate_route_details(route, 6)
      total_cost += rt_tn_km
   return total_cost

def CalculateRouteCost(route):
   rt_tn_km, rt_load = calculate_route_details(route, 6)
   return rt_tn_km

def ReportSolution(sol, filename):
   totalCost = CalculateSolutionCost(sol)
   nodeIDs = []
   for route in sol:
      l = []
      for node in route:
         l.append(node.ID)
      nodeIDs.append(l)

   f = open(f"{filename}", "w")
   f.write("Cost:\n")
   f.write(str(totalCost))
   f.write("\nRoutes:\n")
   f.write(str(len(nodeIDs)))
   for route in nodeIDs:
      f.write("\n")
      for node in range(len(route)):
         f.write(str(route[node]))
         if node < len(route) - 1:
            f.write(",")