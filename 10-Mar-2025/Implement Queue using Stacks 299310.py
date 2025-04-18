# Problem: Implement Queue using Stacks - https://leetcode.com/problems/implement-queue-using-stacks/

class MyQueue:

    def __init__(self):
        self.stk=deque()

    def push(self, x: int) -> None:
        self.stk.append(x)
        

    def pop(self) -> int:
        v=self.stk.popleft()
        return v
        

    def peek(self) -> int:
        return self.stk[0]
            
        

    def empty(self) -> bool:
        return len(self.stk)==0
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()