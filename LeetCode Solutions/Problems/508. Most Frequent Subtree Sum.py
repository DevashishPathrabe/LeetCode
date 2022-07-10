# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findFrequentTreeSum(self, root: Optional[TreeNode]) -> List[int]:
        counts = collections.Counter()
        def helper(node):
            if not node:
                return 0            
            result = node.val + helper(node.left) + helper(node.right)
            counts[result] += 1        
            return result
        helper(root)
        try:
            freq = counts.most_common(1)[0][1]
            return [x[0] for x in counts.items() if x[1] == freq]
        except:
            return []