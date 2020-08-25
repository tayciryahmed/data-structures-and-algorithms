def solution(A):
  unseen = set()
  for i in A:
    if i not in unseen:
      unseen.add(i)
    else:
      unseen.remove(i)
  
  return unseen.pop()
