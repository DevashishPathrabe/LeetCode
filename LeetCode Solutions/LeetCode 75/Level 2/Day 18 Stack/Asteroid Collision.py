class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        state = []
        for a in asteroids:
            if a > 0:
                state.append(a)
            else:
                while len(state) > 0 and state[-1] > 0 and state[-1] < abs(a):
                    state.pop()
                if len(state) == 0 or state[-1] < 0:
                    state.append(a)
                elif state[-1] == abs(a):
                    state.pop()
        return state