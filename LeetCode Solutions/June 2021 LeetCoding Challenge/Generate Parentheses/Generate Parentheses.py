class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        arr, m = [], 2 * n
        def helper(position: int, Open: int, sequence: int) -> None:
            if (position == m):
                res = [0] * m
                for i in range(m):
                    res[i] = "(" if sequence & 1 << i else ")"
                arr.append("".join(res))
                return
            if (Open):
                helper(position+1, Open-1, sequence)
            if (m - position > Open):
                helper(position+1, Open+1, sequence | 1 << position)
        helper(0, 0, 0)
        return arr