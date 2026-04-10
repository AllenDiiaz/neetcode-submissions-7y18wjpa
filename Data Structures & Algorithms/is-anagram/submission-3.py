class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        seen_s = {}
        seen_t = {}

        for string in s:
            if string in seen_s:
                seen_s[string] += 1
            else:
                seen_s[string] = 1

        for string in t:
            if string in seen_t:
                seen_t[string] += 1
            else:
                seen_t[string] = 1

        if seen_s == seen_t:
            return True
        else:
            return False
        