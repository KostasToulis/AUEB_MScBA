import math
from sol_checker import Node
from ModifiedNearestNeighbor import NearestNeighbor
from Setup import ReportSolution

class Line:
    def __init__(self):
        self.covered_nodes = []
        self.cost = 0

def calculate_angle(o, p):
    # Calculate the vector OP
    vector_op = [p.x - o.x, p.y - o.y]

    # Calculate the angle in radians using the arctangent function
    angle_radians = math.atan2(vector_op[1], vector_op[0])
    angle_radians = math.degrees(angle_radians)
    return angle_radians

def CalculateNodeDegree(nodes, depot):
    # reference = Node(-1, 200, 20, 0)
    for i in range(len(nodes)):
        nodes[i].degree = calculate_angle(depot, nodes[i])
    return nodes

def LineSweep(nodes, cap):
    depot = nodes[0]
    nodes = CalculateNodeDegree(nodes, depot)
    nodes.sort(key=lambda x: x.degree, reverse=True)
    routes = []
    route = Line()
    route.covered_nodes.append(depot)
    for node in nodes:
        if route.cost+node.demand <= cap and not node.isRouted:
            route.covered_nodes.append(node)
            route.cost += node.demand
            node.isRouted = True
        else:
            routes.append(route.covered_nodes)
            route = Line()
            route.covered_nodes.append(depot)
            route.covered_nodes.append(node)
            route.cost += node.demand
            node.isRouted = True
    routes.append(route.covered_nodes)

    # ReportSolution(routes,"Sweep.txt")
    sortedSol = []
    for route in routes:
        sortedRoute = NearestNeighbor(route)
        if(sortedRoute[0]==sortedRoute[-1]):
            sortedRoute.pop()
        sortedSol.append(sortedRoute)
    return sortedSol