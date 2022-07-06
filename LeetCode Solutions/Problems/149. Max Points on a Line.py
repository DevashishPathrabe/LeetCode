class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        if(len(points) < 3): 
            return len(points)
        result = 0
        for i1 in range(len(points)-1):
            duplicate = 0
            mydict = {}
            for i2 in range(i1+1, len(points)):
                dx = points[i1][0] - points[i2][0]
                dy = points[i1][1] - points[i2][1]
                if(dx == 0 and dy == 0):
                    duplicate += 1
                elif(dx == 0):
                    if("vertical" in mydict):
                        mydict["vertical"] += 1
                    else:
                        mydict["vertical"] = 1
                elif(dy == 0):
                    if("horizontal" in mydict):
                        mydict["horizontal"] += 1
                    else:
                        mydict["horizontal"] = 1
                else:
                    temp = abs(math.gcd(dy,dx))
                    if(dy < 0):
                        temp *= -1
                    s_temp = str(dy/temp)+str(dx/temp)
                    if(s_temp in mydict):
                        mydict[s_temp] += 1
                    else:
                        mydict[s_temp] = 1
            result = max(result, duplicate)
            for k in mydict.values():
                result = max(result, k + duplicate);
        return result + 1