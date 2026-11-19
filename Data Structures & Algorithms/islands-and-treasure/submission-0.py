from collections import deque
class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:

        n = len(grid)
        m = len(grid[0])

        q = deque()

        for i in range(n):
            for j in range(m):
                if grid[i][j] == 0 :
                    q.append((i,j))
        directions = [(0,1),(1,0),(-1,0),(0,-1)]
        while q :

            ind1,ind2 = q.popleft()

            for dr,dl in directions:

                nr= ind1 + dr
                nl = ind2 + dl 
                if 0<= nr< n and 0<=nl<m:

                    if grid[nr][nl] == 2147483647 :

                        grid[nr][nl] = min(grid[nr][nl],1+grid[ind1][ind2])
                
                        q.append((nr,nl))
        return None




        
        