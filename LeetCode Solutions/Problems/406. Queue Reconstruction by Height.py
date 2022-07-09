class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        queue = []
        for h, k in sorted(people, key=lambda x: (-x[0], x[1])):
            queue.insert(k, [h, k])
        return queue