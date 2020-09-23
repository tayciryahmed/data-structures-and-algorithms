class Solution:
    def lengthOfLongestSubstring(self, s):
        chars = set()
        i, j, ans = [0]*3
        while i < len(s) and j < len(s):
            if s[j] not in chars:
                chars.add(s[j])
                j += 1 
                ans = max(ans , j-i)
            else:
                chars.remove(s[i])
                i += 1
        return ans
