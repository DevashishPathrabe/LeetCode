class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        s1 = set(list1)
        s2 = set(list2)
        l = {}
        for i in (s1 & s2):
            ans = list1.index(i) + list2.index(i)
            l[i] = ans
            answer = min(l.values())
            result = (j for j, k in l.items() if k == answer)
        return result