# 155.最小栈(在常数时间内找到最小栈)
# 说明：构建一个辅助栈
# 入栈：辅助栈栈顶用来存放栈的最小元素
# 出栈：两个栈同时出栈
class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.data = []
        self.min_data = []
        

    def push(self, x: int) -> None:
        self.data.append(x)
        if self.min_data == []:
            self.min_data.append(x)
        elif x < self.min_data[-1]:
            self.min_data.append(x)
        else:
            self.min_data.append(self.min_data[-1])

    def pop(self) -> None:
        self.data.pop()
        self.min_data.pop()

    def top(self) -> int:
        return self.data[-1]

    def getMin(self) -> int:
        return self.min_data[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()