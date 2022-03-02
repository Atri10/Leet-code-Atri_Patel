class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s)==len(t):
            if s==t:return True
            else:return False
        if(len(s)>len(t)):return False
        i,j = 0,0 
        while True:
            if(j>=len(s)):
                if(j == len(s)):return True                
            if(i>=len(t)):break              
            X,Y = t[i],s[j]          
            if X==Y:j = j + 1
            i = i + 1