class Solution(object):
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        res = 0
        for x in range(len(grid)):
            for y in range(len(grid[0])):
                if grid[x][y] == 1:
                    stack = [(x, y)]
                    nb = 0
                    while stack:
                        i, j = stack.pop()
                        if grid[i][j] == 0 :
                            continue
                        nb += 1
                        grid[i][j] = 0
                        if  0 <= i+1 < len(grid) and 0 <= j < len(grid[0]) and grid[i+1][j] == 1 :
                            stack.append((i+1, j))
                            
                        if  0 <= i-1 < len(grid) and 0 <= j < len(grid[0]) and grid[i-1][j] == 1 :
                            stack.append((i-1, j))
                        if  0 <= i < len(grid) and 0 <= j+1 < len(grid[0]) and grid[i][j+1] == 1:
                            stack.append((i, j+1))
                        if  0 <= i < len(grid) and 0 <= j-1 < len(grid[0]) and grid[i][j-1] == 1 :
                            stack.append((i, j-1))
                    
                    if nb > res : 
                        res = nb

        return res