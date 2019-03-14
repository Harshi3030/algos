import networkx as nx

def createGraphWithEdgesInPath(dataPath):
    graph = nx.Graph()
    for edge in open(dataPath, "r").read().split("\n"):
        splits = edge.strip().split(" ")
        if len(splits) == 2: graph.add_edge(splits[0], splits[1])
    return graph