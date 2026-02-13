class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        dis = [97 + i for i in range(27)]
        def find(x):
            stk = []
            while x != dis[x - 97]:
                stk.append(x - 97)
                x = dis[x - 97] 
            while stk:
                dis[stk.pop()] = x
            return x
        def union(u , v):
            x , y = find(u), find(v)
            if x == y:
                return False
            if x < y:
                dis[y - 97] = x
            else:
                dis[x - 97] = y
            return True


        for val in equations:
            f , v , s = val[0] , val[1:3], val[3]
            if v == '==':
                union(ord(f),ord(s))
        for val in equations:
            f , v , s = val[0] , val[1:3], val[3]
            if v == '!=':
                if find(ord(f)) == find(ord(s)):
                    return False
        return True
