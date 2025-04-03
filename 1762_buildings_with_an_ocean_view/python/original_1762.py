class Solution:
    def findBuildings(self, heights: list[int]) -> list[int]:
        n = len(heights)
        max_so_far = heights[n - 1]
        res = [n - 1]
        for i in range(n - 2, -1, -1):
            if heights[i] > max_so_far:
                res.append(i)
                max_so_far = heights[i]
        return res[::-1]