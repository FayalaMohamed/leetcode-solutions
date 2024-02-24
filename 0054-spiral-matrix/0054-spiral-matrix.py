class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if len(matrix) == 0:
            return []
        
        
        res = []
        currRow = 0
        currCol = len(matrix[0]) - 1
        nbRows = 0
        nbCols = 0
        
        while len(res) != len(matrix)*len(matrix[0]):
            for i in range(nbRows,len(matrix[0])-nbRows):
                res.append(matrix[currRow][i])
                
            for i in range(nbCols+1, len(matrix)-nbCols):
                res.append(matrix[i][currCol])
                
            if len(res) == len(matrix) * len(matrix[0]):
                break
                
            for i in range(len(matrix[0])-nbRows-2,nbRows-1,-1):
                res.append(matrix[len(matrix)-1-currRow][i])
                
            for i in range(len(matrix)-nbCols-2,nbCols,-1):
                res.append(matrix[i][len(matrix[0]) - 1-currCol])
            
            nbRows += 1
            nbCols += 1
            currRow += 1
            currCol -= 1
                
        return res
            