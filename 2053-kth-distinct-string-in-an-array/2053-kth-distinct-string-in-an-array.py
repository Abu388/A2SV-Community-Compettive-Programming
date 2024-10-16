class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        hasM={}
        for c in arr:
            if c in hasM:
                hasM[c]+=1
            else:
                hasM[c]=1

        for i in arr:
            if hasM[i]==1:
                k-=1
            if k==0:
                return i
        if k>0:
            return ""