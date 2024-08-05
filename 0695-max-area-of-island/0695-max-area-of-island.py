class Solution(object):
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        res = 0
        
        visited = set()
        cols, rows = len(grid[0]), len(grid)
        curr = 0
        directions = [[1,0], [0,1], [-1,0], [0,-1]]
        
        def dfs(i,j):
            nonlocal curr
            q = collections.deque()
            q.append((i, j))
            visited.add((i, j))
            
            while q :
                row, col = q.pop()
                curr += 1
                for dr, dc in directions:
                    if 0 <= row+dr < rows and 0 <= col+dc < cols and (row+dr, col+dc) not in visited and grid[row+dr][col+dc]:
                        q.append((row+dr, col+dc))
                        visited.add((row+dr, col+dc))
                
        
        for i in range(rows):
            for j in range(cols):
                if (i, j) not in visited and grid[i][j] == 1 :
                    curr = 0
                    dfs(i,j)
                    res = max(res,curr)
                    
        
        return res