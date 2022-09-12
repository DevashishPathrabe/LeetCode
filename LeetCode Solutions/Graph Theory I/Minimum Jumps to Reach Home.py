class Solution:
    def minimumJumps(self, forbidden: List[int], a: int, b: int, x: int) -> int:
        limit = 2000 + a + b
        visited = set(forbidden)
        q = collections.deque([(0, True, 0)])
        hops = 0
        while q:
            current, move_backward, jumps = q.popleft() 
            if current == x:
                return jumps
            if current in visited:
                continue
            visited.add(current)
            if move_backward:
                next_jump = current - b
                if next_jump >= 0:
                    q.append((next_jump, False, jumps + 1))
            next_jump = current + a
            if next_jump <= limit:
                q.append((next_jump, True, jumps + 1))
        return -1