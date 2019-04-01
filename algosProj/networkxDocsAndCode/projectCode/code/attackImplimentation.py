import createGraph as create
import graphManipulation as manipulate
import recovery as recover


k = 10 # k = no new fake accounts
w = 10 # w = no of targets
d0 = 5
d1 = 10
c = 3

def prepareGraph():
    print("preparing the graph for attack")
    graph = create.createGraphWithEdgesInPath("../data/edges.edges") #graph
    targetNodes = manipulate.selectTargets(graph, w) #array
    [fakeNodes, fakeNodesInteralDegrees] = manipulate.internaNodes(k, graph) #array , array of arrays
    externalDergrees = manipulate.fakeNodesExternalDegrees(graph, fakeNodes, d0, d1) #dict
    [graph, fakeNodesInteralDegrees] = create.addFakeNodesToGraphAndIntenalDergrees(graph, fakeNodesInteralDegrees, fakeNodes) # graph, array of arrays
    [graph, fakeNodesExternalDegrees, fakeAndTargetNodeEdges] = manipulate.appendFakeNodesToOrigianlNodes(graph, fakeNodes, targetNodes, externalDergrees, c) # graph, array of arrays, array of arrays
    return [graph, fakeNodesExternalDegrees, targetNodes, fakeNodesInteralDegrees, fakeNodes, fakeAndTargetNodeEdges]

def recovery(finalGraph,fakeNodesExternalDegrees,fakeNodesInteralDegrees, fakeAndTargetNodeEdges, c, totalDegrees):
    print("Recovery Process started")
    startDegree = totalDegrees[0]
    nodesWithRequiredDegree = recover.getNodesWithDegree(startDegree, finalGraph)
    startNodeWithDegrees = recover.retreiveSubGraphs(nodesWithRequiredDegree, finalGraph, totalDegrees)
    print("start node", str(startNodeWithDegrees))
    return len(startNodeWithDegrees)

def calculatetotalDegrees(fakeNodesExternalDegrees, fakeNodesInteralDegrees, c, fakeNodes):
    totalDegrees =[]
    for node in fakeNodes:
        index = fakeNodes.index(node)
        totalDegrees.append(c + len(fakeNodesExternalDegrees[index]) + len(fakeNodesInteralDegrees[index]))
    return totalDegrees

[finalGraph, fakeNodesExternalDegrees, targetNodes, fakeNodesInteralDegrees, fakeNodes, fakeAndTargetNodeEdges] = prepareGraph()
totalDegrees = calculatetotalDegrees(fakeNodesExternalDegrees, fakeNodesInteralDegrees, c, fakeNodes)

print("Final Edges:")
print(finalGraph.edges())
print("------------------------------------------------------------------------------------------------------------")
print("Final Nodes:")
print(finalGraph.nodes())
print("------------------------------------------------------------------------------------------------------------")
print("fakeNodesExternalDegrees:")
print(fakeNodesExternalDegrees)
print("------------------------------------------------------------------------------------------------------------")
print("targetNodes:")
print(targetNodes)
print("------------------------------------------------------------------------------------------------------------")
print("fakeNodesInteralDegrees:")
print(fakeNodesInteralDegrees)
print("------------------------------------------------------------------------------------------------------------")
print("fakeNodes:")
print(fakeNodes)
print("------------------------------------------------------------------------------------------------------------")
print("total degree")
print(totalDegrees)
print("------------------------------------------------------------------------------------------------------------")
print("fakeAndTargetNodeEdges:")
print(fakeAndTargetNodeEdges)
print("------------------------------------------------------------------------------------------------------------")

startNodeWithDegrees = recovery(finalGraph,fakeNodesExternalDegrees,fakeNodesInteralDegrees, fakeAndTargetNodeEdges, c, totalDegrees)