class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        ans = {}

        for idx, num in enumerate(nums):
            
            diff = target - num

            if diff in ans:
                return [idx, ans[diff]]
            else:
                ans[num] = idx