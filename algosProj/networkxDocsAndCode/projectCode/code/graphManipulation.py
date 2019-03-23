import networkx as nx
import random
import numpy as np

def internaNodes(k, graph):
    maxNodeNum = max(graph.nodes())
    InteralDegreesAndNodes = {}
    for node in range(k):
        InteralDegreesAndNodes[maxNodeNum + node + 2] = []
    for node1 in InteralDegreesAndNodes:
        for node2 in InteralDegreesAndNodes:
            if node1 != node2:
                if random.randint(0,1) == 1:
                    InteralDegreesAndNodes[node1].append(node2)
    return InteralDegreesAndNodes

def selectTargets(graph, noOfTargets):
    np.random.seed(10)
    nodes = graph.nodes()
    return [np.random.choice(nodes) for i in range(noOfTargets)]

def fakeNodesExternalDegrees(graph, fakeNodes, d0, d1):
    externalDergrees = {}
    for node in fakeNodes:
        externalDergrees[node] = np.random.randint(d0, d1)
    return externalDergrees

def appendFakeNodesToOrigianlNodes(graph, fakeNodes, targetNodes, externalDergrees, c):
    x = 0
    nodes = graph.nodes()
    externalDegreeEdges ={}
    for fakeNode in fakeNodes:
        externalDegreeEdges[fakeNode] = []
        x += externalDergrees[fakeNode]
        for externalEdge in range(externalDergrees[fakeNode]):
            while(1):
                externalNode = np.random.choice(nodes)
                if externalNode not in targetNodes and externalNode not in targetNodes:
                    graph.add_edge(fakeNode,externalNode)
                    externalDegreeEdges[fakeNode].append(externalNode)
                    break
    print(len(graph.edges()))
    return graph