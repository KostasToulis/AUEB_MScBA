class Item:
    def __init__(self, id, wt):
        self.id = id
        self.weight = wt
        self.assigned = False

class Bin:
    def __init__(self, id):
        self.id = id
        self.capacity = 150
        self.items = []
        self.load = 0

def UpdateBinLoad(bin):
    load = 0
    for i in bin.items:
        load += i.weight
    bin.load = load

def CalculateSolutionScore(bins):
    score = 0
    for bin in bins:
        score += bin.load**2
    return score