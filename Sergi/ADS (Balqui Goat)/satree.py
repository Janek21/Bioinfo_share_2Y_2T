def is_tree(adj_list):
    n = len(adj_list)
    visited = [False] * n
    parent = [-1] * n
    
    def dfs(node, par):
        visited[node] = True
        parent[node] = par
        for neighbor in adj_list[node]:
            if not visited[neighbor]:
                if dfs(neighbor, node):
                    return True
            elif neighbor != par:
                return True
        return False
    
    # Check if there's a cycle
    if dfs(0, -1):
        return False
    
    # Check if all nodes are reachable
    if False in visited:
        return False
    
    # Check if the graph is connected
    for i in range(n):
        if len(adj_list[i]) == 0 and i != 0:
            return False
    
    return True

# Read input
while True:
    try:
        n = int(input())
        adj_list = [[] for _ in range(n)]
        for i in range(n):
            neighbors = list(map(int, input().split()))[1:]
            adj_list[i].extend(neighbors)
        
        # Check if the graph is a tree or not
        if is_tree(adj_list):
            print("is a tree")
        else:
            print("is NOT a tree")
    
    except EOFError:
        break
