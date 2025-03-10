# Problem: Find Consecutive Integers from a Data Stream - https://leetcode.com/problems/find-consecutive-integers-from-a-data-stream/

class DataStream:

    def __init__(self, value: int, k: int):
        self.stk=deque()
        self.k=k
        self.v=value

    def consec(self, num: int) -> bool:
        if num != self.v:
            self.stk=deque()
            return False
        else:
            self.stk.append(num)
            if len(self.stk)==self.k:
                self.stk.popleft()
                return True
            return False




        
        

# Your DataStream object will be instantiated and called as such:
# obj = DataStream(value, k)
# param_1 = obj.consec(num)