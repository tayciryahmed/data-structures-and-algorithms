from collections import Counter
class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        nums = Counter(nums)
        ans = sum([n*(n-1)/2 for n in nums.values()])
        return int(ans)
        
