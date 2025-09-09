from collections import defaultdict

def has_cycle(V, edges):
    adj = defaultdict(list)
    for u, v in edges:
        adj[u].append(v)
        adj[v].append(u)
    visited = [False] * V
    for i in range(V):
        if not visited[i]:
            if is_cyclic_util(i, -1, adj, visited):
                return True
    return False

def is_cyclic_util(node, parent, adj, visited):
    visited[node] = True
    
    for neighbor in adj[node]:
        if not visited[neighbor]:
            if is_cyclic_util(neighbor, node, adj, visited):
                return True
        elif neighbor != parent:
            return True
            
    return False

V = 5
Edges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 0]]
print(has_cycle(V, Edges))
