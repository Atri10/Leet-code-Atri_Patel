class Solution:
    def binaryGap(self, n: int) -> int:  
        a = str(bin(n))
        a = a[2:]
        dis = []
        c = 0
        for i in range(len(a)):
            if a[i] == "1":
                dis.append(c)
                c = 0    
            c +=1
        return max(dis)
        
                
            
            
        