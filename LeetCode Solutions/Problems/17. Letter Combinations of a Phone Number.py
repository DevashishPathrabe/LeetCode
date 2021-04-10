L = {'2':"abc",'3':"def",'4':"ghi",'5':"jkl",
     '6':"mno",'7':"pqrs",'8':"tuv",'9':"wxyz"}
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        lendigits, letterCombinations = len(digits), []
        if(digits == ""):
            return []
        def helper(position: int, string: str):
            if(position == lendigits):
                letterCombinations.append(string)
            else:
                letters = L[digits[position]]
                for letter in letters:
                    helper(position+1,string+letter)
        helper(0,"")
        return letterCombinations