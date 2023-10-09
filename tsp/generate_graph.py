import random
import numpy as np
import matplotlib.pyplot as plt

class Node:
    def __init__(self, id, x , y):
        self.id = id
        self.x = x
        self.y = y

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

# nodesNum = 20
# # while (nodesNum <= 0 or nodesNum > 100):
# #     nodesNum = int(input("Give value for number of nodes:"))
#
# nodes = CreateNodes(nodesNum)
# coords = np.array([[i.x, i.y] for i in nodes])
# plt.plot(coords[:,0], coords[:,1], linewidth = 0, marker='*', color='blue')
# plt.show()