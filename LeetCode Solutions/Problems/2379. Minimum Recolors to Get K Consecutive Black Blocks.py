class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        min_operation, step = 0, 0
        while (step < len(blocks) - k + 1):
            temp_arr = blocks[step : step + k]
            if step == 0:
                min_operation += temp_arr.count("W")
            else:
                min_operation = min(min_operation, temp_arr.count("W"))
            step += 1
        return min_operation