class Solution:
    def dfs(self,i,j,board,visited,n,m):

        visited[i][j] = 1 

        board[i][j] = '#'

        directions = [(0,1),(1,0),(0,-1),(-1,0)]

        for dr,dl in directions:

            nr = i + dr 
            nl = j + dl 

            if 0<= nr<n and 0<= nl < m :
                if board[nr][nl] == 'O' and visited[nr][nl] == 0:
                    self.dfs(nr,nl,board,visited,n,m)



    def solve(self, board: List[List[str]]) -> None:

        # task : replace all the O's the are surrounded by X

        n = len(board)
        m = len(board[0])

        visited = [[0]*m for i in range(n)]
        for i in range(n):
            boundary = [0,m-1]
            for j in boundary:
                if board[i][j] == 'O' and visited[i][j]== 0 :
                    self.dfs(i,j,board,visited,n,m)

        boundary = [0,n-1]
        for i in boundary:
            for j in range(m):
                if board[i][j] == 'O' and visited[i][j]== 0 :
                    self.dfs(i,j,board,visited,n,m)
        
        for i in range(n):
            for j in range(m):

                if board[i][j] == 'O':
                    board[i][j] = 'X'
        for i in range(n):
            for j in range(m):

                if board[i][j] == '#':
                    board[i][j] = 'O'
                

        return None
        