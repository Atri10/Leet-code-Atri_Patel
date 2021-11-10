class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        BZip =  list(zip(*board))
        
        def Checkline(li):
            temp = [i for i in li if i!="."]
            return len(set(temp))==len(temp)
            
        
        def check_row(board):
            for i in board:
                if not Checkline(i):return False
            return True
            
        def check_col(board):
            for i in BZip:
                if not Checkline(i):return False
            return True
                
        def square(board):
            for i in range(0,9,3):
                for j in range(0,9,3):
                    sqr = [board[x][y] for x in range(i,i+3) for y in range(j,j+3)]
                    if not Checkline(sqr):return False
            return True
        
        def checkmat():
            return (check_row(board) and check_col(board) and square(board))
        
        return checkmat()