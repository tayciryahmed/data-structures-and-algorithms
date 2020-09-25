
class Solution:
    def romanToInt(self, s):
        # deal with subtracion cases
        subs = {'IV': 4, 'IX': 9, 'XL': 40, 'XC': 90, 'CD': 400, 'CM': 900}       
        mapp = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

        ans = 0
        i = 0
        
        while i < len(s):        
            if s[i:i+2] in subs:
                ans += subs[s[i:i+2]]
                i += 2
            else:
                ans += mapp[s[i]]
                i += 1
            
        return ans 
