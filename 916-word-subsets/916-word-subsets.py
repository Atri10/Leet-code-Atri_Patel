import string 
class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        
        def newDic():
            latters = [i for i in string.ascii_lowercase]
            dic = {}
            for char in latters:dic[char] = 0
            return dic
        
        def countfreq(word):
            dic = newDic()
            for char in word:dic[char] += 1
            return dic
        
        maxdic = newDic()
        
        for word in words2:
            curdic = countfreq(word)
            for char in curdic:maxdic[char] = max(maxdic[char],curdic[char])
        
        
        ans = []
        
        for word in words1:
            curdic = countfreq(word)
            curstring = ""
            maxstr = ""

            for char in maxdic:
                
                if int(curdic[char]) >= int(maxdic[char]) and maxdic[char] > 0: 
                    curstring += char
                    
                
                if maxdic[char] > 0:
                    maxstr += char
                    
            if maxstr == curstring: ans.append(word)
                
        return ans