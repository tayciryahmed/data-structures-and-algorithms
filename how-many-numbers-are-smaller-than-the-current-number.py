class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        _nums = sorted(nums)
        
        ans = [0]*len(nums)
        
        for i in range(len(nums)):
             ans[i] = _nums.index(nums[i])       
        
        return ans
