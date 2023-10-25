import random
from Setup import Item, Bin, UpdateBinLoad, CalculateSolutionScore

class Slack:
    def __init__(self, binId, val):
        self.binId = binId
        self.value = val

def FindBestBin(bins,item):
    slacks = []
    for bin in bins:
        slacks.append(bin.capacity-bin.load-item.weight)
    minSlack = 10000
    minPos = -1
    for i in range(len(slacks)):
        if (slacks[i]< minSlack and slacks[i]>=0):
            minSlack = slacks[i]
            minPos = i
    if(minPos!=-1):
        return bins[minPos]
    return False

random.seed(1)
items = []
for i in range(100):
    items.append(Item(i,random.randint(5,100)))

items.sort(key = lambda x: x.weight, reverse = True)

bins = [Bin(0)]
for item in items:
    bin = FindBestBin(bins, item)
    if (not bin):
        bins.append(Bin(len(bins)))
        bins[-1].items.append(item)
        UpdateBinLoad(bins[-1])
        item.assigned = True
    else:
        bin.items.append(item)
        UpdateBinLoad(bin)
        item.assigned = True

print("Number of bins to store 1000 items with best fit algorithm:", len(bins))
print("Solution score: ", CalculateSolutionScore(bins))
