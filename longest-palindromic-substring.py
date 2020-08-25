class Solution:
    def longestPalindrome(self, s: str) -> str:
        def expand_around_center(s, l, r):
            while l>=0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
            
            return l+1, r-1
        
        ans = (0, 0)
        for i in range(len(s)):
            _ans = expand_around_center(s, i, i)
            if _ans[1]-_ans[0] > ans[1]-ans[0]:
                ans = _ans
        
        for i in range(len(s)-1):
            _ans = expand_around_center(s, i, i+1)
            if _ans[1]-_ans[0] > ans[1]-ans[0]:
                ans = _ans
        
        return s[ans[0]:ans[1]+1]
