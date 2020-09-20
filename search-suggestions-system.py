class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        
        ans = [None]*len(searchWord)
        
        for i in range(1, len(searchWord)+1):
            for p in products:
                if p.startswith(searchWord[:i]):
                    if ans[i-1]:
                        ans[i-1].append(p)
                    else:
                        ans[i-1] = [p]
            
            if ans[i-1]: 
                ans[i-1].sort()
            
                if len(ans[i-1]) > 3:
                    ans[i-1] = ans[i-1][:3]
            
        
        return ans
            
        
