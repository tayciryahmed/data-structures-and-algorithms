class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        if len(strs) == 0: return ""
        
        strs.sort()
        
        i = 0
        while i < len(strs[0]) and i < len(strs[-1]) and strs[0][i] == strs[-1][i]:
            i += 1
        
        return strs[0][:i]
            
