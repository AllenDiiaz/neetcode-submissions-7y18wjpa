class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        # nums = [3,4,5,6], target = 7

        seen = {}

        for i in range(len(nums)):

            diff = target - nums[i]

            if diff in seen:
                return [seen[diff],i]
            else:
                seen[nums[i]] = i