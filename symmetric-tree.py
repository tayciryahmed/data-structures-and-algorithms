# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class PyQueue:
    def __init__(self):
        self._data = []
    def enqueue(self, node):
        self._data.append(node)
    def dequeue(self):
        return self._data.pop(0)
    def isEmpty(self):
        return len(self._data) == 0

#iterative solution 
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        q = PyQueue()
        q.enqueue(root)
        q.enqueue(root)
        
        while not q.isEmpty():
            t1 = q.dequeue()
            t2 = q.dequeue()
            
            if t1==None and t2==None: 
                continue
            if t1==None or t2==None:
                return False
            if t1.val != t2.val :
                return False
            
            q.enqueue(t1.left)
            q.enqueue(t2.right)
            q.enqueue(t1.right)
            q.enqueue(t2.left)
        
        return True
 
 #recursive solution
 class Solution:
    def mirror(self, t1, t2):
        if t1==None and t2==None: return True 
        if t1==None or t2==None : return False
        return t1.val==t2.val and self.mirror(t1.right, t2.left) and self.mirror(t1.left, t2.right)
        
    def isSymmetric(self, root: TreeNode) -> bool:
        return self.mirror(root, root)
