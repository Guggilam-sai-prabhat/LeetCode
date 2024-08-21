class TwoStacks:
    def __init__(self, n=100):
        self.size = n
        self.arr = [None]*n
        self.top1 = -1
        self.top2 = n

    
    def push1(self, x):
        if self.top1 < self.top2 - 1:
            self.top1 +=1
            self.arr[self.top1] = x
        pass

    # Function to push an integer into stack 2
    def push2(self, x):
        if self.top1 < self.top2 - 1:
            self.top2 -= 1
            self.arr[self.top2] = x
            
        pass

  
    def pop1(self):
        if self.top1 >= 0:
            x = self.arr[self.top1]
            self.top1 -=1
            return x
        else:
            return -1
        pass

    
    def pop2(self):
        if self.top2 < self.size:
            x = self.arr[self.top2]
            self.top2 +=1
            return x
        else:
            return -1
        pass
