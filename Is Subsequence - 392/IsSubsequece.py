#ponteiros
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        p_str = 0
        p_sub = 0
        
        while p_str < len(t) and p_sub < len(s):
            if s[p_sub] == t[p_str]:
                p_sub += 1
            p_str +=1
            
        return p_sub == len(s)

#iteradores
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        t = iter(t)
        
        for letter in s:
            if letter not in t:
                return False
        return True