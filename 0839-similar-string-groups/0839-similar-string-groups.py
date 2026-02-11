class Solution:
    def numSimilarGroups(self, strs: List[str]) -> int:
        n = len(strs)
        par = [ i for i in range(n)]
        def find(x):
            stk = []
            while x != par[x]:
                stk.append(x)
                x = par[x]
            while stk:
                par[stk.pop()] = x
            return x

        def union(u,v):
            x , y = find(u) , find(v)
            if x == y:
                return
            if x < y:
                par[y] = x 
            else:
                par[x] = y
            return
        
        for i in range(len(strs) - 1):
            for j in range(i + 1, len(strs)):
                if len(strs[i]) != len(strs[j]) or find(i) == find(j) :
                    continue
                count = 0
                val1 , val2 = strs[i] , strs[j]
                for k in range(len(val1)):
                    if val1[k] != val2[k]:
                        count += 1
                    if count > 2:
                        break
                if count < 3:
                    union(i , j)
        
        return len(set(find(i) for i in range(n)))


                

        