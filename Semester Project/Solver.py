from sol_checker import load_model, Node, calculate_route_details
from Setup import CalculateDistMatrix, PlotInitial, CalculateDistance, PlotGraph, CalculateSolutionCost
from ClarknWright import ClarknWrightSol

class Arc:
    def __init__(self, startx, starty, endx, endy, r):
        self.startx = startx
        self.starty = starty
        self.endx = endx
        self.endy = endy
        self.radius = r
        self.covered_nodes = []

# def Sweep(step, arc):





nodes, capacity, weigth = load_model("Instance.txt")
# PlotInitial(nodes)
sol = ClarknWrightSol(nodes, 8)
totalCost = CalculateSolutionCost(nodes, sol)

# PlotGraph(sol,nodes)
print(totalCost)
print(len(sol))

f = open("Solution.txt", "w")
f.write("Cost:\n")
f.write(str(totalCost))
f.write("\nRoutes:")
f.write(str(len(sol)))
for route in sol:
    f.write("\n")
    for node in range(len(route)):
        f.write(str(route[node]))
        if node < len(route)-1:
            f.write(",")

