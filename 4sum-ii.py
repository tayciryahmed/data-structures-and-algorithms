class Solution:
    def fourSumCount(self, A: List[int], B: List[int], C: List[int], D: List[int]) -> int:
        sumAB = dict()
        
        for a in A:
            for b in B:
                sumAB[a+b] = sumAB.get(a+b, 0) + 1
        
        ans = 0
        for c in C:
            for d in D:
                if -(c+d) in sumAB:
                    ans += sumAB[-(c+d)]
        
        return ans 
