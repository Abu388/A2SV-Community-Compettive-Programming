class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        x = sorted(arr)
        mp = defaultdict(int)
        c = 1
        for i in x:
            if i not in mp:
                mp[i] = c 
                c += 1
        for i in range(len(arr)):
            arr[i] = mp[arr[i]]
        return arr
        