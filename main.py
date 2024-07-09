
### 2. `main.py`

# ```python
"""
Assignment: Implement the most efficient algorithm to solve the given problem.

Problem Statement:
You are given a Directed Acyclic Graph (DAG) with `n` nodes, numbered from `0` to `n-1`.
The graph is represented as an adjacency list where `graph[i]` is a list of tuples `(j, w)`,
representing an edge from node `i` to node `j` with weight `w`. Your task is to find the longest
path in the graph starting from any node.

Function Signature:
def longest_path(graph: list) -> int:

Parameters:
- graph (list): A list of lists, where `graph[i]` contains tuples `(j, w)` representing an edge
  from node `i` to node `j` with weight `w`.

Returns:
- int: The length of the longest path in the graph.

Example:
>>> graph = [
...     [(1, 3), (2, 2)],
...     [(3, 4)],
...     [(3, 1)],
...     []
... ]
>>> longest_path(graph)
7
# """

def longest_path(graph: list) -> int:
    topo_order = topological_sort(graph)
    return calculate_longest_path(graph, topo_order)

def topological_sort(graph):
    from collections import deque
    
    indegree = [0] * len(graph)
    for u in range(len(graph)):
        for v, _ in graph[u]:
            indegree[v] += 1
    
    queue = deque([i for i in range(len(graph)) if indegree[i] == 0])
    topo_order = []
    
    while queue:
        u = queue.popleft()
        topo_order.append(u)
        for v, _ in graph[u]:
            indegree[v] -= 1
            if indegree[v] == 0:
                queue.append(v)
    return topo_order

def calculate_longest_path(graph, topo_order):
    dist = [-float('inf')] * len(graph)
    
    for node in topo_order:
        if dist[node] == -float('inf'):
            dist[node] = 0
    
    for node in topo_order:
        for neighbor, weight in graph[node]:
            if dist[neighbor] < dist[node] + weight:
                dist[neighbor] = dist[node] + weight

    return max(dist)

