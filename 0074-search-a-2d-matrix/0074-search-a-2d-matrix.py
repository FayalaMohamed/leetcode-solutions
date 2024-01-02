class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """

        row = 0

        l = 0
        r = len(matrix[0])
        while l < r and row < len(matrix): 
            mid = (l+r)//2
            if matrix[row][mid] <= target: 
                l = mid + 1
            else:
                r = mid
            if matrix[row][r-1] < target:
                row += 1
                l = 0
                r = len(matrix[0])


        if l > 0 and row < len(matrix) and matrix[row][l -1] == target: 
            return True
        else:
            return False

