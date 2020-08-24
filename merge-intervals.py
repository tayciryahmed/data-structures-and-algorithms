class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        if len(intervals) == 0 : return []
        
        intervals.sort(key = lambda x: x[0])
        
        ans = [intervals[0]]
        
        for i in range(1, len(intervals)):
            if intervals[i][0] <= ans[-1][1]:
                ans[-1] = [min(intervals[i][0], ans[-1][0]), 
                           max(intervals[i][1], ans[-1][1])]
            else:
                ans.append(intervals[i])
        
        return ans
            
