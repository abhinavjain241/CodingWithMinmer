class Solution:
    def findBuildingsCount(self, heights: list[int]) -> list[int]:
        n = len(heights)
        max_so_far = heights[n - 1]
        count = 1
        for i in range(n - 2, -1, -1):
            if heights[i] > max_so_far:
                count += 1
                max_so_far = heights[i]
        return count
    
if __name__ == "__main__":
    solution = Solution()
    assert solution.findBuildingsCount([2, 5, 3, 10, 9, 8]) == 3