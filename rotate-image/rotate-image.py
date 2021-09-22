class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        T = list(zip(*matrix))
        for i in range(len(matrix)):matrix[i] = reversed(list(T[i]))
                
            
            
            
            
            
            
       