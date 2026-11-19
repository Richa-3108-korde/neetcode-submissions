
class Solution:
    def pacificAtlantic(self, heights):

        n = len(heights)
        m = len(heights[0])

        pacific = [[0] * m for _ in range(n)]
        atlantic = [[0] * m for _ in range(n)]

        directions = [(0,1), (0,-1), (1,0), (-1,0)]

        def dfs(i, j, visited):

            visited[i][j] = 1

            for dr, dc in directions:

                nr = i + dr
                nc = j + dc

                if (0 <= nr < n and 0 <= nc < m
                    and not visited[nr][nc]
                    and heights[nr][nc] >= heights[i][j]):

                    dfs(nr, nc, visited)

        # Pacific DFS: Top row and Left column
        for j in range(m):
            if not pacific[0][j]:
                dfs(0, j, pacific)

        for i in range(n):
            if not pacific[i][0]:
                dfs(i, 0, pacific)

        # Atlantic DFS: Bottom row and Right column
        for j in range(m):
            if not atlantic[n-1][j]:
                dfs(n-1, j, atlantic)

        for i in range(n):
            if not atlantic[i][m-1]:
                dfs(i, m-1, atlantic)

        # Find cells visited by both DFS
        ans = []

        for i in range(n):
            for j in range(m):

                if pacific[i][j] and atlantic[i][j]:
                    ans.append([i, j])

        return ans

        