class DynamicQueue:
    defaultSize = 2
    
    def __init__(self):
        self.data = [None] * self.defaultSize
        self.count = 0
        self.front = 0

    def isQueueEmpty(self):
        return self.count == 0
    
    def getElementsCount(self):
        return self.count
    
    def enque(self,ele):
        if self.count == self.defaultSize:
            self.resizeQueue(2*len(self.data))
        idx = (self.front + self.count) % len(self.data)
        self.data[idx] = ele
        self.count += 1
        return self.count
    
    def deque(self):
        if not self.isQueueEmpty():
            ele = self.data[self.front]
            self.count = self.count - 1
            self.data[self.front] = None 
            self.front = (self.front + 1) % len(self.data)
            if self.count > 0 and self.count < len(self.data)//4:
                self.resizeQueue(len(self.data)//2)
            return ele
        else:
            return None
    
    def resizeQueue(self,cap):
        oldData = self.data
        walk = self.front
        self.data = [None] * cap
        for k in range(self.count):
            self.data[k] = oldData[walk]
            walk = (walk + 1) % len(oldData)
        self.front = 0

    def printQ(self):
        return self.data