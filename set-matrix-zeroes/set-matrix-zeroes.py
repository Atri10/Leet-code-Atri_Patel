class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        zeros = []
        c = len(matrix)
        r = len(matrix[0])
        for i in range(c):
            for j in range(r):
                if matrix[i][j] == 0:zeros.append((i,j))
                    
        
        
        for x,y in zeros:
            for i in range(c):matrix[i][y] = 0
            for i in range(r):matrix[x][i] = 0