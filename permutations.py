class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        if len(nums) < 2: return [nums]
        if len(nums) == 2: return [nums, [nums[1], nums[0]]]
        
        permutations_1 = self.permute(nums[1:])
        
        ans = []
        
        
        for i in range(len(nums)):
            for perm in permutations_1:
                ans.append(perm[:i]+[nums[0]]+perm[i:])
        
        return ans 
        
