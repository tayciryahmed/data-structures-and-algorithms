class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        strs = [(x, ''.join(sorted(x))) for x in strs]
        strs.sort(key=lambda x: x[1])
        
        
        ans = [[strs[0][0]]]
            
        for i in range(1, len(strs)):
            if strs[i][1] == strs[i-1][1]:
                ans[-1].append(strs[i][0])
            else:
                ans.append([strs[i][0]])
        
        return ans 
            
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = {}
        
        for x in strs:
            y = ''.join(sorted(x))
            ans[y] = ans.setdefault(y, []) + [x]
        
        return ans.values()
