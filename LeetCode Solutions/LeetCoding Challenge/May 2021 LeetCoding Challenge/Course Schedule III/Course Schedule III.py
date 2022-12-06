class Solution:
    def scheduleCourse(self, courses: List[List[int]]) -> int:
        heap, total = [], 0
        for duration, end in sorted(courses, key=lambda el: el[1]):
            if (duration + total <= end):
                total += duration
                heappush(heap, -duration)
            elif (heap and -heap[0] > duration):
                total += duration + heappop(heap)
                heappush(heap, -duration)
        return len(heap)