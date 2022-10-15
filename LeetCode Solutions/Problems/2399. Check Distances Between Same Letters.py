class Solution:
    def checkDistances(self, s: str, distance: List[int]) -> bool:
        d = {}        
        for i,ch in enumerate(s):
            if ch in d:
                if distance[ord(ch) - ord("a")] != (i-d[ch]):
                    return False                
            else:
                d[ch] = i+1
        return True