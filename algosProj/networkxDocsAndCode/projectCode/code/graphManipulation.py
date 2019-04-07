import networkx as nx
import random
import numpy as np

def internaNodes(k, graph):
    fakeNodes = []
    InteralDegreesAndNodes = []
    maxNodeNum = max(graph.nodes())
    InteralDegreesAndNodes = []
    for node in range(k):
        InteralDegreesAndNodes.append([])
        fakeNodes.append(maxNodeNum + node + 2)
    for node1 in fakeNodes:
        for node2 in fakeNodes:
            if node1 != node2:
                if random.randint(0,1) == 1:
                    InteralDegreesAndNodes[fakeNodes.index(node1)].append(node2)
    for node in fakeNodes[1:]:
        currIndex = fakeNodes.index(node)
        if fakeNodes[currIndex -1 ] not in  InteralDegreesAndNodes[currIndex]:
            InteralDegreesAndNodes[currIndex].append(fakeNodes[currIndex -1 ])
    return [fakeNodes, InteralDegreesAndNodes]

def removeEdgesForPrevention(finalGraph, percentageOfRemoval):
    removedEdgesGraph = nx.Graph()
    for u,v,w in finalGraph.edges(data=True):
        if random.randint(1, int(100/percentageOfRemoval)) != 1 :
            removedEdgesGraph.add_edge(u, v)
    return removedEdgesGraph

def selectTargets(graph, noOfTargets):
    np.random.seed(10)
    nodes = graph.nodes()
    targetNodes = []
    while len(targetNodes) < noOfTargets:
        node = np.random.choice(nodes) 
        if node not in targetNodes:
            targetNodes.append(node)
    return targetNodes

def fakeNodesExternalDegrees(graph, fakeNodes, d0, d1):
    externalDergrees = {}
    for node in fakeNodes:
        externalDergrees[node] = np.random.randint(d0, d1)
    return externalDergrees

def connectFakeNodesToTargetNodes(graph, fakeNodes, targetNodes, c):
    fakeAndTargetNodeEdges = []
    for fakeNode in fakeNodes:
        nodeIndex = fakeNodes.index(fakeNode)
        fakeAndTargetNodeEdges.append([])
        count = 0
        while(count < c):
            selectedTargetNode = np.random.choice(targetNodes)
            if selectedTargetNode not in fakeAndTargetNodeEdges[nodeIndex]:
                count += 1
                graph.add_edge(fakeNode,selectedTargetNode)
                fakeAndTargetNodeEdges[nodeIndex].append(selectedTargetNode)
    return [graph, fakeAndTargetNodeEdges]

def appendFakeNodesToOrigianlNodes(graph, fakeNodes, targetNodes, externalDergrees, c):
    # print(len(graph.edges()))
    # x = 0
    nodes = graph.nodes()
    externalDegreeEdges =[]
    for fakeNode in fakeNodes:
        nodeIndex = fakeNodes.index(fakeNode)
        externalDegreeEdges.append([])
        # x += externalDergrees[fakeNode]
        for externalEdge in range(externalDergrees[fakeNode]):
            while(1):
                externalNode = np.random.choice(nodes)
                if (externalNode not in targetNodes) and (externalNode not in fakeNodes) and (externalNode not in externalDegreeEdges[nodeIndex]):
                    graph.add_edge(fakeNode,externalNode)
                    externalDegreeEdges[nodeIndex].append(externalNode)
                    break
    # print(x)
    # print(len(graph.edges()))
    # print(externalDergrees)
    # print(externalDegreeEdges)
    
    [graph, fakeAndTargetNodeEdges] =  connectFakeNodesToTargetNodes(graph, fakeNodes, targetNodes, c)

    return [graph, externalDegreeEdges, fakeAndTargetNodeEdges]