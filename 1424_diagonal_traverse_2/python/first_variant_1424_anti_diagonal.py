from collections import deque


class Solution:
    def findAntiDiagonalOrder(self, nums: list[list[int]]) -> list[list[int]]:
        def is_valid(i, j):
            return i >= 0 and i < len(nums) and j >= 0 and j < len(nums[i])

        visited = set()
        queue = deque([(0, 0)])
        visited.add((0, 0))
        result = []
        while queue:
            queue_length = len(queue)
            curr_level = []
            for _ in range(queue_length):
                x, y = queue.popleft()
                curr_level.append(nums[x][y])
                neighbours = [(x, y + 1), (x + 1, y)]
                for nei in neighbours:
                    nx, ny = nei
                    if nei not in visited and is_valid(nx, ny):
                        visited.add(nei)
                        queue.append(nei)
            result.append(curr_level)

        return result


if __name__ == "__main__":
    solution = Solution()
    assert solution.findAntiDiagonalOrder([[1, 2, 3], [4, 5, 6], [7, 8, 9]]) == [
        [1],
        [2, 4],
        [3, 5, 7],
        [6, 8],
        [9],
    ]
    assert solution.findAntiDiagonalOrder(
        [[1, 2, 3, 4, 5], [6, 7], [8], [9, 10, 11], [12, 13, 14, 15, 16]]
    ) == [[1], [2, 6], [3, 7, 8], [4, 9], [5, 10, 12], [11, 13], [14], [15], [16]]
