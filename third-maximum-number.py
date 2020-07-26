class Solution:
    def thirdMax(self, nums: List[int]) -> int:        
        maxs = [nums[0]]

        
        for i in range(1, len(nums)):

            if len(maxs) == 1 and nums[i] != maxs[0]:
                maxs.append(nums[i])
                maxs.sort(reverse=True)
            
            if len(maxs) == 2 and nums[i] not in maxs:
                maxs.append(nums[i])
                maxs.sort(reverse=True)
            
            if len(maxs) == 3 and nums[i] > maxs[2] and nums[i] not in maxs:
                maxs[2] = nums[i]
                maxs.sort(reverse=True)
                    
        
        if len(maxs) < 3: return max(maxs)
        return maxs[2]
        
        
class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        nums = list(set(nums))
        if len(nums) < 3: return max(nums)
        
        maxs = nums[:3]
        maxs.sort(reverse=True)
        
        for i in range(3, len(nums)):
            if nums[i] > maxs[2]:
                if nums[i]>maxs[0]:
                    maxs = [nums[i], maxs[0], maxs[1]]
                elif  nums[i]>maxs[1]:
                    maxs = [maxs[0], nums[i], maxs[1]]
                else:
                    maxs = [maxs[0], maxs[1], nums[i]]
        
        return maxs[2]
        
        
 class Solution:
    def thirdMax(self, nums: List[int]) -> int:        
        max1, max2, max3 = None, None, None
        
        for n in nums:
            if n == max1 or n == max2 or n == max3: 
                continue 
            
            if max1 is None or n > max1:
                max3 = max2
                max2 = max1
                max1 = n
            
            elif max2 is None or n > max2:
                max3 = max2
                max2 = n
                
            elif max3 is None or n > max3:
                max3 = n 
                
        return max1  if max3 is None else max3
