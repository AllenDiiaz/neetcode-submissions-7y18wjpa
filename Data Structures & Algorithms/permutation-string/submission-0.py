class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n, m = len(s1), len(s2)
        if n > m:
            return False

        count1 = [0] * 26
        count2 = [0] * 26

        # 建立第一個視窗
        for i in range(n):
            count1[ord(s1[i]) - ord('a')] += 1
            count2[ord(s2[i]) - ord('a')] += 1

        if count1 == count2:
            return True

        # 滑動視窗
        for i in range(n, m):
            count2[ord(s2[i]) - ord('a')] += 1        # 右邊進來
            count2[ord(s2[i - n]) - ord('a')] -= 1    # 左邊出去
            if count1 == count2:
                return True

        return False