class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        graph = defaultdict(list)
        tickets.sort(key=lambda x: x[1])
        for u, v in tickets:
            graph[u].append(v)
        itinerary, stack = [], ["JFK"]
        while stack:
            current = stack[-1]
            if current in graph and len(graph[current]) > 0:
                stack.append(graph[current].pop(0))
            else:
                itinerary.append(stack.pop())
        return itinerary[::-1]