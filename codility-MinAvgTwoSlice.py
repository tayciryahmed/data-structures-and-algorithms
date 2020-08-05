def solution(A):
  sum = A[0] + A[1]
  left_index, min_left_index = 0,0 
  min_avg = (A[0]+A[1])/2
  for i in range(2, len(A)):
    sum += A[i]

    avg_with_prev = sum/(i-left_index+1)
    avg_of_two = (v[i-1]+v[i]) / 2
    if avg_of_two < avg_with_prev:
      avg_here = avg_of_two
      left_index = i - 1
      sum = v[i-1]+v[i]
    else:
      avg_here = avg_with_prev
    if avg_here < min_avg:
      min_avg = avg_here
      min_left_index = left_index

  return min_left_index
