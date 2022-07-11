# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class CBTInserter:

    def __init__(self, root: Optional[TreeNode]):
        self.head = root

    def insert(self, val: int) -> int:
        root = self.head
        if root == None:
            root.data = val
            return root.val
        else:
            queue = [root]
            nextqueue = []
            while queue != []:
                for root in queue:
                    if root.left is  None:
                        root.left = TreeNode(val)
                        return root.val
                    else:
                         nextqueue.append(root.left)
                    if root.right is None:
                        root.right = TreeNode(val)
                        return root.val
                    else:
                        nextqueue.append(root.right)
                queue = nextqueue
                nextqueue = []

    def get_root(self) -> Optional[TreeNode]:
        return self.head


# Your CBTInserter object will be instantiated and called as such:
# obj = CBTInserter(root)
# param_1 = obj.insert(val)
# param_2 = obj.get_root()