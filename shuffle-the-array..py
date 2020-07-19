class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        ans = [0]*len(nums)
        for i in range(len(nums)):
            if i % 2 == 1:
                ans[i] = nums[i//2 + len(nums)//2]
            else:
                ans[i] = nums[i//2]
        return ans
        
