class Solution:
    def distributeCandies(self, candies: int, num_people: int) -> List[int]:
        List, i = [0] * num_people, 1
        while candies > 0: 
            List[(i-1) % num_people] += min(i, candies)
            candies, i = candies-i, i+1
        return List