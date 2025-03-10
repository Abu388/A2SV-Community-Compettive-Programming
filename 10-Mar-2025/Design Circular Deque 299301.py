# Problem: Design Circular Deque - https://leetcode.com/problems/design-circular-deque/

class MyCircularDeque:

    def __init__(self, k: int):
        self.k=k
        self.stk=deque()

    def insertFront(self, value: int) -> bool:
        if len(self.stk)<self.k:
            self.stk.appendleft(value)
            return True
        return False
        

    def insertLast(self, value: int) -> bool:
        if len(self.stk)<self.k:
            self.stk.append(value)
            return True
        return False
        

    def deleteFront(self) -> bool:
        if self.stk:
            self.stk.popleft()
            return True
        return False
        

    def deleteLast(self) -> bool:
        if self.stk:
            self.stk.pop()
            return True
        return False
        

    def getFront(self) -> int:
        if self.stk:            
            return self.stk[0]
        return -1

    def getRear(self) -> int:
        if self.stk:            
            return self.stk[-1]
        return -1
        

    def isEmpty(self) -> bool:
        return len(self.stk)==0
       
        

    def isFull(self) -> bool:
        return len(self.stk)==self.k
       
        


# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()