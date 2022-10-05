class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        lenP, i, j, sp = len(pushed), 0, 0, 0
        while(i < lenP):
            if(~sp and popped[j] == pushed[sp]):
                j += 1
                sp -= 1
            else:
                sp += 1
                i += 1
                if(i < lenP):
                    pushed[sp] = pushed[i]
        return not sp