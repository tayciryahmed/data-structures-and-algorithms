def solution(N, A):
  max_current_counter = 0
  max_global_counter = 0 
  ans = [0]*N
  for i in range(len(A)):
    if 1<=A[i]<=N:
      ans[A[i]-1] = max(max_global_counter, ans[A[i]-1]) + 1
      max_current_counter = max(max_current_counter, ans[A[i]-1])

    elif A[i] == N+1:
      max_global_counter = max_current_counter
    
    for i in range(N):
      ans[i] = max(ans[i], max_global_counter)

  return ans 
  
  
def solution(N, A):
  ans = [0] * N
  for x in A:
    if 1<=x<=N:
      ans[x-1] += 1
    else:
      ans = [max(ans)]*N
  return ans 
