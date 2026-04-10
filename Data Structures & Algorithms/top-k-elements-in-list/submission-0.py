class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        # nums = [1,2,2,3,3,3], k = 2
        # key = 1 seen[1] = 1 => seen {1:1}
        # key = 2 seen[2] = 1 => seen {1:1,2:1}
        # key = 2 seen[2] += 1 => seen {1:1,2:2}
        # key = 3 seen[3] = 1 => seen {1:1,2:2,3:1}
        # key = 3 seen[3] += 1 => seen {1:1,2:2,3:2}
        # key = 3 seen[3] += 1 => seen {1:1,2:2,3:3}
        
        seen = {}

        for key in nums:
            if key in seen:
                seen[key] += 1
            else:
                seen[key] = 1

        sorted_item  = sorted(seen.items(),key =lambda item: item[1], reverse=True)

        return [item[0] for item in sorted_item[:k]]


        
        