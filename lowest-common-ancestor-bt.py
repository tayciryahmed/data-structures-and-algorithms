def lca(root, p, q):
  if root is None: return None
  if root == p or root == q: return root
  
  right = lca(root.right, p, q)
  left = lca(root.left, p, q)
  
  if right is None and left is None : return None
  if right is None : return left 
  if left is None: return right
  return root 
  
#if BST

def lca (root, p, q):
  if p.val < root.val and q.val < root.val:
    return lca(root.left, p, q)
  if p.val > root.val and q.val > root.val:
    return lca(root.right, p, q)
  
  return root 
