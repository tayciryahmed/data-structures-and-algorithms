class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        l, r = 0, len(nums)-1
        
        while l < r:
            mid = (l+r)//2
            if (mid % 2 == 1 and nums[mid-1] == nums[mid]) or (mid % 2 == 0 and nums[mid+1] == nums[mid]):
                l = mid+1
            else:
                r = mid
                
        return nums[l]
                
            
