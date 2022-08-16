class Solution:
    def firstUniqChar(self, s: str) -> int:
        
        dic = {}
        
        for i in s:
            
            if i not in dic:
                dic[i] = 0
            else:
                dic[i]  += 1
        
        for i in dic:
            if dic[i] == 0:
                return s.index(i)

        return -1
            