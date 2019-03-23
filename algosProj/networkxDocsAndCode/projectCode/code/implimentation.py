import createGraph as create
import graphManipulation as manipulate


k = 10 # k = no new fake accounts
w = 10 # w = no of targets
d0 = 5
d1 = 10
c = 3

def prepareGraph():
    graph = create.createGraphWithEdgesInPath("../data/edges.edges")
    targetNodes = manipulate.selectTargets(graph, w)
    fakeNodesInteralDegrees = manipulate.internaNodes(k, graph)
    fakeNodes = list(fakeNodesInteralDegrees.keys())
    externalDergrees = manipulate.fakeNodesExternalDegrees(graph, fakeNodes, d0, d1)
    graph = create.addFakeNodesToGraphAndIntenalDergrees(graph, fakeNodesInteralDegrees)
    [graph, fakeNodesExternalDegrees, fakeAndTargetNodeEdges] = manipulate.appendFakeNodesToOrigianlNodes(graph, fakeNodes, targetNodes, externalDergrees, c)
    return [graph, fakeNodesExternalDegrees, targetNodes, fakeNodesInteralDegrees, fakeNodes, fakeAndTargetNodeEdges]

def recovery(finalGraph):
    return finalGraph

[finalGraph, fakeNodesExternalDegrees, targetNodes, fakeNodesInteralDegrees, fakeNodes, fakeAndTargetNodeEdges] = prepareGraph()
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
print("fakeAndTargetNodeEdges:")
print(fakeAndTargetNodeEdges)
print("------------------------------------------------------------------------------------------------------------")
recovery(finalGraph)