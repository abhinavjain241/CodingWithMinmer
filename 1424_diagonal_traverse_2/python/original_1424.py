from collections import deque


class Solution:
    def findDiagonalOrder(self, nums: list[list[int]]) -> list[int]:
        def is_valid(i, j):
            return i >= 0 and i < len(nums) and j >= 0 and j < len(nums[i])

        visited = set()
        queue = deque([(0, 0)])
        visited.add((0, 0))
        result = [nums[0][0]]
        while queue:
            x, y = queue.popleft()
            neighbours = [(x + 1, y), (x, y + 1)]
            for nei in neighbours:
                nx, ny = nei
                if nei not in visited and is_valid(nx, ny):
                    visited.add(nei)
                    queue.append(nei)
                    result.append(nums[nx][ny])
        return result
