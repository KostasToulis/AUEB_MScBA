from sol_checker import load_model, Node
from Setup import CalculateDistMatrix, PlotInitial
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
ClarknWrightSol(nodes)