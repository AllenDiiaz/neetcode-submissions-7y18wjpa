class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False

        s = sorted(s)
        t = sorted(t)

        p1 = 0
        p2 = 0

        while p1 < len(s):
            if s[p1] == t[p2]:
                p1 = p1 + 1
                p2 = p2 + 1
            else:
                return False
        return True

        