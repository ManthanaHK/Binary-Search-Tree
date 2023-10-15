# Traversing the tree in Decreasing Order


from BinaryTree import *

tree = BST()

tree.addNode(45)
tree.addNode(5)
tree.addNode(10)
tree.addNode(9)

def inOrder():
    if not tree.isEmpty():
        inOrderOppo(tree.root)

def inOrderOppo(node):
    if node != None:
        inOrderOppo(node.right)
        print(node.data)
        inOrderOppo(node.left)

inOrder()