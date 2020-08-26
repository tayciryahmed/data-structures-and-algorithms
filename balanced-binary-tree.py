# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        
        def check(root):
            if root is None: return True, -1
            
            left = check(root.left)
            if not left[0]:
                return False, 0
            
            right = check(root.right)
            if not right[0]:
                return False, 0 
            
            balanced = abs(left[1]-right[1]) <= 1
            height = max(left[1], right[1]) + 1
            
            return balanced, height
    
        return check(root)[0]
            
            
