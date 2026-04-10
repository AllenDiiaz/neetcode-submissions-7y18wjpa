class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        # nums = [1,2,4,6]

        zero_count = 0
        product_without_zero = 1

        for n in nums:
            if n == 0:
                zero_count += 1
            else:
                product_without_zero = n * product_without_zero

        res = []
        for n in nums:
            if zero_count > 1:
                res.append(0)
            elif zero_count == 1:
                if n == 0:
                    res.append(product_without_zero)
                if n != 0:
                    res.append(0)
            elif zero_count == 0:
                res.append(product_without_zero//n)
        return res


        