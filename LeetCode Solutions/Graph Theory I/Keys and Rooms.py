class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visited = set()
        def helper(i, room):
            visited.add(i)
            print(room)
            for key in room:
                if(key not in visited):
                    helper(key, rooms[key])
        helper(0, rooms[0])
        return len(visited) == len(rooms)