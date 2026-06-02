class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        rel = []
        nums.sort()

        for i in range(len(nums)):

            if i > 0 and nums[i] == nums[i-1]:
                continue

            Fix = nums[i]
            left = i + 1
            right = len(nums) - 1

            while left < right :

                ans = nums[left] + nums[right] 

                if ans < -Fix:
                    left += 1
                elif ans > - Fix:
                    right -= 1
                else:
                    rel.append([nums[i],nums[left],nums[right]])
                    left += 1
                    right -= 1
                    while left < right and nums[left] == nums[left-1]:
                        left += 1

        return rel

















        