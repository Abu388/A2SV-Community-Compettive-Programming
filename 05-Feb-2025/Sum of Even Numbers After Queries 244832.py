# Problem: Sum of Even Numbers After Queries - https://leetcode.com/problems/sum-of-even-numbers-after-queries/description/

class Solution(object):
    def sumEvenAfterQueries(self, nums, queries):
        count=1
        even=[]
        value=0

        for val, index in queries :
            if count>0:
                nums[index]=val+nums[index]
               
                for i in nums:
                    if i%2==0:
                        value+=i
                even.append(value)
                count-=1
            else:
                checker=nums[index]+val
                if checker%2 !=0:
                    if nums[index]%2 ==0:
                        value-=nums[index]

                    
                else:
                    if nums[index]%2 ==0:
                        value +=val
                    else:
                        value+=checker

                nums[index]=checker
                even.append(value)
        return even 