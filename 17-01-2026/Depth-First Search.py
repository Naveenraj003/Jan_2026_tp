def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()

    visited.add(start)
    print(start, end=" ")

    for neighbor in graph[start]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)


if __name__ == "__main__":
    graph = {
        0: [1, 2],
        1: [0, 3],
        2: [0],
        3: [1]
    }

    print("DFS Traversal:")
    dfs(graph, 0)
