from sol_checker import load_model, Node, calculate_route_details
from Setup import *
from ClarknWright import ClarknWrightSol
from LineSweep import LineSweep
from TabuSearch import *
from ModifiedNearestNeighbor import NearestNeighbor



nodes, capacity, weight = load_model("Instance.txt")
# PlotInitial(nodes)

# sol = ClarknWrightSol(nodes, 8)

sol = LineSweep(nodes, 8)

# for route in sol:
#     PlotRoute(route)
# plt.show()

routes = []
for route in sol:
    r = Route(capacity)
    r.sequenceOfNodes = route
    r.cost, r.load = calculate_route_details(route,weight)
    routes.append(r)


s = Solution()
s.cost = CalculateSolutionCost(sol)
s.routes = routes

ReportSolution(sol,"Solution.txt")

r = Solver(nodes, capacity, s)
sol = r.solve()