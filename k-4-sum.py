class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        def ksum(nums, target, k):
            ans = []
            if len(nums) == 0 or nums[0]*k > target or target > nums[-1]*k:
                return ans 
            if k == 2: return twosum(nums, target)
            for i in range(len(nums)):
                if i > 0 and nums[i] == nums[i-1]: continue
                for ans_1 in ksum(nums[i+1:], target-nums[i], k-1):
                    ans.append([nums[i]]+ans_1)
            return ans
        
        def twosum(nums, target):
            ans = []
            left, right = 0, len(nums)-1
            while left < right :
                s = nums[right] + nums[left]
                if s < target or (left > 0 and nums[left] == nums[left-1]):
                    left += 1
                elif (s > target) or (right < (len(nums)-1) and nums[right]==nums[right+1]):
                    right -= 1
                else:
                    ans.append([nums[left], nums[right]])
                    left += 1
                    right -= 1
            return ans 
        
        nums.sort()
        return ksum(nums, target, 4)
            
        
