class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        
        l = [(intervals[i][0], i) for i in range(len(intervals))]
        l.sort(key=lambda x : x[0])
        
        ans = [-1]*len(intervals)
        
        for i in range(len(intervals)):
            r = bisect.bisect_left(l, (intervals[i][1],))
            if r < len(l):
                ans[i] = l[r][1] 
        
        return ans 
        
