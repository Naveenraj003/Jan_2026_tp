from collections import deque

def shortest_path(grid):
    rows, cols = len(grid), len(grid[0])
    queue = deque([(0, 0, 0)])  # row, col, distance
    visited = set((0, 0))

    directions = [(1,0), (-1,0), (0,1), (0,-1)]

    while queue:
        r, c, dist = queue.popleft()

        if r == rows - 1 and c == cols - 1:
            return dist

        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 0:
                if (nr, nc) not in visited:
                    visited.add((nr, nc))
                    queue.append((nr, nc, dist + 1))

    return -1


if __name__ == "__main__":
    rows = int(input("Enter rows: "))
    grid = [list(map(int, input().split())) for _ in range(rows)]
    print("Shortest Path Length:", shortest_path(grid))
