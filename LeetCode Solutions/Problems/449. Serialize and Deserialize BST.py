# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root: Optional[TreeNode]) -> str:
        """Encodes a tree to a single string.
        """
        if root is None:
            return ''
        return ','.join([
            str(root.val), self.serialize(root.left), self.serialize(root.right)])

    def deserialize(self, data: str) -> Optional[TreeNode]:
        """Decodes your encoded data to tree.
        """
        def helper(nodes):
            try:
                value = nodes.pop()
            except IndexError:
                return
            if value == '':
                return None
            return TreeNode(int(value), helper(nodes), helper(nodes))
        nodes = data.split(',')
        nodes.reverse()
        return helper(nodes)

# Your Codec object will be instantiated and called as such:
# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# tree = ser.serialize(root)
# ans = deser.deserialize(tree)
# return ans