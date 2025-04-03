class Solution:
    def clearPathBinaryMatrix(self, grid: list[list[int]]) -> list[list[int]]:
        if grid[0][0] != 0:
            return []

        dirs = [(-1, -1), (-1, 0), (-1, 1), (0, 1), (0, -1), (1, 1), (1, 0), (1, -1)]
        
        visited = set()
        visited.add((0, 0))
        path = [(0, 0)]

        n = len(grid)

        def valid(x, y):
            return 0 <= x < n and 0 <= y < n

        def dfs(i, j):
            nonlocal path
            if (i, j) == (n - 1, n - 1):
                return
            for dx, dy in dirs:
                nx, ny = i + dx, j + dy
                if valid(nx, ny) and grid[nx][ny] == 0 and (nx, ny) not in visited:
                    path.append((nx, ny))
                    visited.add((nx, ny))
                    dfs(nx, ny)
            return
            
        dfs(0, 0)
        return path

if __name__ == "__main__":
    s = Solution()
    print(s.clearPathBinaryMatrix([[0, 0, 0], [1, 1, 0], [1, 1, 0]]))