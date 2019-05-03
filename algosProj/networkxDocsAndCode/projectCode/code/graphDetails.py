def printInputs(isPreventionImplimentation, percentageOfRemoval, k, w, d0, d1, c):
    print("------------------------------------------------------------------------------------------------------------")
    print("is Prevention Implimentation ",isPreventionImplimentation)
    print("percentage Of Removal ", str(percentageOfRemoval))
    print("k ", str(k))
    print("w", str(w))
    print("d0 ", str(d0))
    print("d1 ", str(d1))
    print("c ", str(c))
    print("------------------------------------------------------------------------------------------------------------")
    return
def implentailDetails():
    print("Choose implimentation type:")
    print("1: Attack")
    print("2: Prevention")
    implimentationType = int(input())
    percentage = 0
    if implimentationType == 2:
        percentage = int(input("Prevention percentage"))
    elif implimentationType != 1:
        print("incorrect input")
        exit()
    return [implimentationType==2, percentage]

def calculatetotalDegrees(fakeNodesExternalDegrees, fakeNodesInteralDegrees, c, fakeNodes, cDict):
    totalDegrees =[]
    for node in fakeNodes:
        index = fakeNodes.index(node)
        if cDict == {}:
            totalDegrees.append(c + len(fakeNodesExternalDegrees[index]) + len(fakeNodesInteralDegrees[index]))
        else:
            totalDegrees.append(cDict[node] + len(fakeNodesExternalDegrees[index]) + len(fakeNodesInteralDegrees[index]))
    return totalDegrees

def printGraphDetails(finalGraph, fakeNodesExternalDegrees, fakeNodesInteralDegrees, fakeNodes, totalDegrees, fakeAndTargetNodeEdges, targetNodes):
    print("Final Edges:")
    print(finalGraph.edges())
    print("------------------------------------------------------------------------------------------------------------")
    print("Final Nodes:")
    print(finalGraph.nodes())
    print("------------------------------------------------------------------------------------------------------------")
    print("fakeNodesExternalDegrees:")
    print(fakeNodesExternalDegrees)
    print("------------------------------------------------------------------------------------------------------------")
    print("targetNodes:")
    print(targetNodes)
    print("------------------------------------------------------------------------------------------------------------")
    print("fakeNodesInteralDegrees:")
    print(fakeNodesInteralDegrees)
    print("------------------------------------------------------------------------------------------------------------")
    print("fakeNodes:")
    print(fakeNodes)
    print("------------------------------------------------------------------------------------------------------------")
    print("total degree")
    print(totalDegrees)
    print("------------------------------------------------------------------------------------------------------------")
    print("fakeAndTargetNodeEdges:")
    print(fakeAndTargetNodeEdges)
    print("------------------------------------------------------------------------------------------------------------\n\n\n\n")
    return 

def printResult(finalPaths, fakeNodes):
    print("**************")
    if len(finalPaths) >= 1:
        print("Retrived nodes\n")
        print(finalPaths)
        print("\nFake nodes\n")
        print(fakeNodes)

    if len(finalPaths) == 1:
        print("verifying graph")
        print(sorted(finalPaths[0]) == sorted(fakeNodes))
    elif len(finalPaths) == 0:
        print("no graph retreived")
    else:
        print("multiple graphs")
