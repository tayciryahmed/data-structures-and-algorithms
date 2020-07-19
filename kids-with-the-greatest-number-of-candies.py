class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        _max = max(candies)
        return [x+extraCandies >= _max for x in candies]
        
