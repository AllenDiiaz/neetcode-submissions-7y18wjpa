class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:

        # 打包 pos sp
        cars = zip(position,speed)
        # cars [(4,2),(1,2),(0,1),(7,1)]
        # 按照位置排序 離終點近的靠前 （因為最快到的會是fleet的 bottleneck）
        cars = sorted(cars,reverse = True)
        # cars [(7,1),(4,2),(1,2),(0,1)]

        # 建 stack 維護fleet 的領頭羊
        stack = []

        for p,s in cars:
            time = (target - p) / s
            # time 3 -> 3 -> 4.5 -> 10
            if stack and time > stack[-1]:
                stack.append(time)
            elif not stack:
                stack.append(time)
            else:
                continue

        return len(stack)


            
        