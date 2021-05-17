class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        r, result = ["qwertyuiop","asdfghjkl","zxcvbnm"], []    
        for i in words:
            words = set(i.lower())
            if(words.issubset(r[0]) or words.issubset(r[1]) or words.issubset(r[2])):
                result.append(i)
        return result