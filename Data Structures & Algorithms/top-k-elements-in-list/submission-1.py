class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        # nums = [1,2,2,3,3,3], k = 2

        # Construc dict. { Num: times ... }
        # Sorting for times
        # Return dict 's key

        seen = { }

        for key in nums:
            if key in seen:
                seen[key] += 1
            else:
                seen[key] = 1

        # seen = { 1:1, 2:2, 3:3 }
        sorted_nums = sorted(seen.items(),key = lambda item: item[1], reverse= True )

        # sorted_nums = [(1,1),(2,2),(3,3)]

        return [key[0] for key in sorted_nums[:k]]






