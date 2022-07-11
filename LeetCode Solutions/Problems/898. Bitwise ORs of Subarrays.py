class Solution:
    def subarrayBitwiseORs(self, arr: List[int]) -> int:
        Set = set(arr)
        current = 0
        previous = set()
        previous.add(arr[0])
        for num in arr[1:]:
            temp = set()
            for p in previous:
                temp.add(num | p)
                Set.add(num | p)
            previous = temp
            previous.add(num)
        return len(Set)