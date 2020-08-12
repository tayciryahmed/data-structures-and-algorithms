class Trie:
  def __init__(self):
    self.root_node = {}
  
  def add_word(self, word):
    current_node = self.root_node
    for c in word:
      if c not in current_node:
        new_word = True
        current_node[c] = {}
      
      current_node = current_node[c]
    
    if '*' not in current_node:
      new_word = True 
      current_node['*'] = {}
    
    return new_word
