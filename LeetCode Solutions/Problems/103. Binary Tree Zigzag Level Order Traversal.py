# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root is None:
            return []
        else:
            ans, q, d = [], [[root, 0]], {}
            while q:
                current, level = q.pop(0)
                if level in d:
                    d[level].append(current.val)
                else:
                    d[level] = [current.val]
                if current.left is not None:
                    q.append([current.left, level+1])
                if current.right is not None:
                    q.append([current.right, level+1])
            for k in sorted(d.keys()):
                if k % 2 ==0:
                    ans.append(d[k])
                else:
                    ans.append(d[k][::-1])
            return ans