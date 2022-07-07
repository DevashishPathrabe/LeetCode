class Solution:
    def isSumEqual(self, firstWord: str, secondWord: str, targetWord: str) -> bool:
        a = int("".join([str(ord(i)-97) for i in firstWord]))
        b = int("".join([str(ord(i)-97) for i in secondWord]))
        c = int("".join([str(ord(i)-97) for i in targetWord]))
        return (a+b) == c