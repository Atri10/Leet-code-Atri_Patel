class Solution:
    def findComplement(self, num: int) -> int:
        x = bin(num)[2:]
        a = ""
        for i in range(len(x)):
            if x[i] == "0" : a += "1"
            else : a += "0"
            
        return int(a,2)