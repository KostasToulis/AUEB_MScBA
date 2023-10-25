from generate_graph import CreateNodes, PlotGraph, Node, SelectStartNode, CalculateDistMatrix, CalculateSolutionDistance
import time

def SelectClosestNeighbor(distMatrix, targetNode, nodes):
   neighbors = distMatrix[targetNode.id]
   min = 1000000
   minIndex = -1
   for i,dist in enumerate(neighbors):
      if (dist < min and dist != 0 and not nodes[i].isVisited):
         min = dist
         minIndex = i
   return minIndex

nodes = CreateNodes(100)
sortedNodes = []
distMatrix = CalculateDistMatrix(nodes)
startNode = SelectStartNode(nodes)
sortedNodes.append(startNode)
startTime = time.time()
nextNode = nodes[SelectClosestNeighbor(distMatrix, startNode, nodes)]
while len(sortedNodes) < len(nodes):
   sortedNodes.append(nextNode)
   nextNode = nodes[SelectClosestNeighbor(distMatrix, nextNode, nodes)]
   nextNode.isVisited = True
sortedNodes.append(startNode)

endTime = time.time()
print('Nearest neighbor time elapsed: ', endTime-startTime)
print('Nearest neighbor solution distance: ', CalculateSolutionDistance(sortedNodes))
sortedNodes.append(startNode)
PlotGraph(sortedNodes)



