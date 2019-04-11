# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None



class Solution(object):
    def isLeaf(self, p):
        return (p.left == None) and (p.right == None)
    
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        
        if (not p) and (not q):
            return True
        
        elif p and not q:
            return False
        
        elif q and not p: 
            return False 
            
        if self.isLeaf(p) or self.isLeaf(q):
            if self.isLeaf(q) and self.isLeaf(p) and (p.val == q.val):
                return True 
            else: 
                return False 
            
        elif p.val == q.val:
            return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        
        else:
            return False
        
        return None 
    
    def solIsSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        
        if (not p) and (not q):
            return True
        
        if (not p) or (not q):
            return False 
        
        if p.val != q.val :
            return False 
            
        return self.isSameTree(p.left, q.left) and \
               self.isSameTree(p.right, q.right)
        
