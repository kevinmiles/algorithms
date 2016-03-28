# graph_search.py

from collections import deque


def bfs(graph, source, visited_callback):
    agenda = deque([source])
    visited = set()
    while len(agenda) > 0:
        node = agenda.popleft()
        visited_callback(node)
        for child in graph[node]:
            if child not in visited:
                agenda.append(child)


def dfs(graph, source, visited_callback):
    agenda = deque([source])
    visited = set()
    while len(agenda) > 0:
        node = agenda.pop()
        visited_callback(node)
        for child in graph[node]:
            if child not in visited:
                agenda.append(child)
