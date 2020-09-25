class Solution:
    def validSquare(self, p1: List[int], p2: List[int], p3: List[int], p4: List[int]) -> bool:
        def dist(p1, p2):
            return (p2[1]-p1[1])**2 + (p2[0]-p1[0])**2
        
        p = [p1, p2, p3, p4]
        
        p.sort(key=lambda x: (x[0], x[1]))
        
        return dist(p[0], p[1]) != 0 and dist(p[0], p[1]) == dist(p[1], p[3]) == dist(p[3], p[2]) == dist(p[2], p[0])   and dist(p[0],p[3]) == dist(p[1],p[2])
