class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []
        
        def backtracking(ans, current_string, open, close, n):
            if len(current_string) == 2*n:
                ans.append(current_string)
                return 
            
            if open < n: backtracking(ans, current_string+"(", open+1, close, n)
            if close < open : backtracking(ans, current_string+")", open, close+1, n)
        
        backtracking(ans, "", 0, 0, n)
        
        return ans 
