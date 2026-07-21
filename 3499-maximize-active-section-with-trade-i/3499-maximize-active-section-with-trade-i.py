class Solution:
    def maxActiveSectionsAfterTrade(self, s: str) -> int:
        base_ones = s.count('1')
     
        t = '1' + s + '1'
        
        groups = []
        current_char = t[0]
        count = 0
        
        for char in t:
            if char == current_char:
                count += 1
            else:
                groups.append(count)
                current_char = char
                count = 1
        groups.append(count) 
        
      
        max_gain = 0
        
        
        for i in range(2, len(groups) - 1, 2):
            
            gain = groups[i - 1] + groups[i + 1]
            max_gain = max(max_gain, gain)
            
        return base_ones + max_gain
            