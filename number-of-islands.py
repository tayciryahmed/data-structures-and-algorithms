class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        ans = 0 
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == "1":
                    ans += 1
                    self.dfs(grid, r, c)
        
        return ans
        
    def dfs(self, grid, r, c):

        if r < 0 or r >= len(grid) or c < 0 or c >= len(grid[0]):
            return 

        if grid[r][c] == "1":
            grid[r][c] = "0"

            self.dfs(grid, r+1, c)
            self.dfs(grid, r, c+1)
            self.dfs(grid, r-1, c)
            self.dfs(grid, r, c-1)

