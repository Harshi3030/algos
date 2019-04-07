import networkx

def getNodesWithDegree(startNodeTotalDegree, finalGraph):
    nodesArray = []
    for (node, degree) in finalGraph.degree():
        if(degree == startNodeTotalDegree):
            nodesArray.append(node)
    return nodesArray

def getNeighborsrequiredDegree(startNode, graph, degree):
    nodes = []
    neighbors = list(graph.neighbors(startNode))
    for node in neighbors:
        if (graph.degree(node) == degree):
            nodes.append(node)
    return nodes

def interDegreeOfNode(graph, node, path):
    degree = 0
    neighbors = list(graph.neighbors(node))
    # print(neighbors)
    for neighbor in neighbors:
        if neighbor in path:
            degree += 1
    return degree

def IsMatchingInternalStructure(graph, path, fakeNodesInteralDegrees):
    index = 0
    while index < len(fakeNodesInteralDegrees):
        # print("fakeNodesInteralDegrees")
        # print(fakeNodesInteralDegrees[index])
        # print("fakeNodesInteralDegrees len")
        # print(len(fakeNodesInteralDegrees[index]))
        # print("interDegreeOfNode")
        # print(interDegreeOfNode(graph, path[index], path))
        if len(fakeNodesInteralDegrees[index]) != interDegreeOfNode(graph, path[index], path):
            return False
        index += 1
    return True

def lookForInternalStructure(finalGraph, startNodeWithDegrees, fakeNodesInteralDegrees, paths):
    finalPaths = []
    for path in paths:
        if IsMatchingInternalStructure(finalGraph, path, fakeNodesInteralDegrees):
            finalPaths.append(path)
        # print("===========")
    return finalPaths

def isRequiredSubGraph(startNode, graph, totalDegrees, currDegreeIndex, path, pathDegree):
    path.append(startNode)
    pathDegree.append(graph.degree(startNode))
    if currDegreeIndex == len(totalDegrees):
        return True
    nodesWithDegree  = getNeighborsrequiredDegree(startNode, graph, totalDegrees[currDegreeIndex])
    if len(nodesWithDegree) == 0:
        return False
    for node in nodesWithDegree:
        if node not in path:
            if isRequiredSubGraph(node, graph, totalDegrees, currDegreeIndex+1, path, pathDegree):
                return True
            else:
                path.pop()
                pathDegree.pop()
    return False
            
def retreiveSubGraphs(nodesWithRequiredDegree, graph, totalDegrees):
    startNodeWithDegrees = []
    paths = []
    # print(nodesWithRequiredDegree)
    for startNode in nodesWithRequiredDegree:
        path = []
        pathDegree = []
        if(isRequiredSubGraph(startNode, graph, totalDegrees, 1, path, pathDegree)):
            startNodeWithDegrees.append(startNode)
            paths.append(path)
        #     print(path)
        #     print(pathDegree)
        # print("------")
    return [startNodeWithDegrees, paths]
