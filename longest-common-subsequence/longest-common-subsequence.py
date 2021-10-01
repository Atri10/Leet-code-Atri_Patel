class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        
        from functools import cache
        """
        Recursive
        Time limit Exceeded if cache is not used
        """
        @cache
        def rec(i,j): 
            if i==len(text1) or j==len(text2):return 1
            elif text1[i] == text2[j]:return 1 + rec(i+1,j+1)
            else:return max(rec(i,j+1),rec(i+1,j))
            
        return rec(0,0) - 1
    
        