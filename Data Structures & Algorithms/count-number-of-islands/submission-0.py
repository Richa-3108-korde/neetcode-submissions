class Solution:
    def dfs(self,i,j,visited,grid,n,m):

        visited[i][j] = 1 

        directions = [(1,0),(0,1),(-1,0),(0,-1)]

        for dr,dl in directions:

            nr , nl = i+dr , j+ dl 

            if 0<= nr<n and 0<= nl < m:
                if grid[nr][nl] == '1' and visited[nr][nl] == 0 :
                    self.dfs(nr,nl,visited,grid,n,m)

    def numIslands(self, grid: List[List[str]]) -> int:

        # we will be using the dfs 

        n = len(grid)
        m = len(grid[0])

        visited = [[0]*m for i in range(n)]
        count = 0 
        for i in range(n):
            for j in range(m):
                if grid[i][j] == '1' and visited[i][j]== 0:
                    count = count + 1
                    self.dfs(i,j,visited,grid,n,m)
        return count 










        