class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        char_set = set()
        left = 0
        max_len = 0

        # s = "zxyzxyz"

        for right in range(len(s)):  # 0 1 2 .. 8
           
            while s[right] in char_set:
                char_set.remove(s[left])
                left += 1
          
            char_set.add(s[right])

            curr_len = right - left + 1
            max_len = max(max_len,curr_len)

        return max_len


        