class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        # strs = ["act"]

        group = {}

        for string in strs:
            count = [0] * 26
            for char in string:
                index  = ord(char) - ord('a')
                count[index] += 1
            key = tuple(count)
            if key in group:
                group[key] += [string]
            else:
                group[key] = [string]
        return list(group.values())

            


        