import createGraph as create
import graphManipulation as manipulate


k = 10 # k = no new fake accounts
w = 5 # w = no of targets
d0 = 5
d1 = 10
c = 3

def prepareGraph():
    graph = create.createGraphWithEdgesInPath("../data/edges.edges")
    # print(graph.number_of_edges())
    targetNodes = manipulate.selectTargets(graph, w)
    InteralDegreesAndNodes = manipulate.internaNodes(k, graph)
    fakeNodes = list(InteralDegreesAndNodes.keys())
    externalDergrees = manipulate.fakeNodesExternalDegrees(graph, fakeNodes, d0, d1)
    graph = create.addFakeNodesToGraphAndIntenalDergrees(graph, InteralDegreesAndNodes)
    return manipulate.appendFakeNodesToOrigianlNodes(graph, fakeNodes, targetNodes, externalDergrees, c)

def recovery(finalGraph):
    return finalGraph

finalGraph = prepareGraph()
recovery(finalGraph)