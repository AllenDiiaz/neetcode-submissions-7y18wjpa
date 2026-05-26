class Solution:
    def isPalindrome(self, s: str) -> bool:

        # 建一個新 list
        # 去除空格
        # 大寫轉小寫
        # 用左右指針 不一樣就 return false 

        ans_s = []

        for char in s:
            if char.isalnum():
                ans_s.append(char.lower())

        left = 0
        right = len(ans_s) - 1

        while left < right:
            if ans_s[left] != ans_s[right]:
                return False
            left+= 1
            right-=1

        return True

        