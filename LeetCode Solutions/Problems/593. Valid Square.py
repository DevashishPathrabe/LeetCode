class Solution:
    def validSquare(self, p1: List[int], p2: List[int], p3: List[int], p4: List[int]) -> bool:
        def helper(d1, d2):
            return (d1[0]-d2[0])**2+(d1[1]-d2[1])**2
        s = set([helper(d1, d2) for d1, d2 in [[p1,p2],[p1,p3],[p1,p4],[p2,p3],[p2,p4],[p3,p4]]])
        if(len(s) == 2 and 0 not in s):
            return True
        return False