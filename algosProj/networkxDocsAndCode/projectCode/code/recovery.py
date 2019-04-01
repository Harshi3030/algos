import networkx

def getNodesWithDegree(startNodeTotalDegree, finalGraph):
    nodesArray = []
    for (node, degree) in finalGraph.degree():
        if(degree == startNodeTotalDegree):
            nodesArray.append(node)
    return nodesArray