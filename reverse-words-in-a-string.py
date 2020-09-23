class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.split()
        for i in range(len(s)//2):
            s[i], s[len(s)-i-1] = s[len(s)-i-1], s[i]
        
        return " ".join(s)
