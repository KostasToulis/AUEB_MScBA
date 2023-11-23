from sol_checker import load_model, Node, calculate_route_details
from Setup import *
from ClarknWright import ClarknWrightSol
from LineSweep import LineSweep
from ModifiedNearestNeighbor import NearestNeighbor



nodes, capacity, weigth = load_model("Instance.txt")
# PlotInitial(nodes)

# sol = ClarknWrightSol(nodes, 8)

sol = LineSweep(nodes, 8)

for route in sol:
    PlotRoute(route)
plt.show()

ReportSolution(sol,"Solution.txt")


