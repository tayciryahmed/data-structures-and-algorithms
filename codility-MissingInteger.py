def solution(A):
  A = [x for x in A if x>0]
  A = set(A)
  for i in range(1, 1000000):
    if i not in A:
      return i 
  
  return 1000000
