class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        List = []
        c = Counter(arr)
        for i in arr:
            if c[i] == 1:
                List.append(i)
        if k > len(List):
            return ""
        else:
            return List[k-1]