class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        for i in range(len(nums)):          # i : 0 ~ n-1
            for j in range(i+1,len(nums)):    # j : 1 ~ n-1

                if nums[i] == target - nums[j]:
                    return [i,j]
                else:
                    continue


        