def postOrder(root):
    if root:
        if root.left:
            postOrder(root.left)
        if root.right:
            postOrder(root.right)
        print(root.info, '', end='')