# Problem: Number of Recent Calls - https://leetcode.com/problems/number-of-recent-calls/

class RecentCounter:

    def __init__(self):
        self.stk=deque()

    def ping(self, t: int) -> int:
        dif=t-3000
        while self.stk and self.stk[0]<dif:
            self.stk.popleft()
        self.stk.append(t)
        return len(self.stk)

# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)