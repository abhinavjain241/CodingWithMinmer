class Solution:
    def printAntiDiagonalOrder(self, nums: list[list[int]]) -> list[list[int]]:
        def helper(nums, row, col):
            res = []
            while row < len(nums) and col >= 0:
                res.append(nums[row][col])
                row += 1
                col -= 1

        for col in range(len(nums[0])):
            helper(nums, 0, col)
        for row in range(1, len(nums)):
            helper(nums, row, len(nums[0]) - 1)


if __name__ == "__main__":
    solution = Solution()
    solution.printAntiDiagonalOrder([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    solution.printAntiDiagonalOrder(
        [[1, 2, 3, 4, 5], [6, 7], [8], [9, 10, 11], [12, 13, 14, 15, 16]]
    )
