class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        arr, stack, count = [False for i in range(len(rooms))], [0], 1
        arr[0] = 1
        while (stack):
            keys = rooms[stack.pop()]
            for i in keys:
                if (not arr[i]):
                    stack.append(i)
                    arr[i] = True
                    count += 1
        return len(rooms) == count