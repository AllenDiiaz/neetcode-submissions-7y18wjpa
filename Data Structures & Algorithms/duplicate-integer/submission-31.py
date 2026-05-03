class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        # Brute Force

        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i] == nums[j]:
                    return True
                else:
                    continue
        return False
        
        # nums = [1, 2, 3, 3]
        #         i. j