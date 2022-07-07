class Solution:
    def memLeak(self, memory1: int, memory2: int) -> List[int]:
        crashTime = 1
        while True:
            if memory1 >= memory2:
                if memory1 < crashTime:
                    break
                memory1 -= crashTime
            else:
                if memory2 < crashTime:
                    break
                memory2 -= crashTime
            crashTime = crashTime + 1
        return(crashTime, memory1, memory2)