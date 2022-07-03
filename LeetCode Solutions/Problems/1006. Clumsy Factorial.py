class Solution:
    def clumsy(self, n: int) -> int:
        result = ""
        j =- 1
        for i in range(n,0,-1):
            result += str(i)
            j += 1
            if j < n - 1:
                if j % 4 == 0 :
                    result += "*"
                elif j % 4 == 1:
                    result += "//"
                elif j % 4 == 2:
                    result += "+"
                elif j % 4 == 3:
                    result += "-"
        return (eval(result))