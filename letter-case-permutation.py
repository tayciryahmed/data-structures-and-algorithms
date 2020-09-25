class Solution:
    def letterCasePermutation(self, S: str) -> List[str]:
        nbl = 0
        for c in S: nbl += (c.isalpha())
        
        ans = []
        
        for mask in range(1<<nbl):
            s = []
            i = 0
            for c in S:
                if not c.isalpha(): 
                    s.append(c)
                else:
                    if (mask & 1<<i):
                        s.append(c.upper())
                    else:
                        s.append(c.lower())
                    i += 1
            
            ans.append(''.join(s))
        
        return ans 
                     
