class Subset:
    def __init__(self, id, lst):
        self.id = id
        # direct conversion of list to set
        self.coveredItems = set(lst)


def buildInput():
    subsets = []
    s = Subset(1, [1, 2])
    subsets.append(s)
    s = Subset(2, [1, 2, 3])
    subsets.append(s)
    s = Subset(3, [3, 4, 5, 6])
    subsets.append(s)
    s = Subset(4, [2, 3, 4, 9])
    subsets.append(s)
    s = Subset(5, [4, 5, 6, 8])
    subsets.append(s)
    s = Subset(6, [6, 7])
    subsets.append(s)
    s = Subset(7, [7, 8])
    subsets.append(s)
    s = Subset(8, [5, 7, 8, 10])
    subsets.append(s)
    s = Subset(9, [4, 8, 9])
    subsets.append(s)
    s = Subset(10, [8, 10])
    subsets.append(s)
    return subsets