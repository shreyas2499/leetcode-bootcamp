class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        count = 0
        R, C = len(grid), len(grid[0])
        
        
        def dfs(r, c):
            grid[r][c] = '0'
            if r-1 >= 0 and grid[r-1][c] == '1':
                dfs(r-1, c)
            if r+1 < R and grid[r+1][c] == '1':
                dfs(r+1, c)
            if c+1 < C and grid[r][c+1] == '1':
                dfs(r, c+1)
            if c-1 >= 0 and grid[r][c-1] == '1':
                dfs(r, c-1)
                
                
        for row in range(0, len(grid)):
            for col in range(0, len(grid[0])):
                if grid[row][col] == '1':
                    count += 1
                    dfs(row, col)
                    
        return count