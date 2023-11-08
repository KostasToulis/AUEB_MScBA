import random

class Item:
    def __init__(self, id, w, p):
        self.id = id
        self.weight = w
        self.profit = p
        self.chosen = False

class Container:
    def __init__(self, c):
        self.capacity = c
        self.items = []
        self.load = 0
        # self.CalculateLoad()

def CalculateLoad(container):
    load = 0
    for item in container.items:
        load += item.weight
    return load

def CreateItems(n, minProf, maxProf, minWeight, maxWeight):
    items = []
    for i in range(n):
        p = random.randint(minProf, maxProf)
        w = random.randint(minWeight, maxWeight)
        items.append(Item(i,w,p))
    return items

def CreateContainer(c):
    return Container(c)