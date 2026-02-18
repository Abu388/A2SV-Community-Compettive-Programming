class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        val = []
        res = [-1] * len(intervals)
        l = 0
        if len(intervals) == 1:
            return [0] if intervals[0][0] == intervals[0][1] else [-1]

        for i , j in intervals:
            val.append([i,j,l])
            l += 1
        val.sort()
        # print(val)
        for i in range(len(val)-1):
            for j in range(i+ 1,len(val)):
                # print("comparison",val[i][1], "<=" ,val[j][1])
                if val[i][1] == val[i][0]:
                    # print("comparison",val[i][1], "==" ,val[i][2])
                    res[val[i][2]] = val[i][2]
                elif val[i][1] <= val[j][0]:
                    res[val[i][2]] =  val[j][2]
                    break
        return res
        
