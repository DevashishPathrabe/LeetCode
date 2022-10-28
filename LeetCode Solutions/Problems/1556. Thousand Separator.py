class Solution:
    def thousandSeparator(self, n: int) -> str:
        string = ""
        for n in format(n,",d"):
            if n == ",":
                string += "."
            else:
                string += n
        return string