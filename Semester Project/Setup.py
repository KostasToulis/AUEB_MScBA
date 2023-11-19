import math
import numpy as np
import matplotlib.pyplot as plt

def CalculateDistance(node1, node2):
   return math.sqrt((node1.x - node2.x)**2 + (node1.y - node2.y)**2)

def CalculateDistMatrix(nodes):
   distMatrix = np.zeros((len(nodes),len(nodes)))
   for node1 in nodes:
      for node2 in nodes:
         distMatrix[node1.ID, node2.ID] = CalculateDistance(node1, node2)
   return distMatrix

def PlotInitial(nodes):
   plt.plot(nodes[0].x, nodes[0].y,linewidth=0, marker='*', color='red')
   for i in range(1,len(nodes)):
      plt.plot(nodes[i].x, nodes[i].y, linewidth=0, marker='*', color='blue')
   plt.show()


def PlotGraph(routes):
   for route in routes:
      route = np.asarray(route, dtype=np.int_)
      plt.plot(route[:, 0], route[:, 1], linewidth=1, marker='*', color=np.random.rand(3, ))
   plt.show()