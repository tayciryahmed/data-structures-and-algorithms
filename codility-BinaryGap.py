def sol(n):
  while n%2 == 0: 
    n = n >> 1 
  max_z = 0
  z_count = 0
  while n:
    if n%2==0: 
      z_count += 1
    else:
      if z_count > max_z : 
        max_z = z_count
        z_count = 0
    n = n >> 1

  return  max_z
