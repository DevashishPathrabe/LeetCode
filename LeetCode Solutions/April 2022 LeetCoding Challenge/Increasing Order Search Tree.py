result = []
        def inorder(node):
            if(node is None):
                return
            inorder(node.left)
            result.append(node)
            inorder(node.right)
        inorder(root)
        for i in range(len(result) - 1):
            result[i].left = None
            result[i].right = result[i + 1]
        result[len(result) - 1].left = None
        result[len(result) - 1].right = None
        return result[0]