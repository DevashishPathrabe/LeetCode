class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        operators = {'+', '-', '*', '/'}
        sign = '+'
        temp = 0
        for i in range(len(s)):
            letter = s[i]
            if (letter not in operators and letter != ' '):
                temp = temp * 10 + int(letter)
            if (letter in operators or i == len(s) - 1):
                if (sign == '+'):
                    stack.append(temp)
                if (sign == '-'):
                    stack.append(-temp)
                if (sign == '*'):
                    temp = temp*stack.pop()
                    stack.append(temp)
                if (sign == '/'):
                    vertex = stack.pop()
                    if (vertex > 0):
                        stack.append(vertex // temp)
                    else:
                        stack.append(-1 * ((-vertex) // temp))
                sign = letter
                temp = 0
        return sum(stack)