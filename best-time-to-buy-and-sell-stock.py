class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        last_min = float('inf')
        
        ans = 0 
        
        for i in range(len(prices)):
            if prices[i] < last_min:
                last_min = prices[i]

            if prices[i] - last_min > ans:
                ans = prices[i] - last_min
        
        return ans 
