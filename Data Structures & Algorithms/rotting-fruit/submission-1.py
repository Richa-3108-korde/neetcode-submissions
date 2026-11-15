from collections import deque 
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        q = deque()
        fruits = 0 
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 2:
                    q.append((i,j))
                elif grid[i][j]== 1:
                    fruits += 1
        time = 0 
        while q and fruits >0 :
            length = len(q)

           
            for i in range(length):

                i,j = q.popleft()

                directions = [(1,0),(0,1),(-1,0),(0,-1)]

                for dr , dl in directions:

                    nr = i + dr
                    nl = j + dl 
                    if 0 <= nr < n and 0<= nl<m:
                        if grid[nr][nl] == 1:
                            grid[nr][nl]=2
                            fruits -= 1 
                            q.append((nr,nl))
                        
            time = time + 1 

        
        return time if fruits == 0 else -1 








        