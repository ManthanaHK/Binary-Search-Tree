# Determining the height of the tree


from BinaryTree import *

tree = BST()

tree.addNode(20)
tree.addNode(15)
tree.addNode(30)

def find_height(root):
    if root is None:
        return 0
    queue = []
    queue.append(root)
    height = 0

    while queue:
        level_size = len(queue)
        for i in range(level_size):
            node = queue.pop(0)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        height += 1

    return height

assert find_height(tree.root) == 2