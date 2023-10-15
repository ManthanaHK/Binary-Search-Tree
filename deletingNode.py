# Deleting operation in Binary Search Tree


from BinaryTree import *

tree = BST()

def deletingNode(key):
    if not tree.isEmpty():
        tree.root = nodeDelete(tree.root,key)
    
def nodeDelete(node,key):
    if node == None:
        return None
    elif key < node.data:
        node.left = nodeDelete(node.left,key)
    elif key > node.data:
        node.right = nodeDelete(node.right,key)
    elif node.left and node.right:
        temp = findMin(node.right)
        node.data = temp.data
        node.right = nodeDelete(node.right,temp.data)
    else:
        if node.right == None:
            node = node.left
        elif node.left == None:
            node = node.right
        tree.count -= 1
    return node

def findMin(node):
    if node.left == None:
        return node
    else:
        return (findMin(node.left))

