class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for i in tokens:
            if(i[-1].isdigit()):
                stack.append(int(i))
            else:
                s2 = stack.pop() 
                s1 = stack.pop()
                if(i == '+'):
                    stack.append(s1 + s2)
                elif(i == '-'): 
                    stack.append(s1 - s2)
                elif(i == '*'): 
                    stack.append(s1 * s2)
                else: 
                    stack.append(int(float(s1) / s2))
        return stack.pop()