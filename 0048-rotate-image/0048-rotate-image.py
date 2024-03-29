class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        """n = len(matrix)-1
        for i in range(n+1):
            temp = matrix[i][0]
            matrix[i][0] = matrix[n][i]
            matrix[n][i] = matrix[n-i][n]
            matrix[n-i][n] = matrix[0][n-i]
            matrix[0][n-i] = temp
        for i in range(n+1):
            print(matrix[i])"""
        """n = len(matrix)

        # Transpose the matrix
        for i in range(n):
            for j in range(i, n):
                matrix[j][i], matrix[i][j] = matrix[i][j], matrix[j][i]

        # Reverse each row
        for i in range(n):
            matrix[i] = matrix[i][::-1]

        return matrix"""
        n = len(matrix)
        for layer in range(n // 2):
            first, last = layer, n - layer - 1
            for i in range(first, last):
                # Save top
                top = matrix[layer][i]

                # Left to top
                matrix[layer][i] = matrix[-i - 1][layer]

                # Bottom to left
                matrix[-i - 1][layer] = matrix[-layer - 1][-i - 1]

                # Right to bottom
                matrix[-layer - 1][-i - 1] = matrix[i][-layer - 1]

                # Top to right
                matrix[i][-layer - 1] = top

        
        
            
        