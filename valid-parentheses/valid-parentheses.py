class Solution:
    def isValid(self, s: str) -> bool:
        if len(s)%2!=0:return False
        stack =[]
        for i in s:
            try:
                if i=="{" or i=="[" or i=="(" :stack.append(i)
                elif i=="}" and stack.pop() != "{":return False
                elif i=="]" and stack.pop() != "[":return False
                elif i==")" and stack.pop() != "(":return False
            except:return False
                
        if len(stack)==0:return True
        else: return False