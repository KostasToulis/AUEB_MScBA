import math
import numpy as np
import matplotlib.pyplot as plt
from sol_checker import calculate_route_details

def CalculateDistance(node1, node2):
   return math.sqrt((node1.x - node2.x)**2 + (node1.y - node2.y)**2)

def CalculateDistMatrix(nodes):
   distMatrix = np.zeros((len(nodes),len(nodes)))
   for node1 in nodes:
      for node2 in nodes:
         distMatrix[node1.ID, node2.ID] = CalculateDistance(node1, node2)#/(node1.demand+1000)
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
         plt.plot(route[i-1], route[i], linewidth=1, marker='*', color=color)
   plt.show()


def CalculateSolutionCost(nodes, sol):
   # cost = 0
   # for route in sol:
   #     for i in range(1,len(route)):
   #         cost += CalculateDistance(nodes[i-1],nodes[i])*
   total_cost = 0
   for route in sol:
      nodes_sequence = [nodes[idd] for idd in route]
      rt_tn_km, rt_load = calculate_route_details(nodes_sequence, 6)
      total_cost += rt_tn_km
   return total_cost

def CalculateRouteCost(nodes,route):
   nodes_sequence = [nodes[idd] for idd in route]
   rt_tn_km, rt_load = calculate_route_details(nodes_sequence, 6)
   return rt_tn_km