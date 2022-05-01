# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator(object):

    def __init__(self, root):
        """
        :type root: TreeNode
        """
        self.root = root
        self.stack = []
        self.arr = []
        curr = self.root
        while(curr or self.stack):
            while(curr):
                self.stack.append(curr)
                curr = curr.left
            curr = self.stack.pop()
            self.arr.append(curr.val)
            curr = curr.right
        print(self.arr)

    def next(self):
        """
        :rtype: int
        """
        if(self.arr):
            return self.arr.pop(0)

    def hasNext(self):
        """
        :rtype: bool
        """
        if(self.arr):
            return True
        return False


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()