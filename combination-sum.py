class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()
        
        
        def dfs(target, idx, path):
            if target == 0:
                res.append(path)
                return

            for i in range(idx, len(candidates)):
                if candidates[i] > target: return 
                dfs(target-candidates[i], i, path+[candidates[i]])

        
        dfs(target, 0, [])
        
        
        return res
