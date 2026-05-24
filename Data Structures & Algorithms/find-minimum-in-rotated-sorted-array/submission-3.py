class Solution:
    def findMin(self, nums: List[int]) -> int:

        # 建 left right 指針
        # 看 left 數值 跟 right 數值
        # 決定要往哪裡找
        # 如果 mid > right
        # 代表這是被 rotate 的 array
        # 所以要找最小值往右找
        # 如果 mid < right
        # 可能沒被 rotate 
        # 也可能這是在 最小的那一半了
        # 要注意不能讓 while left < = right
        # 不然 left = right 迴圈不會停止

        left = 0
        right = len(nums) - 1

        while left < right:
            mid = (left+right) // 2
            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid

        return nums[left]


        