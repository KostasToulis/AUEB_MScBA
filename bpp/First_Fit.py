import random
from Setup import Item, Bin, UpdateBinLoad


def ExistsAvailableBin(bins,item):
    for bin in bins:
        if (bin.capacity-bin.load >= item.weight):
            return bin
    return False

random.seed(1)
items = []
for i in range(1000):
    items.append(Item(i,random.randint(50,100)))

items.sort(key = lambda x: x.weight, reverse = True)

bins = [Bin(0)]
for item in items:
    bin = ExistsAvailableBin(bins, item)
    if (not bin):
        bins.append(Bin(len(bins)))
        bins[-1].items.append(item)
        UpdateBinLoad(bins[-1])
        item.assigned = True
    else:
        bin.items.append(item)
        UpdateBinLoad(bin)
        item.assigned = True

print("Number of bins to store 1000 items with first fit algorithm:", len(bins))