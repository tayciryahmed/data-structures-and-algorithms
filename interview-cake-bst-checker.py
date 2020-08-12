# recursive : using call stack

def _is_binary_search_tree(root, low, high):
    
    if not root:
        return True
    
    if root.value >= high or root.value <= low: return False
    
    
    return _is_binary_search_tree(root.right, root.value, high
    ) and _is_binary_search_tree(root.left, low, root.value) 
    



def is_binary_search_tree(root):
    if not root or (not root.left and not root.right):
        return True
        
    return _is_binary_search_tree(root.right, low=root.value, high=float('inf')
    ) and _is_binary_search_tree(root.left, low=float('-inf'), high=root.value) 



# using stack 


def is_binary_search_tree(root):
    node_bounds_stack = [(root, float('-inf'), float('inf'))]
    
    while node_bounds_stack:
        node, low, high = node_bounds_stack.pop()
        
        if node.value <= low or node.value >= high: return False
        
        if node.left:
            node_bounds_stack.append([node.left, low, node.value])
        
        if node.right:
            node_bounds_stack.append([node.right, node.value, high])
    
    return True
            
