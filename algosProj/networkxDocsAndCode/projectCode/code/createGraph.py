import networkx as nx
import random

def addFakeNodesToGraphAndIntenalDergrees(graph, InteralDegreesAndNodes, fakeNodes):
    for node in fakeNodes:
        for connectingNode in InteralDegreesAndNodes[fakeNodes.index(node)]:
            graph.add_edge(node, connectingNode)
            if(node not in InteralDegreesAndNodes[fakeNodes.index(connectingNode)]):
                InteralDegreesAndNodes[fakeNodes.index(connectingNode)].append(node)
    return [graph, InteralDegreesAndNodes]

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