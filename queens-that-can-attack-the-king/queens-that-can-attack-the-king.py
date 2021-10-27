class Solution:
    def queensAttacktheKing(self, queens: List[List[int]], king: List[int]) -> List[List[int]]:
        
        c = king[0]
        r = king[1]
        ans = []
        
        # row right
        for i in range(r+1,8): 
            if [c,i] in queens : 
                ans.append([c,i])
                break
                
        
        
        # row left
        for i in range(r-1,-1,-1):
            if [c,i] in queens : 
                ans.append([c,i])
                break
        
        
        
        # col up
        for i in range(c-1,-1,-1):
            if [i,r] in queens:
                ans.append([i,r])
                break
        
        
        
        # col down
        for i in range(c+1,8):
            if [i,r] in queens:
                ans.append([i,r])
                break
        
        
        # diginal left - up 
        i = c - 1
        j = r - 1
        while True:
            if i < 0 or j<0 : break
            if [i,j] in queens:
                ans.append([i,j])
                break
            i -= 1
            j -= 1
            
            
        
        # diginal left - down
        i = c + 1
        j = r - 1
        while True:
            if i > 7 or j < 0 : break
            if [i,j] in queens:
                ans.append([i,j])
                break
            i += 1
            j -= 1
        
        
            
        # diginal right - up 
        i = c - 1
        j = r + 1
        while True:
            if i < 0 or j > 7 : break
            if [i,j] in queens:
                ans.append([i,j])
                break
            i -= 1
            j += 1
        
        
        # diginal right - down
        i = c + 1
        j = r + 1
        while True:
            if i > 7 or j < 0 : break
            if [i,j] in queens:
                ans.append([i,j])
                break
            i += 1
            j += 1
            
        return (ans)
      
