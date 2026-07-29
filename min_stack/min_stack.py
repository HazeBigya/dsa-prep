class min_stack:
    def __init__(self):
        self.arr = []
        self.min_arr = []
        
    def push(self, x):
        self.arr.append(x)
        if self.min_arr:
            self.min_arr.append(min(x, self.getMin()))
        else:
            self.min_arr.append(x)
        
    def pop(self):
        self.arr.pop()
        self.min_arr.pop()
        
    def top(self):
        return self.arr[-1]
    
    def getMin(self):
        return self.min_arr[-1]
    
    def print(self):
        print(self.arr)
        print(self.min_arr)
    
    
stack = min_stack()
stack.push(1)
stack.push(-2)
print("Top so far: ", stack.top());
stack.push(0)
stack.push(-5)
stack.push(2)
stack.pop()
print("Min so far: ", stack.getMin());
stack.pop()
print("Top: ", stack.top());
print("Min: ", stack.getMin());
stack.print()