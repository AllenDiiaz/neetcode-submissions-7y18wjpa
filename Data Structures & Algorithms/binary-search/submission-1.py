class Solution:
    def search(self, nums: List[int], target: int) -> int:

        # nums = [-1,0,2,4,6,8], target = 4

        # 設 left right 指針
        # 開始找 mid
        # mid > target 太大了往左找 left & mid-1 (新的right)
        # mid < target 太小了往右找 mid+1 & right (新的left)
        # mid == target return idx
        # 不然就繼續找 mid
        # 如果沒找到 return -1 (left<=right)

        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = (left+right) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                right = mid- 1
            elif nums[mid] < target:
                left = mid + 1

        return -1







         