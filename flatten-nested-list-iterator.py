
class NestedIterator:
  def __init__(self, nested_list):
    self.stack = [[nested_list, 0]]
   
  def has_next(self):
    while self.stack:
      nl, i = self.stack[-1]
      if i == len(nl): 
        self.stack.pop()
      else:
        x = nl[i]
        if x.is_integer():
          return True 
        else:
          self.stack[-1][1] += 1
          self.stack.append([x.get_list(), 0])
     
     return False 
     
  def next(self):
    nl, i = self.stack[-1]
    self.stack[-1][1] += 1
    return nl[i].get_integer()
    
