# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flipMatchVoyage(self, root: TreeNode, voyage: List[int]) -> List[int]:
        listOfValues = [0]
        def helper(node, voyage, listOfValues):
            if(not node or listOfValues[0] == -1):
                return
            if(node.val != voyage[listOfValues[0]]):
                listOfValues[0] = -1
            else:
                listOfValues[0] += 1
                if(node.left and node.left.val != voyage[listOfValues[0]]):
                    listOfValues.append(node.val)
                    helper(node.right, voyage, listOfValues)
                    helper(node.left, voyage, listOfValues)
                else:
                    helper(node.left, voyage, listOfValues)
                    helper(node.right, voyage, listOfValues)
        helper(root, voyage, listOfValues)
        if(listOfValues[0] == -1):
            return listOfValues[:1]
        else:
            return listOfValues[1:]