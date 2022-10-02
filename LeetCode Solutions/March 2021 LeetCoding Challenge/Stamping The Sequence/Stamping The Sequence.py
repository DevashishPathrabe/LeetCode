class Solution:
    def movesToStamp(self, stamp: str, target: str) -> List[int]:
        if (stamp not in target):
            return []
        x, y = len(stamp), len(target)
        count = 0
        arr = []
        while (count < 10):
            flag = False
            for i in range(y - x + 1):
                if (target[i:i+x] != "."*x and self.helper(stamp, target[i:i+x])):
                    flag = True
                    target = target[:i] + "."*x + target[i+x:]
                    arr.append(i)
            if (target == "."*y):
                return arr[::-1]
            if (not flag):
                return []
            count += 1
        return []
    def helper(self, stamp, target):
        for i in range(len(stamp)):
            if (target[i] != "." and stamp[i] != target[i]):
                return False
        return True