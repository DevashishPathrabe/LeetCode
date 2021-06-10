# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: TreeNode) -> List[List[int]]:
        result = []
        def helper(node, x, y):
            if(not node):
                return
            result.append(((x, y), node.val))
            helper(node.left, x - 1, y + 1)
            helper(node.right, x + 1, y + 1)
        helper(root, 0, 0)
        result.sort()
        groups = collections.defaultdict(list)
        for k, v in result:
            x, _ = k
            groups[x].append(v)
        verticalOrderTraversal = []
        for k in sorted(list(groups.keys())):
            verticalOrderTraversal.append(groups[k])
        return verticalOrderTraversal