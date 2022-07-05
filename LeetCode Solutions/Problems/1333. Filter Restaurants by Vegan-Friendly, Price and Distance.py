class Solution:
    def filterRestaurants(self, restaurants: List[List[int]], veganFriendly: int, maxPrice: int, maxDistance: int) -> List[int]:
        result = []
        for subList in restaurants:
            if (subList[2] == veganFriendly or veganFriendly == 0) and subList[3] <= maxPrice and subList[4] <= maxDistance:
                result.append([subList[0], subList[1]])
        result = sorted(result, key=lambda x: (x[1], x[0]), reverse=True)
        result = [x[0] for x in result]
        return result