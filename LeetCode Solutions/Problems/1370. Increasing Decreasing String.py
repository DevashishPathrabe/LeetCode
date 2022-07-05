class Solution:
    def sortString(self, s: str) -> str:
        result = []
        s = list(s)
        flag = True
        while len(s)!=0:
            if flag:
                temp = sorted(set(s))
            else:
                temp = sorted(set(s), reverse = True)
            for ch in temp:
                s.remove(ch)
            result.extend(temp)  
            flag = not flag
        return "".join(result)