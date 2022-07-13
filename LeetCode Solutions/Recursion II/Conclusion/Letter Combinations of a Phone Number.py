class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res = list()
        if(len(digits) == 0):
            return res
        res.append("")
        d = {'2':'abc','3':'def','4':'ghi', '5':'jkl','6':'mno','7':'pqrs','8':'tuv','9':'wxyz'}
        for i in digits:
            p = d[i]
            l = list()
            for letter in p:
                for k in res:
                    l.append(k+letter)
            res = l
        return res