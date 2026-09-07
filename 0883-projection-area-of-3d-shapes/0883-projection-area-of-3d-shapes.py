class Solution(object):
    def projectionArea(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """

        mp = defaultdict(int)
        for i in range(len(grid[0])):
            mp[i] = -1

        c = 0
        left = []
        for v in grid:
            val = v
            left.append(max(val))

            for i in range(len(val)):
                if val[i] != 0:
                    c += 1
                mp[i] = max(mp[i], val[i])
        tot = 0
        for k in mp.keys():
            tot += mp[k]
        return c + sum(left) + tot
                
                
                