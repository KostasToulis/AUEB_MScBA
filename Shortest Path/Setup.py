
class Node:
    def __init__(self, id):
        self.id = id
        self.neighbors = []
        self.visited = False
        self.distance = None
        self.connected = False

class Edge:
    def __init__(self, n1, n2, cost):
        self.id = str(n1.id) + " " + str(n2.id)
        self.n2 = n2
        self.n1 = n1
        self.cost = cost