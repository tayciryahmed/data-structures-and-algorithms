def solution(A, K):
  if len(A) <=1: return A
  K = K % len(A)
  return A[-K:]+A[:-K]
