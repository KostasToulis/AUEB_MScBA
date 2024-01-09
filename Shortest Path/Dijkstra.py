from Setup import Node, Edge
from random import randint, choice, random

nodes = []
edges = []
for i in range(100):
    nodes.append(Node(i))

for node in nodes:
    if not node.connected:
        index = choice([i for i in range(100) if i not in [node.id]])
        neighbor = nodes[index]
        cost = random.randint(3,20)
        edges.append(Edge(node, neighbor, cost))
        node.neighbors.append(neighbor)
        neighbor.neighbors.append(node)