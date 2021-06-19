class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        if(len(arr) < 3):
            return False
        for i in range(len(arr)-2):
            odd1, odd2, odd3 = arr[i], arr[i+1], arr[i+2]
            if((odd1%2 !=0) and (odd2%2 !=0) and (odd3%2 !=0)):
                return True
        return False