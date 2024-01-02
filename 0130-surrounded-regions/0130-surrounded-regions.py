class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        ROWS, COLS = len(board), len(board[0])

        def dfs(i, j):
            if i < 0 or i >= ROWS or j < 0 or j >= COLS or board[i][j] != 'O':
                return
            board[i][j] = 'C'
            
            dfs(i + 1, j)
            dfs(i - 1, j)
            dfs(i, j + 1)
            dfs(i, j - 1)


        for row in range(ROWS):
            if board[row][0] == 'O':
                dfs(row, 0)
            if board[row][COLS-1] == 'O':
                dfs(row, COLS-1)

        for col in range(1, COLS-1):
            if board[0][col] == 'O':
                dfs(0, col)
            if board[ROWS-1][col] == 'O':
                dfs(ROWS-1, col)

        for row in range(ROWS):
            for col in range(COLS):
                if board[row][col] == 'C':
                    board[row][col] = 'O'
                else:
                    board[row][col] = 'X'
