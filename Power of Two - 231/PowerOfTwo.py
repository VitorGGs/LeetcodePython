#Usando matemática 
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n <= 0: return False
        return not (math.log2(n) - int(math.log2(n)))


#Contando o número de 1's
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n <= 0: return False
        return bin(n).count('1') == 1


#bitwise AND
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        return n > 0 and not (n & n-1)