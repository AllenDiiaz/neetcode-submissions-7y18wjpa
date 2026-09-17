from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t or not s:
            return ""

        countT = Counter(t)
        window = {}

        have, need = 0, len(countT)
        res, resLen = [-1, -1], float('inf')
        left = 0

        for right in range(len(s)):
            c = s[right]
            window[c] = window.get(c, 0) + 1

            if c in countT and window[c] == countT[c]:
                have += 1

            while have == need:                    # 湊齊了 → 縮左邊
                # 更新答案
                if (right - left + 1) < resLen:
                    res = [left, right]
                    resLen = right - left + 1

                # 移出最左邊的字元
                window[s[left]] -= 1
                if s[left] in countT and window[s[left]] < countT[s[left]]:
                    have -= 1
                left += 1

        l, r = res
        return s[l:r+1] if resLen != float('inf') else ""