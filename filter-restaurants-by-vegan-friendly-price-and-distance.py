class Solution:
    def filterRestaurants(self, restaurants: List[List[int]], veganFriendly: int, maxPrice: int, maxDistance: int) -> List[int]:
        ans = []
        
        for r in restaurants:
            if veganFriendly and r[2] == 0: continue
            if r[-1] > maxDistance: continue
            if r[-2] > maxPrice: continue 
            
            ans.append((r[0], r[1]))
        
        ans.sort(key=lambda x: (-x[1], -x[0]))
        
        return [x[0] for x in ans]
