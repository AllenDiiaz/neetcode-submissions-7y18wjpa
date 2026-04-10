class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:

        cars = sorted(zip(position,speed),reverse = True)

        stack = []

        for p,s in cars:
            # 2. 計算這台車抵達終點的時間
            time = (target - p) / s
            # 3. 把時間丟進 stack
            stack.append(time)

            # 4. 如果發現這台車會追上「前車」
            # 也就是 stack 裡至少有兩台車，且最後進去的那台（後車）時間比較短

            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                #它被擋住了，變成同一個車隊，所以把自己的時間彈出來
                stack.pop()

        return len(stack)


        