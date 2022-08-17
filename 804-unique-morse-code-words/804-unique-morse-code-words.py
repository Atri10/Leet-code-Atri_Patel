import string

class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        
        
        char = list(string.ascii_lowercase)
        mc = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        
        def mtw(word):
            s = ""
            for char in word:
                s += mc[ord(char) - 97]
            return s
        
        dic = {}
        ans = 0
        for word in words:
            m_word = mtw(word)
            if m_word in dic:
                pass
            else:
                dic[m_word] = True
                ans += 1
                
        print(dic)
        return ans