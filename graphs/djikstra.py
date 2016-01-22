# djikstra.py

import heapq

def relax(graph, costs, node, child):
    if costs[child] > costs[node] + graph[node][child]:
        costs[child] = costs[node] + graph[node][child]

def dijkstra(graph, source):

    costs = {}
    for node in graph:
        costs[node] = float('Inf')
        costs[source] = 0

    visited = set()
    queue = [(0, source)]

    while len(queue) > 0:
        node = heapq.heappop(queue)[1]
        for child in graph[node]:
            if child in visited:
                continue
            relax(graph, costs, node, child)
            heapq.heappush(queue, (costs[child], child))
            visited.add(node)

    return costs
