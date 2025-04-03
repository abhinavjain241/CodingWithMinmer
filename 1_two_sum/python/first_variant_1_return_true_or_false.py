class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        seen = set()
        for num in enumerate(nums):
            diff = target - num
            if diff in seen:
                return True
            seen.add(num)
        return False
