def solution(A):
  N = len(A)
  return (N+2)*(N+1)//2 - sum(A)
