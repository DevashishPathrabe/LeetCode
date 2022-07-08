# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        d = dict()
        s = set()
        for par, child, is_left in descriptions:
            s.add(child)
            if par not in d:
                d[par] = TreeNode(par)
            if child not in d:
                d[child] = TreeNode(child)
            if is_left:                
                d[par].left = d[child]
            else:
                d[par].right = d[child]
        root = set(d.keys()) - s
        return d[root.pop()]