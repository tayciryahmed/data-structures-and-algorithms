import random

class Solution:

    def __init__(self, w: List[int]):
        self.w = w
        for i in range(1, len(w)):
            self.w[i] += self.w[i-1] 
        
    def pickIndex(self) -> int:

        n = random.randint(1, self.w[-1])
        l,r = 0, len(self.w)-1
        while l<r:
            mid = (l+r)//2
            if n <= self.w[mid]:
                r = mid
            else:
                l = mid+1
        return l
