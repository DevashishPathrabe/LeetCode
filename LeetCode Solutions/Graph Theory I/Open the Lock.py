class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        if(target == "0000"):
            return 0
        queue, target = deque([0]), int(target)
        seen, turns = [0] * 10000, 1
        for d in deadends: seen[int(d)] = 1
        if(seen[0]):
            return -1
        while(len(queue)):
            qlen = len(queue)
            for i in range(qlen):
                current, j = queue.popleft(), 1
                while(j < 10000):
                    mask = current % (j * 10) // j
                    masked = current - (mask * j)
                    for k in range(1,10,8):
                        nxt = masked + (mask + k) % 10 * j
                        if(seen[nxt]):
                            continue
                        if(nxt == target):
                            return turns
                        seen[nxt] = 1
                        queue.append(nxt)
                    j *= 10
            turns += 1
        return -1