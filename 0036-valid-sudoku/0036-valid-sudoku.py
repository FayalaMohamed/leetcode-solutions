class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        for i in range(9):
            # for each row
            unique = set()
            for j in range(9):
                if board[i][j] in unique:
                    return False
                if board[i][j] != ".":
                    unique.add(board[i][j])
                
            # for each column
            unique = set()
            for j in range(9):
                if board[j][i] in unique:
                    return False
                if board[j][i] != ".":
                    unique.add(board[j][i])
            
        for i in [0,3,6]:
            for j in [0,3,6]:
                unique = set()
                for x in range(3):
                    for y in range(3):
                        if board[i+x][j+y] in unique:
                            return False
                        if board[i+x][j+y] != ".":
                            unique.add(board[i+x][j+y])
        return True