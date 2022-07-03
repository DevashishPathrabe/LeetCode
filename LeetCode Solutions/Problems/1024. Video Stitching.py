class Solution:
    def videoStitching(self, clips: List[List[int]], time: int) -> int:
        if time == 0:
            return 0
        clips.sort(key=lambda x: (x[0], -x[1]))
        if clips[0][0] <= 0:
            len_clips = len(clips)
            List = [clips[0]]
            index = 1
            while List[-1][1] < time and index < len_clips:
                start, end = clips[index]
                if start <= List[-1][1] < end:
                    if len(List) > 1 and start <= List[-2][1]:
                        List.pop()
                    List.append(clips[index])
                index += 1
            if List[-1][1] >= time:
                return len(List)
        return -1