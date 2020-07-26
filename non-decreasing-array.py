class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        ans = None
        for i in range(len(nums)-1):
            if nums[i] > nums[i+1]:
                if ans is not None: 
                    return False 
                else: 
                    ans = i

        
        return ans is None or ans == 0 or ans == len(nums)-2 or nums[ans-1] <= nums[ans+1] or nums[ans] <= nums[ans+2]
