class Solution:
    def wordBreak(self, s, wordDict):
        
        wordSet = set(wordDict)
        dp = [False]*(len(s)+1)
        
        dp[0] = True 
        
        for i in range(1, len(s)+1):
            for j in range(i):
                if s[j:i] in wordSet and dp[j]:
                    dp[i] = True 
                    
        return dp[len(s)]
