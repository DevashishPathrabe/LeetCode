class Solution:
    def maximumTime(self, time: str) -> str:
        time = list(time)
        for i, letter in enumerate(list(time)):
            if i ==0 and letter == "?":
                if time[1] == "?" or int(time[1]) <= 3:
                    time[i] = "2"
                    continue
                else:
                    time[i] = "1"
                    continue
            if i == 1 and letter == "?":
                if time[0] == "2":
                    time[i] = "3"
                    continue
                else:
                    time[i] = "9"
                    continue
            if i == 3 and letter == "?":
                time[i] = "5"
                continue
            if i == 4 and letter == "?":
                time[i] = "9"
                continue
        return "".join(time)