class Solution:
    def reverse(self, x: int) -> int:
        
        if x < -2**31 or x > 2**31 -1: return 0
        
        ans = 0
        
        if x <0: 
            neg = True 
            x = -x
        else: 
            neg=False
        
        
        while x :
            ans = ans*10 + x%10
            x = x // 10
        
        if neg: ans = -ans
            
        if ans < -2**31 or ans > 2**31 -1: return 0
        
        return ans
        
