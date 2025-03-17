# Problem: Find the Winner of the Circular Game - https://leetcode.com/problems/find-the-winner-of-the-circular-game/

class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        count = 1
        l = 0  
        arr = [int(i) for i in range(1, n + 1)]

        while len(arr) > 1:
            if count < k:
                count += 1
                l += 1
                if l >= len(arr): 
                    l = 0
            elif count == k:
                arr.pop(l)  
                print(arr)
                count = 1  
                if l >= len(arr): 
                    l = 0
            
        return arr[0]
            
            
        
        
# first finaly we have got one num
# how the it goint to work the loop 
# if the count == k then we change count into 1 and we are going to continue the loop

   