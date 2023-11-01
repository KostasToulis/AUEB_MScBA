class Node:
    def __init__(self, id):
        self.id = id
        self.neighbors = set()

class Colour:
    def __init__(self, id):
        self.id = id
        self.forbidden_nodes = set()
        self.assigned_nodes = []

