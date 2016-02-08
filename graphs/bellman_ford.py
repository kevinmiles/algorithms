# bellman_ford.py

def relax(graph, costs, node, child):
    if costs[child] > costs[node] + graph[node][child]:
        costs[child] = costs[node] + graph[node][child]

def bellman_ford(graph, source):

    costs = {}
    for node in graph:
        costs[node] = float('Inf')
    costs[source] = 0

    for i in range(len(graph)-1):
        for node in graph:
            for child in graph[node]:
                relax(graph, costs, node, child)

    for node in graph:
        for child in graph[node]:
            if not costs[child] <= costs[node] + graph[node][child]:
                raise ValueError("graph has negative weight cycle")

    return costs

graph = {
        "a":
        }

