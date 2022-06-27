# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        indexMap = {inorder[i]: i for i in range(len(inorder))}
        return self.splitTree(preorder, inorder, indexMap, 0, 0, len(preorder)-1)
    def splitTree(self, preorder: List[int], inorder: List[int], indexMap: dict, preorderIndex: int, Ileft: int, Iright: int) -> TreeNode:
        rightValue = preorder[preorderIndex]
        root, Imid = TreeNode(rightValue), indexMap[rightValue]
        if (Imid > Ileft):
            root.left = self.splitTree(preorder, inorder, indexMap, preorderIndex+1, Ileft, Imid-1)
        if (Imid < Iright):
            root.right = self.splitTree(preorder, inorder, indexMap, preorderIndex+Imid-Ileft+1, Imid+1, Iright)
        return root