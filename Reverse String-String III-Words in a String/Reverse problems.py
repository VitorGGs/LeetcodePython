# Reverse string
class Solution:
    def reverseString(self, s: List[str]) -> None:
        return s.reverse()


# Reverse Words in a String III
class Solution:
    def reverseWords(self, s: str) -> str:
        return " ".join([a[::-1] for a in s.split()])


# Reverse words in a string
class Solution:
    def reverseWords(self, s: str) -> str:
        return " ".join(s.split()[::-1])