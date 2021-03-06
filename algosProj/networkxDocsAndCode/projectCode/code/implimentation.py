import createGraph as create
import graphManipulation as manipulate
import graphDetails as details
import recovery as recover
import networkx as nx
import random 

def prepareGraph():
    print("preparing the graph for attack")
    # graph = create.createGraphWithEdgesInPath("../data/huge.edges") #facebook graph
    # graph = create.createGraphWithEdgesInPath("../data/Email-Enron.txt") #email graph
    graph = create.createGraphWithEdgesInPath("../data/twitter.edges") #twitter graph
    # graph = create.createGraphWithEdgesInPath("../data/Amazon.txt") #Amazon graph
    targetNodes = manipulate.selectTargets(graph, w) #array
    [fakeNodes, fakeNodesInteralDegrees] = manipulate.internaNodes(k, graph) #array , array of arrays
    externalDergrees = manipulate.fakeNodesExternalDegrees(graph, fakeNodes, d0, d1) #dict
    [graph, fakeNodesInteralDegrees] = create.addFakeNodesToGraphAndIntenalDergrees(graph, fakeNodesInteralDegrees, fakeNodes) # graph, array of arrays
    [graph, fakeNodesExternalDegrees, fakeAndTargetNodeEdges, cDict] = manipulate.appendFakeNodesToOrigianlNodes(graph, fakeNodes, targetNodes, externalDergrees, c) # graph, array of arrays, array of arrays
    return [graph, fakeNodesExternalDegrees, targetNodes, fakeNodesInteralDegrees, fakeNodes, fakeAndTargetNodeEdges, cDict]

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
k = 40 # k = no new fake accounts
w = 10 # w = no of targets
d0 = 5
d1 = 10
c = 3
[isPreventionImplimentation, percentageOfRemoval] = details.implentailDetails()
[finalGraph, fakeNodesExternalDegrees, targetNodes, fakeNodesInteralDegrees, fakeNodes, fakeAndTargetNodeEdges, cDict] = prepareGraph()
totalDegrees = details.calculatetotalDegrees(fakeNodesExternalDegrees, fakeNodesInteralDegrees, c, fakeNodes, cDict)
details.printInputs(isPreventionImplimentation, percentageOfRemoval, k, w, d0, d1, c)
details.printGraphDetails(finalGraph, fakeNodesExternalDegrees, fakeNodesInteralDegrees, fakeNodes, totalDegrees, fakeAndTargetNodeEdges, targetNodes)
if isPreventionImplimentation:
    finalGraph = manipulate.removeEdgesForPrevention(finalGraph, percentageOfRemoval)
finalPaths = recovery(finalGraph,fakeNodesExternalDegrees,fakeNodesInteralDegrees, fakeAndTargetNodeEdges, c, totalDegrees)
details.printResult(finalPaths, fakeNodes)