class Solution:
    def toGoatLatin(self, sentence: str) -> str:
        words = sentence.split()
        vowels = "AEIOUaeiou"
        m = "maa"
        List = []
        for i in words:
            if i[0] in vowels:
                List.append(i + m)
            else:
                List.append(i[1:] + i[0] + m)
            m += "a"   
        return " ".join(List)