class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        # nums = [1,2,4,6]
        # nums = [1,0,4,6]
        # nums = [1,2,0,0]
        n = len(nums)
        ans = [0]* n
        # based on zero_count by case
        zero_count = 0
        zero_idx = 0
        for idx, num in enumerate(nums):
            if num == 0:
                zero_count += 1
                zero_idx = idx
        # Case1: No zero
        if zero_count == 0:
            total_pruduct = 1
            for num in nums:
                total_pruduct = total_pruduct * num

            for idx, num in enumerate(nums):
                ans[idx] = total_pruduct // num
        # Case2: One zero
        # nums = [1,0,4,6]
        elif zero_count == 1:
            total_pruduct = 1
            for idx, num in enumerate(nums):
                if idx == zero_idx:
                    continue
                else:
                    total_pruduct = total_pruduct * num
            for idx, num in enumerate(nums):
                if idx == zero_idx:
                    ans[idx] = total_pruduct
                else:
                    ans[idx] = 0
        # Case3: > One zero
        # nums = [1,2,0,0]
        else:
            for i in range(n):
                ans[i] = 0

        return ans

        