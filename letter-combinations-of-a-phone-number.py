class Solution:
    map = {'2': ['a', 'b', 'c'],
             '3': ['d', 'e', 'f'],
             '4': ['g', 'h', 'i'],
             '5': ['j', 'k', 'l'],
             '6': ['m', 'n', 'o'],
             '7': ['p', 'q', 'r', 's'],
             '8': ['t', 'u', 'v'],
             '9': ['w', 'x', 'y', 'z']}
    
    def letterCombinations(self, digits: str) -> List[str]:
        ans = []
        
        if len(digits) == 0:
            return ""
        
        if len(digits) == 1:
            return self.map[digits]
        
        for a in self.letterCombinations(digits[1:]):
            for c in self.map[digits[0]]:
                ans.append(c+a)
        
        return ans 
            
