class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.p = []
        self.m = 9999999999999
    def push(self, x: int) -> None:
        self.p.append(x)
        self.m=min(self.m,x)
    def pop(self) -> None:
        tem=self.p.pop()
        if tem==self.m:
            if self.p:
                self.m=min(self.p)
            else:
                self.m=9999999999999
    def top(self) -> int:
        return self.p[-1]

    def getMin(self) -> int:
        if self.p:
            return self.m
        else:
            return None
