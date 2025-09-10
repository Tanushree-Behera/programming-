from collections import deque

def build_adjacency_list(V, edges):
    adj = {i: [] for i in range(V)}
    for u, v in edges:
        adj[u].append(v)
        adj[v].append(u)  
    return adj

def shortest_path_length(V, edges, start, end):
    adj = build_adjacency_list(V, edges)
    
    if start == end:
        return 0
    
    queue = deque([(start, 0)]) 
    visited = {start}  
    
    while queue:
        current_node, distance = queue.popleft()
        
        if current_node == end:
            return distance
            
        for neighbor in adj[current_node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor, distance + 1))
                
    return -1

V = 5
edges = [[0, 1], [0, 2], [1, 3], [2, 3], [3, 4]]
start = 0
end = 4

path_length = shortest_path_length(V, edges, start, end)

print(f"The shortest path length from node {start} to node {end} is: {path_length}")
