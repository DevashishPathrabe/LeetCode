class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        trip = set(trip for (trip, destination) in paths)
        destination = set(destination for (trip, destination) in paths)
        return list(destination - trip)[0]