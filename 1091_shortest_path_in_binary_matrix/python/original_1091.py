from collections import deque


class Solution:
    def shortestPathBinaryMatrix(self, grid: list[list[int]]) -> int:
        if grid[0][0] != 0:
            return -1
        
        start = (0, 0)

        visited = set()
        queue = deque()

        queue.append((start, 1))
        visited.add(start)

        n = len(grid)
        dirs = [(-1, -1), (-1, 0), (-1, 1), (0, 1), (0, -1), (1, 1), (1, 0), (1, -1)]

        def valid(x, y):
            return 0 <= x < n and 0 <= y < n

        while len(queue):
            curr, dist = queue.popleft()
            cx, cy = curr
            if (cx, cy) == (n - 1, n - 1):
                return dist
            for dx, dy in dirs:
                nx, ny = cx + dx, cy + dy
                if valid(nx, ny) and (nx, ny) not in visited and grid[nx][ny] == 0:
                    visited.add((nx, ny))
                    queue.append((cx + dx, cy + dy), dist + 1)
        return -1
