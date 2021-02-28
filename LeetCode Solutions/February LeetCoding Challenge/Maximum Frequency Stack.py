class FreqStack:

    def __init__(self):
        self.frequencyMap = Counter()
        self.stack = [0]

    def push(self, x: int) -> None:
        self.frequencyMap[x] += 1
        freq = self.frequencyMap[x]
        if(freq == len(self.stack)):
            self.stack.append([x])
        else:
            self.stack[freq].append(x)

    def pop(self) -> int:
        top = self.stack[-1]
        x = top.pop()
        if(not top):
            self.stack.pop()
        self.frequencyMap[x] -= 1
        return x


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(x)
# param_2 = obj.pop()