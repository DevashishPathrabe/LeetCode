"""
   This is the custom function interface.
   You should not implement it, or speculate about its implementation
   class CustomFunction:
       # Returns f(x, y) for any given positive integers x and y.
       # Note that f(x, y) is increasing with respect to both x and y.
       # i.e. f(x, y) < f(x + 1, y), f(x, y) < f(x, y + 1)
       def f(self, x, y):
  
"""

class Solution:
    def findSolution(self, customfunction: 'CustomFunction', z: int) -> List[List[int]]:
        A, Y = [], z+1        
        for x in range(1, z+1):
            if customfunction.f(x, 1) > z:
                return A
            for y in range(Y, 0, -1):
                if customfunction.f(x, y) == z:
                    Y, _ = y-1, A.append([x, y])
                    break
        return A