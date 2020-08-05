def solution(S, P, Q):
  ans = [0]*len(P)
  for i in range(len(P)):
    if 'A' in S[P[i]:Q[i]+1]:
      ans[i] = 1
    elif 'C' in S[P[i]:Q[i]+1]:
      ans[i] = 2
    elif 'G' in S[P[i]:Q[i]+1]:
      ans[i] = 3
    elif 'T' in S[P[i]:Q[i]+1]:
      ans[i] = 4
  return ans
