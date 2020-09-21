class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        d = {}
        
        for i in range(len(list1)):
            d[list1[i]] = i 
        
        res = []
        min_sum = float('inf')
        for j in range(len(list2)):
            if j > min_sum : break 
            if list2[j] in d:
                s = j + d[list2[j]]
                if s < min_sum:
                    res = [list2[j]]
                    min_sum = s
                elif s == min_sum:
                    res.append(list2[j])
        
        return res
