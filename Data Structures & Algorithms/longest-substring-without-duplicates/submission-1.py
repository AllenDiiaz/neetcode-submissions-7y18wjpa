class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # 1. 初始化快取 (Cache/Map) 與 指標
        char_map = {}  # 紀錄字元最後出現的索引
        left = 0       # 視窗左邊界 (覺知起點)
        max_length = 0 # 最終要回傳的最大長度
        
        # 2. 宇宙引擎開始渲染：右指標探索時間線
        for right, char in enumerate(s):
            
            # 3. 偵測衝突：如果這個角色之前出現過
            if char in char_map:
                # 核心邏輯：跳躍到新時間線，且「絕不回頭」
                left = max(left, char_map[char] + 1)
            
            # 4. 更新紀錄：把這個角色當前的座標寫入「阿卡西紀錄」(Map)
            char_map[char] = right
            
            # 5. 計算當前視窗長度，並更新最高紀錄
            # 視窗長度公式：(右界 - 左界 + 1)
            max_length = max(max_length, right - left + 1)
            
        return max_length
        