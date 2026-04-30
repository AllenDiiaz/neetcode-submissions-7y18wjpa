class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        res = 0
        
        # 1. 第一層：遍歷所有可能的起點
        for i in range(n):
            # 2. 第二層：遍歷所有可能的終點
            for j in range(i, n):
                # 3. 檢查 s[i:j+1] 是否有重複
                if self.allUnique(s, i, j):
                    res = max(res, j - i + 1)
        return res

    def allUnique(self, s, start, end):
        # 使用 Set 來紀錄看過的字元 (記憶體開銷)
        seen = set()
        for k in range(start, end + 1):
            if s[k] in seen:
                return False
            seen.add(s[k])
        return True
        