class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        _list = set(nums)

        if len(_list) == len(nums):
            return False
        else:
            return True
        