class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        colmat = list(zip(*grid))
        max_row = [max(row) for row in grid]
        max_col = [max(col) for col in colmat]
        ans = 0
        for i in range(m):
            for j in range(n):ans += min(max_row[j],max_col[i]) - grid[i][j]
        return ans