class Solution:      
    mov = ((2,1),(2,-1),(-2,1),(-2,-1),
                                   (1,2),(1,-2),(-1,2),(-1,-2))
    
    def knightProbability(self, N: int, K: int, r: int, c: int) -> float:
        dp_1 = [[0] * N for _ in range(N)]
        dp_1[r][c] = 1
        
        for _ in range(K):
            dp = [[0] * N for _ in range(N)]
            
            for r, row in enumerate(dp_1):
                for c, val in enumerate(row):
                    for dr, dc in self.mov :
                        if 0 <= (r+dr) < N  and 0 <= (c+dc) < N:
                            dp[r+dr][c+dc] += val / 8
                
            dp_1 = dp
        
        return sum(map(sum, dp_1))
        
        
