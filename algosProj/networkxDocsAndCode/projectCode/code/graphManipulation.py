import networkx as nx
import random
import numpy as np


def selectTargets(graph, noOfTargets):
    np.random.seed(10)
    nodes = graph.nodes()
    return [np.random.choice(nodes) for i in range(noOfTargets)]

def fakeNodesExternalDegrees(graph, w, d0, d1):
    externalDergrees = {}
    for node in w:
        externalDergrees[node] = np.random.randint(d0, d1)
    return externalDergrees

def createrGraphByAddingNodes(graph, k, w, externalDergrees):
    print(externalDergrees)
    return graph