def solution(v):
    left_sum = 0
    right_sum = sum(v)
    minimal = float('inf')

    for i in range(1, len(v)):
      val = v[i-1]
      left_sum += val
      right_sum -= val
      if minimal > abs(left_sum - right_sum):
        minimal = abs(left_sum - right_sum)
      
    return minimal 
