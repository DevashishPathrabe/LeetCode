class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people = sorted(people)
        start = minNumberOfBoats = 0
        end = len(people) - 1
        while(start <= end):
            if(people[start] + people[end] <= limit):
                start += 1
            end -= 1
            minNumberOfBoats += 1
        return minNumberOfBoats