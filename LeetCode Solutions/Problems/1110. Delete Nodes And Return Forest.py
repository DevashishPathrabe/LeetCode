# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        result = []
        to_delete = set(to_delete)
        def helper(node, isroot):
            if not node:
                return
            nodeDel = node.val in to_delete
            if isroot and not nodeDel:
                result.append(node)
            node.left = helper(node.left, nodeDel)
            node.right = helper(node.right, nodeDel)
            return None if nodeDel else node
        helper(root, True)
        return result