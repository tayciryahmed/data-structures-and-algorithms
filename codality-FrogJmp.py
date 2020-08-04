def solution(X, Y, D):
  Y = Y - X 
  ans = Y//D
  if  Y%D != 0: ans +=1
  return ans 
