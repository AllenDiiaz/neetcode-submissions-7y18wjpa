class MinStack:

    def __init__(self):
        self.data_stack = []
        self.min_stack = []

    def push(self, val: int) -> None:
        self.data_stack.append(val)

        if self.min_stack:
            self.min_stack.append(min(val,self.min_stack[-1]))
        else:
            self.min_stack.append(val)

    def pop(self) -> None:
        self.data_stack.pop()
        self.min_stack.pop()

    def top(self) -> int:
        return self.data_stack[-1]

    def getMin(self) -> int:
        return self.min_stack[-1]
        
