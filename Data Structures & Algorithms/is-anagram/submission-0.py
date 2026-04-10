class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False

        def get_counts(substring):

            # BaseCase
            if len(substring) <= 1:
                return {substring:1} if substring else {}

            # Devide
            mid = len(substring) // 2
            left = substring[:mid]
            right = substring[mid:]

            # Conquer
            left_dict = get_counts(left)
            right_dict = get_counts(right)

            # Combine
            return merge_dict(left_dict,right_dict)

        def merge_dict(d1,d2):
            for letter, nums in d2.items():
                if letter in d1:
                    d1[letter] = d1[letter] + nums
                else:
                    d1[letter] = nums
            return d1

        return get_counts(s) == get_counts(t)
        