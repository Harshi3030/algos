import createGraph as create
import graphManipulation as manipulate


k = 10 # k = no new fake accounts
noOfTargets = 5 # w count
d0 = 5
d1 = 10
c = 3


graph = create.createGraphWithEdgesInPath("../data/edges.edges")
print(graph.number_of_edges())
w = manipulate.selectTargets(graph, noOfTargets)
externalDergrees = manipulate.fakeNodesExternalDegrees(graph, w, d0, d1)
fakeNodesGraph = create.createFakeNodesGraphWithInternalNodes(k, externalDergrees, graph)
manipulate.createrGraphByAddingNodes(graph, k, w, externalDergrees)
