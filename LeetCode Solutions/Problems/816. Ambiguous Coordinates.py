class Solution:
    def ambiguousCoordinates(self, s: str) -> List[str]:
        def create(num):
            length = len(num)
            if(length == 1):
                return [num]
            if(num[0] == "0" and num[-1] == "0"):
                return []
            if(num[0] == "0"):
                return ["0."+num[1:]]
            if(num[-1] == "0"):
                return [num]
            result = [num]
            for i in range(1,len(num)):
                result.append(num[:i]+"."+num[i:])
            return result
        s = s[1:-1]
        n = len(s)
        listOfStrings = []
        for i in range(1,n):
            left = create(s[:i])
            right = create(s[i:])
            if(not left or not right):
                continue
            for l in left:
                for r in right:
                    listOfStrings.append(f'({l}, {r})')
        return listOfStrings