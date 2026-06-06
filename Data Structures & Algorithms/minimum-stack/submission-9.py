class MinStack:

    def __init__(self):
        self.stack = []
        self.min = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if(len(self.min) == 0):
            self.min.append(val)
        elif(val <= self.min[-1]):
            self.min.append(val)

        # print(self.min)
        
    def pop(self) -> None:
        # print(self.stack)
        # print(self.min)
        if(self.min[-1] == self.stack[-1]):
            self.min = self.min[:-1]
        self.stack = self.stack[:-1]
        # print(self.min)


    def top(self) -> int:
        # print(self.stack)
        return self.stack[-1]

    def getMin(self) -> int:
        # print(self.stack)
        # print(self.min)
        return self.min[-1]


       
