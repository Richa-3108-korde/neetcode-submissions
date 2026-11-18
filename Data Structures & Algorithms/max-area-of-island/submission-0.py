class Solution:
    def dfs(self,i,j,visited,directions,grid,n,m):

        visited[i][j] = 1 
        count =  1
        for dr,dl in directions:

            nr = i + dr 
            nl = j + dl 

            if 0<= nr<n and 0<= nl < m :
                if  grid[nr][nl] == 1 and visited[nr][nl] ==  0 :
                    count += self.dfs(nr,nl,visited,directions,grid,n,m)
        return count

    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        visited  =  [[0]*m for i in range(n)]
        
        directions = [(0,1),(1,0),(-1,0),(0,-1)]
        maxcount = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1 and visited[i][j] == 0 :
                    count = self.dfs(i,j,visited,directions,grid,n,m)

                    maxcount = max(maxcount,count)
        return maxcount 





        