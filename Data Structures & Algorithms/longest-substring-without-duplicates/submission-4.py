class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        char_set = set()
        left = 0
        max_len = 0

        # s = "zxyzxyz"

        # left = 0 right = 0
        # char_set {}
        # max_len = 0
        # ----------------------
        # left = 0 right = 0
        # s[right] not in char_set {}
        # char_set {'z'}
        # curr_len = right - left + 1 -> 0 - 0 + 1 = 1
        # max_len = max(0,1) = 1
        # ----------------------
        # left = 0 right = 1
        # s[right] not in char_set {}
        # char_set {'z','x'}
        # curr_len = right - left + 1 -> 1 - 0 + 1 = 2
        # max_len = max(0,2) = 2
        # ----------------------
        # left = 0 right = 2
        # s[right] not in char_set {}
        # char_set {'z','x','y'}
        # curr_len = right - left + 1 -> 2 - 0 + 1 = 3
        # max_len = max(0,3) = 3
        # ----------------------
        # left = 0 right = 3
        # s[right]  in char_set {} !
        # char_set {'z','x','y'}
        # char_set.remove(s[left]) -> {'x','y'}
        # left += 1 -> 1
        # s[right] not in char_set {} 
        # char_set {'x','y','z'}
        # curr_len = right - left + 1 -> 3 - 1 + 1 = 3
        # max_len = max(0,3) = 3



        for right in range(len(s)):  # 0 1 2 .. 8
           
            while s[right] in char_set:
                char_set.remove(s[left])
                left += 1
          
            char_set.add(s[right])

            curr_len = right - left + 1
            max_len = max(max_len,curr_len)

        return max_len


        