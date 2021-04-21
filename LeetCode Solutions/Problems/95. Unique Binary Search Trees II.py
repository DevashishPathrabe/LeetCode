# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def generateTrees(self, n: int) -> List[TreeNode]:
        def generate(left, right):
            if(left == right):
                return [None]
            nodes = []
            for i in range(left, right):
                for leftchild in generate(left, i):
                    for rightchild in generate(i+1, right):
                        node = TreeNode(i+1)
                        node.left = leftchild
                        node.right = rightchild
                        nodes.append(node)
            return nodes
        if(n):
            return generate(0, n)
        else:
            []