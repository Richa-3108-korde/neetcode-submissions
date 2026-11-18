class Solution:
    def dfs(self, i, j, grid, directions, n, m):

        grid[i][j] = 0
        count = 1

        for dr, dl in directions:
            nr = i + dr
            nl = j + dl

            if 0 <= nr < n and 0 <= nl < m:
                if grid[nr][nl] == 1:
                    count += self.dfs(nr, nl, grid, directions, n, m)

        return count

    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:

        n = len(grid)
        m = len(grid[0])

        directions = [(0,1), (1,0), (-1,0), (0,-1)]

        maxcount = 0

        for i in range(n):
            for j in range(m):

                if grid[i][j] == 1:

                    count = self.dfs(i, j, grid, directions, n, m)

                    maxcount = max(maxcount, count)

        return maxcount




        