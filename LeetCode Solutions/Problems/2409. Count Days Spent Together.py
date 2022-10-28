class Solution:
    def countDaysTogether(self, arriveAlice: str, leaveAlice: str, arriveBob: str, leaveBob: str) -> int:
        days = {"01": 0, "02": 31, "03": 59, "04": 90, "05": 120, "06": 151, "07": 181, "08": 212, "09": 243, "10": 273, "11": 304, "12": 334}
        aliceArrMonth, aliceArrDate = arriveAlice.split("-")
        aliceleaveMonth, aliceLeaveDate = leaveAlice.split("-")
        bobArrMonth, bobArrDate = arriveBob.split("-")
        bobleaveMonth, bobLeaveDate = leaveBob.split("-")
        aliceCame = days[aliceArrMonth] + int(aliceArrDate)
        aliceleft = days[aliceleaveMonth] + int(aliceLeaveDate)
        bobCame = days[bobArrMonth] + int(bobArrDate)
        bobleft = days[bobleaveMonth] + int(bobLeaveDate)
        maximum = max(aliceCame, bobCame)
        minimum = min(aliceleft, bobleft)
        if maximum <= minimum:
            result = minimum-maximum+1
        else:
            result = 0
        return result