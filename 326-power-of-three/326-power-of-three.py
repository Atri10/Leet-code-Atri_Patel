class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        
        y = 0
        x = 0
        while True:
            x = 3 ** y
            if x == n:
                return True
            
            if x > n:
                return False
            
            y += 1