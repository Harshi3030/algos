import networkx as nx
import random

def createFakeNodesGraphWithInternalNodes(k, externalDergrees, graph):
    fakeNodeGraph = nx.Graph()
    nodes = graph.nodes()
    maxNodeNum = max(nodes)
    nodesTheFakeMutsConnectWithin = {}
    
    for node in range(k):
        nodesTheFakeMutsConnectWithin[maxNodeNum + node + 2] = []
    for node1 in nodesTheFakeMutsConnectWithin:
        for node2 in nodesTheFakeMutsConnectWithin:
            if node1 != node2:
                if random.randint(0,1) == 1:
                    nodesTheFakeMutsConnectWithin[node1].append(node2)

    return fakeNodeGraph

def createGraphWithEdgesInPath(dataPath):
    graph = nx.Graph()
    # nodes = []
    for edge in open(dataPath, "r").read().split("\n"):
        splits = edge.strip().split(" ")
        if len(splits) == 2:
            graph.add_edge(int(splits[0]), int(splits[1]))
            # if splits[0] not in nodes:
            #     nodes.append(splits[0])
            # if splits[1] not in nodes:
            #     nodes.append(splits[1])
    # print(nodes)
    return graph