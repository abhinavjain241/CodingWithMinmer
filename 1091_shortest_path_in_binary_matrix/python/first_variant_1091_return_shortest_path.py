from collections import deque


class Solution:
    def shortestPathBinaryMatrix(self, grid: list[list[int]]) -> list[list[int]]:
        if grid[0][0] != 0:
            return []

        start = (0, 0)
        path = [[0, 0]]

        visited = set()
        queue = deque()

        queue.append((start, path))
        visited.add(start)

        n = len(grid)
        dirs = [(-1, -1), (-1, 0), (-1, 1), (0, 1), (0, -1), (1, 1), (1, 0), (1, -1)]

        def valid(x, y):
            return 0 <= x < n and 0 <= y < n

        while len(queue):
            curr, path = queue.popleft()
            cx, cy = curr
            if (cx, cy) == (n - 1, n - 1):
                return path
            for dx, dy in dirs:
                nx, ny = cx + dx, cy + dy
                if valid(nx, ny) and (nx, ny) not in visited and grid[nx][ny] == 0:
                    visited.add((nx, ny))
                    path_copy = path[:]
                    path_copy.append([nx, ny])
                    queue.append(((nx, ny), path_copy))
        return []


if __name__ == "__main__":
    s = Solution()
    assert s.shortestPathBinaryMatrix([[1, 0, 0], [1, 1, 0], [1, 1, 0]]) == []
    assert s.shortestPathBinaryMatrix([[0, 0, 0], [1, 1, 0], [1, 1, 0]]) == [
        [0, 0],
        [0, 1],
        [1, 2],
        [2, 2],
    ]
