class Solution:
    def countTime(self, time: str) -> int:
        h, m = time.split(":")
        tempHour = 1
        if h == "??":
            tempHour = 24
        elif h[0] == "?" and h[1] > "3":
            tempHour = 2
        elif h[0] == "?" and h[1] <= "3":
            tempHour = 3
        elif h[1] == "?" and h[0] == "2":
            tempHour = 4
        elif h[1] == "?" and h[0] < "2":
            tempHour = 10
        tempMinute = 1
        if m == "??":
            tempMinute = 60
        elif m[1] == "?":
            tempMinute = 10
        elif m[0] == "?":
            tempMinute = 6
        return tempHour * tempMinute