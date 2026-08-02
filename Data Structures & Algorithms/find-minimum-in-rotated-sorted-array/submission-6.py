class Solution:
    def findMin(self, nums: List[int]) -> int:

        # nums = [3,4,5,6,1,2]

        left = 0
        right = len(nums) - 1

        # if mid > right -> left = mid + 1
        # if mid < right -> right = mid 

        while left < right :

            mid = left + (right-left) // 2

            if nums[mid] > nums[right]:
                left = mid + 1

            elif nums[mid] < nums[right]:
                right = mid

        return nums[left]
        