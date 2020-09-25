class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()
        
        def dfs(target, idx, path):
            if target == 0: 
                res.append(path)
                return 
            
            if target < 0: return 

    
            for i in range(idx, len(candidates)):
                if i == idx or candidates[i] != candidates[i-1]:
                    dfs(target-candidates[i], i+1, path+[candidates[i]])

        dfs(target, 0, [])
                
        
        return res
    
