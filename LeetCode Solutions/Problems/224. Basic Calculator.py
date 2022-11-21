class Solution:
    def calculate(self, s: str) -> int:
        result, sign, num  = 0, 1, 0
        stack_sign = []
        stack_sum = []
        i = 0
        while i < len(s):
            if s[i].isdigit():
                num = 0
                while i<len(s) and s[i].isdigit():
                    num = 10 * num + int(s[i])
                    i += 1
                result += sign*num
            else:
                if s[i] in '+-':
                    sign = 1 if s[i]=='+' else -1
                elif s[i] =='(':
                    stack_sign.append(sign)
                    stack_sum.append(result)
                    sign = 1
                    result = 0
                elif s[i] == ')':
                    result = stack_sum.pop() + result * stack_sign.pop()
                i += 1
        return result