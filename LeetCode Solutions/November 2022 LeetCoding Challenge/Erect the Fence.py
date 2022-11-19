class Solution:
    def outerTrees(self, trees: List[List[int]]) -> List[List[int]]:
        def helper(A, B, C):
            return (B[0]-A[0])*(C[1]-A[1]) - (B[1]-A[1])*(C[0]-A[0])
        if len(trees) <= 1:
            return trees
        coordinatesOfTrees = []
        trees.sort()
        for i in itertools.chain(range(len(trees)), reversed(range(len(trees)-1))):
            while len(coordinatesOfTrees) >= 2 and helper(coordinatesOfTrees[-2], coordinatesOfTrees[-1], trees[i]) < 0:
                coordinatesOfTrees.pop()
            coordinatesOfTrees.append(trees[i])
        coordinatesOfTrees.pop()
        for i in range(1, (len(coordinatesOfTrees)+1)//2):
            if coordinatesOfTrees[i] != coordinatesOfTrees[-1]:
                break
            coordinatesOfTrees.pop()
        return coordinatesOfTrees