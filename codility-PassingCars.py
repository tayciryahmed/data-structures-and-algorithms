def solution(A):
  c_0 = 0
  sum = 0
  for i in A:
    if i == 0:
      c_0 += 1
    else:
      sum += c_0
    
  if sum > 1000000000  : return -1 

  return sum
