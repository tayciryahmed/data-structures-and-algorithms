class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        ans = [0]*len(T)
        stack = []
        for i in range(len(T)-1, -1, -1):
            while stack and stack[-1][0] <= T[i]:
                stack.pop()
            if stack:
                ans[i] = stack[-1][1] - i 
            
            stack.append([T[i], i])
            
        return ans 
