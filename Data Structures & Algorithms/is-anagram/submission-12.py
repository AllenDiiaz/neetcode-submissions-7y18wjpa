class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if set(s) != set(t):
            return False

        s_seen = {}
        t_seen = {}

        for string in s:
            if string in s_seen:
                s_seen[string] += 1
            else:
                s_seen[string] = 1

        for strings in t:
            if strings in t_seen:
                t_seen[strings] += 1
            else:
                t_seen[strings] = 1
            

        return s_seen == t_seen

        

        