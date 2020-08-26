class Solution:
    def rob(self, nums: List[int]) -> int:
        
        if len(nums) == 0: return 0
        if len(nums) == 1: return nums[0]
        
        dp_2 = nums[0]
        dp_1 = max(nums[1], nums[0])
                
        for i in range(2, len(nums)):
            dp = max(dp_1, dp_2+nums[i])
            dp_2, dp_1 = dp_1, dp
            
        return dp_1
        
