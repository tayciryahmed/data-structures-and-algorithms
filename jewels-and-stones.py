from collections import Counter

class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        S = Counter(S)
        ans = 0
        for c in J:
            ans +=  S[c]
        
        return ans 
