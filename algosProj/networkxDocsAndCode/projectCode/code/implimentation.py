import createGraph as create
import graphManipulation as manipulate
import graphDetails as details
import recovery as recover
import networkx as nx
import random 

def prepareGraph():
    print("preparing the graph for attack")
    graph = create.createGraphWithEdgesInPath("../data/huge.edges") #graph
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
    [startNodeWithDegrees, paths] = recover.retreiveSubGraphs(nodesWithRequiredDegree, finalGraph, totalDegrees)
    # print("paths")
    # print(paths)
    # print("------------------------------------------------------------------------------------------------------------")
    # print("start node", str(startNodeWithDegrees))
    # print("------------------------------------------------------------------------------------------------------------")
    if(len(startNodeWithDegrees) > 1):
        finalPaths = recover.lookForInternalStructure(finalGraph, startNodeWithDegrees, fakeNodesInteralDegrees, paths)
    else:
        finalPaths = paths
    return finalPaths

#########################################################################################################
k = 10 # k = no new fake accounts
w = 10 # w = no of targets
d0 = 5
d1 = 10
c = 3
[isPreventionImplimentation, percentageOfRemoval] = details.implentailDetails()
[finalGraph, fakeNodesExternalDegrees, targetNodes, fakeNodesInteralDegrees, fakeNodes, fakeAndTargetNodeEdges] = prepareGraph()
totalDegrees = details.calculatetotalDegrees(fakeNodesExternalDegrees, fakeNodesInteralDegrees, c, fakeNodes)
details.printInputs(isPreventionImplimentation, percentageOfRemoval, k, w, d0, d1, c)
# details.printGraphDetails(finalGraph, fakeNodesExternalDegrees, fakeNodesInteralDegrees, fakeNodes, totalDegrees, fakeAndTargetNodeEdges, targetNodes)
if isPreventionImplimentation:
    finalGraph = manipulate.removeEdgesForPrevention(finalGraph, percentageOfRemoval)
finalPaths = recovery(finalGraph,fakeNodesExternalDegrees,fakeNodesInteralDegrees, fakeAndTargetNodeEdges, c, totalDegrees)
details.printResult(finalPaths, fakeNodes)