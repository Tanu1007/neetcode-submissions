class MinStack:

    def __init__(self):
        self.stk = []
        self.minstk = []
        

    def push(self, val: int) -> None:
        self.stk.append(val)
        if not self.minstk or self.minstk[-1]>=val:
            self.minstk.append(val)
        

    def pop(self) -> None:
        temp = self.stk.pop()
        if self.minstk[-1]==temp:
            self.minstk.pop()
        

    def top(self) -> int:
        return self.stk[-1]
        

    def getMin(self) -> int:
        return self.minstk[-1]
        
