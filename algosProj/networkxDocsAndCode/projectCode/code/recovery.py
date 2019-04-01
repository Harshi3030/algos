import networkx

def getNodesWithDegree(startNodeTotalDegree, finalGraph):
    nodesArray = []
    for (node, degree) in finalGraph.degree():
        if(degree == startNodeTotalDegree):
            nodesArray.append(node)
    return nodesArray

def retreiveSubGraphs(nodesWithRequiredDegree, graph, totalDegrees):
    startNodeWithDegrees = []
    totalFakeNode = 
    index = 1
    for startNode in nodesWithRequiredDegree:
        nodesWithDegree  = [startNode]
        for degreee in totalDegrees[1:]:
            for node in nodesWithDegree:
                nodesWithDegree = getNeighborsrequiredDegree()
                if len(nodesWithDegree.values()) == 0:
                    break
            index += 1
            if index == len(totalDegrees):
                startNodeWithDegrees.append(startNode)
                break
    return startNodeWithDegrees
