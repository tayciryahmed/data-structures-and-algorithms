def solution(A):
  n = len(A)
  A = set(A)
  if len(A) != n: return 0
  for i in range(len(A)):
    if i+1 not in A:
      return 0
  return 1
