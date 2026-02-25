class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        val = defaultdict(list)
        res = []
        for num in arr:
            count = 0
            for j in range(32):
                if (num >> j) & 1:
                    count += 1
            val[count].append(num)
        val = dict(sorted(val.items(), key=lambda x:x[0] ))
        print(val)
        for k in val.values():
            k = sorted(k)
            for i in k:
                res.append(i)
        return res

        
        

        