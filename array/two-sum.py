class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:

        map = {}

        for idx, val in enumerate(nums):
            diff = target - val

            if diff in map:
                return [idx, map[diff]]
            
            map[val] = idx
                     