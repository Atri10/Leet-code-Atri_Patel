class Solution:
    def isValid(self, s: str) -> bool:
        
        if len(s)%2 !=0 :
            return False
        
        
        stack = []
        
        
        for i in s:
            
            if i in ["(","{","["]:
                stack.append(i)
                
            if len(stack) == 0 : return False
            
            if i == ")" and stack.pop() != "(":
                return False
            
            if i == "}" and stack.pop() != "{":
                return False
            
            if i == "]" and stack.pop() != "[":
                return False
                

        return len(stack) == 0