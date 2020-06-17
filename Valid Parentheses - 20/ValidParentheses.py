class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        
        for i in s:
            if par not in ")}]":
                stack.append(i)
            elif not stack:
                return False
            elif not (stack.pop()+i in "(){}[]"):
                return False
            
        return stack == []