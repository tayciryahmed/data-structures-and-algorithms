from collections import Counter
class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        if k > len(s) or not s: return 0
        if k <= 1: return len(s)
        hashmap = Counter(s)
        
        left = 0
        
        while left < len(s) and hashmap[s[left]] >= k:
            left += 1
            
        if left >= len(s) - 1:
            return left
        
        substringBeforeFaultyChar = self.longestSubstring(s[:left], k)
        
        while left < len(s) and hashmap[s[left]] < k:
            left += 1
            
        substringAfterFaultyChar = self.longestSubstring(s[left:len(s)], k) if left < len(s) else 0
        
        return max(substringBeforeFaultyChar, substringAfterFaultyChar)
