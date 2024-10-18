class Solution:
    def maximumSwap(self, num: int) -> int:
        arr=  [int(i) for i in str(num)]


        for i in range(len(arr)-1):
            l=i+1
            while l<len(arr):

                arr[l],arr[i]=arr[i],arr[l]
                y=" "
                for c in arr:
                    y+=str(c) 
                num=max(num,int(y))
                arr[i],arr[l]=arr[l],arr[i]

                l+=1
        return num
