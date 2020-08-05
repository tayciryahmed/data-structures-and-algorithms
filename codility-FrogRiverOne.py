def solution(N, A):
  seen = [False]*N
  total = N
  for idx, i in enumerate(A):
      if i <= N and not seen[i-1]:
          seen[i-1] = True
          total -= 1

      if total == 0: 
         return idx
         
  return -1
