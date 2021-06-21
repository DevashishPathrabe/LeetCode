class Solution:
    def thousandSeparator(self, n: int) -> str:
        a = ""
        for n in format(n,",d"):
            if(n == ","):
                a += "."
            else:
                a += n
        return a