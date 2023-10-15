# Couting the number of terminal nodes


from BinaryTree import *

tree = BST()

def getLeafNodeCount():
    if not tree.isEmpty():
        return leafCount(tree.root)
    else:
        return 0

def leafCount(node):
    if node:
        if isLeafNode(node):
            return 1
        else:
            return(leafCount(node.left) + leafCount(node.right))
    return 0

def isLeafNode(node):
    if node.left == None and node.right == None:
        return True
    else:
        return False
