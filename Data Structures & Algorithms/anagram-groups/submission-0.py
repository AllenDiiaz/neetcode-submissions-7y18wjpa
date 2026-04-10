class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        # Input: strs = ["act","pots","tops","cat","stop","hat"]

        group = {}

        for string in strs:
            key = tuple(sorted(string))
            if key in group:
                group[key] += [string]
            else:
                group[key] = [string]
        return list(group.values())

        