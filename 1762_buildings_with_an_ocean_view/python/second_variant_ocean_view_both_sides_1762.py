class Solution:
    def findBuildingsWithOceanView(self, heights: list[int]) -> list[int]:
        left, right = 0, len(heights) - 1
        left_view = [left]
        right_view = [right]

        left_max = heights[left]
        right_max = heights[right]

        while left < right:
            if left_max < right_max:
                left += 1
                if heights[left] > left_max and left < right:
                    left_view.append(left)
                    left_max = heights[left]
            else:
                right -= 1
                if heights[right] > right_max and left < right:
                    right_view.append(right)
                    right_max = heights[right]
        return left_view + right_view[::-1]
        
    
if __name__ == "__main__":
    solution = Solution()
    assert solution.findBuildingsWithOceanView([2, 5, 3, 10, 9, 8]) == [0, 1, 3, 4, 5]