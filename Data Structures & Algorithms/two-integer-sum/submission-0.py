class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        # nums = [3,4,5,6], target = 7

        # 0 3
        # diff = 4
        # seen {3:0}

        # 1 4
        # diff = 3
        # diff in seen
        # return seen[3]=0 

        seen = {}

        for idx, val in enumerate(nums):

            diff = target - val

            if diff in seen:
                return [seen[diff],idx]
            else:
                seen[val] = idx 


        