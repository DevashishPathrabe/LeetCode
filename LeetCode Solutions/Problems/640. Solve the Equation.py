class Solution:
    def solveEquation(self, equation: str) -> str:
        m = 1
        current = 0
        isCurrent = False
        left = True
        left_x = leftValue = right_x = rightValue = 0
        equation += '+'
        for c in equation:
            if c.isdigit():
                current = current * 10 + int(c)
                isCurrent = True
            elif c == '=':
                leftValue += current * m
                m = 1
                current = 0
                isCurrent = False
                left = False
            elif c == 'x':
                n = current * m if isCurrent else m
                if left:
                    left_x += n
                else:
                    right_x += n
                m = 1
                current = 0
                isCurrent = False
            else:
                if left:
                    leftValue += current * m
                else:
                    rightValue += current * m
                m = 1 if c == '+' else -1
                current = 0
                isCurrent = False
        x = left_x - right_x
        value = rightValue - leftValue
        if x == 0 and value == 0:
            return 'Infinite solutions'
        elif x == 0:
            return 'No solution'
        return f'x={value // x}'