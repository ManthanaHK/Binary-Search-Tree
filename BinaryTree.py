class BST:
    class Node:
        def __init__(self,ele):
            self.data = ele
            self.left = None
            self.right = None

    def __init__(self):
        self.root = None
        self.count = 0
    
    def isEmpty(self):
        return self.count == 0
    
    def getNodeCount(self):
        return self.count
    
    def addNode(self,ele):
        cur = parent = self.root
        while cur != None and cur.data != ele:
            parent = cur
            if ele > cur.data:
                cur = cur.right
            else:
                cur = cur.left
        if cur == None:
            newNode = self.Node(ele)
            if parent == None:
                self.root = newNode
            elif ele > parent.data:
                parent.right = newNode
            elif ele < parent.data:
                parent.left = newNode
            self.count += 1
            return self.count
        
    def inOrder(self):
        if not self.isEmpty():
            self._inOrder_(self.root)
    def _inOrder_(self,node):
        if node != None:
            self._inOrder_(node.left)
            print(node.data)
            self._inOrder_(node.right)
