class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        hashmap={}
        val=[]
        for i in arr:
            if i in hashmap:
                hashmap[i]+=1
            else:
                hashmap[i]=1
        for key, value in hashmap.items():
            val.append(value)
        z=set(val)
        if len(val)==len(z):
            return True
        return False
                
                
            
            
        