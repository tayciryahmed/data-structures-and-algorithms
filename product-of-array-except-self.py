class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        ans = [1]*len(nums)
        
        #left products 
        for i in range(1, len(nums)):
            ans[i] = ans[i-1]*nums[i-1]
        
        R = 1
        for i in range(len(nums)-1, -1, -1):
            ans[i] = ans[i] * R
            R = R * nums[i]
        
        return ans 
