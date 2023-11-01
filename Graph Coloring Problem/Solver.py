from BuildInput import Build_Graph
from Setup import Node, Colour


def UpdateRestrictions(node, colour):
    for restriction in node.neighbors:
        colour.forbidden_nodes.add(restriction)

def FindBestColour(node, colours):
    minRestrictions = 1000000
    minColour = None
    for colour in colours:
        if (node.id in colour.forbidden_nodes):
            pass
        else:
            newRestrictions = set()
            for i in node.neighbors:
                newRestrictions.add(i)
            if len(newRestrictions) < minRestrictions:
                minRestrictions = len(newRestrictions)
                minColour = colour
    return minColour

nodes = Build_Graph()
colours = [Colour(1)]

nodes.sort(key = lambda x: len(x.neighbors), reverse = True)

for node in nodes:
    colour = FindBestColour(node, colours)
    if colour:
        # colour.forbidden_nodes.add(node.id)
        UpdateRestrictions(node, colour)
        colour.assigned_nodes.append(node)
    else:
        colours.append(Colour(len(colours)+1))
        colour = colours[-1]
        UpdateRestrictions(node, colour)
        colour.assigned_nodes.append(node)


for c in colours:
    print(c.id, c.assigned_nodes)