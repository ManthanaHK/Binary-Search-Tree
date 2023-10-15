# Traversing the tree --> InOrder, PreOrder, PostOrder, LevelOrder


from BinaryTree import *
from dynamicQueue import *

tree = BST()

def inOrderTraverse():
    if not tree.isEmpty():
        traverseInorder(tree.root)

def traverseInorder(node):
    if node != None:
        traverseInorder(node.left)
        print(node.data)
        traverseInorder(node.right)

def preOrderTraverse():
    if not tree.isEmpty():
        traversePreorder(tree.root)

def traversePreorder(node):
    if node != None:
        print(node.data)
        traversePreorder(node.left)
        traversePreorder(node.right)

def postOrderTraverse():
    if not tree.isEmpty():
        traversePostorder(tree.root)

def traversePostorder(node):
    if node != None:
        traversePostorder(node.left)
        traversePostorder(node.right)
        print(node.data)

def levelOrderTraverse():
    if not tree.isEmpty():
        q1 = DynamicQueue()
        q1.enque(tree.root)
        while not q1.isQueueEmpty():
            node = q1.deque()
            print(node.data)
            if node.left:
                q1.enque(node.left)
            if node.right:
                q1.enque(node.right)
