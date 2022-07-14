class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        answer = list()
        if(len(digits) == 0):
            return answer
        answer.append("")
        d = {'2':'abc','3':'def','4':'ghi', '5':'jkl','6':'mno','7':'pqrs','8':'tuv','9':'wxyz'}
        for i in digits:
            p = d[i]
            l = list()
            for letter in p:
                for k in answer:
                    l.append(k+letter)
            answer = l
        return answer