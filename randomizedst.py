import random

class Node:
    def __init__(self, key):
        self.key = key
        self.left = self.right = None

    def equals(self, node):
        return self.key == node.key

class RandomizedSplayTree:
    def __init__(self, probability):
        self.root = None
        self.header = Node(None) 
        self.probability = probability
        self.splayn = 0

    def _insert(self, root, node): 
        if self.root == None:
            self.root = node
            return

        if root.key < node.key: 
            if root.right is None: 
                root.right = node 
            else: 
                self._insert(root.right, node) 
        else: 
            if root.left is None: 
                root.left = node 
            else: 
                self._insert(root.left, node) 

    def insert(self, node):
        self._insert(self.root, node)
        p = random.randint(0,self.probability)
        if p == 0:
            self.splayn += 1
            self.splay(node.key)


    def remove(self, key):
        self.splay(key)
        if key != self.root.key:
            raise 'key not found in tree'

        if self.root.left== None:
            self.root = self.root.right
        else:
            x = self.root.right
            self.root = self.root.left
            self.splay(key)
            self.root.right = x

    def find(self, key):
        if self.root == None:
            return None
        self.splay(key)
        if self.root.key != key:
            return None
        return self.root.key
    
    def splay(self, key):
        l = r = self.header
        t = self.root
        self.header.left = self.header.right = None
        while True:
            if key < t.key:
                if t.left == None:
                    break
                if key < t.left.key:
                    y = t.left
                    t.left = y.right
                    y.right = t
                    t = y
                    if t.left == None:
                        break
                r.left = t
                r = t
                t = t.left
            elif key > t.key:
                if t.right == None:
                    break
                if key > t.right.key:
                    y = t.right
                    t.right = y.left
                    y.left = t
                    t = y
                    if t.right == None:
                        break
                l.right = t
                l = t
                t = t.right
            else:
                break
        l.right = t.left
        r.left = t.right
        t.left = self.header.right
        t.right = self.header.left
        self.root = t

    def getSplayn(self):
        return self.splayn

    def getRoot(self):
        return self.root