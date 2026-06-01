class Solution:
    def minimumCost(self, cost: List[int]) -> int:
        c , res = 0 , 0
        cost = sorted(cost)
        for i in range(len(cost) - 1, - 1, - 1):
            if c != 2:
                res += cost[i]
                c += 1
            else:
                c = 0
        return res
