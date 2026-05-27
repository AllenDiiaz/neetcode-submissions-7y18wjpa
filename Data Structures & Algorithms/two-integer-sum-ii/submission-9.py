class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        # numbers = [1,2,3,4] target = 3

        # 因為已經 sorted 
        # 開兩個指針去掃
        # 如果相加結果大於 target
        # 代表右邊太大 right -=1
        # 如果相加結果小於 target
        # 代表左邊要更大 left +=1
        # 如果相加等於 target 就返回 index 

        left = 0
        right = len(numbers) - 1

        while left < right:
            curr = numbers[left] + numbers[right]

            if curr > target:
                right-=1
            elif curr < target:
                left+=1
            else:
                return [left+1,right+1]
                
        