def in_order_traversal(node):
    if node is None:
        return
    in_order_traversal(node.left)
    print(str(node.value) + ' -> ', end='')
    in_order_traversal(node.right)

in_order_traversal(root)
# Output: 4 -> 2 -> 5 -> 1 -> 3 -> 6 ->