##Geometric progression

#tN = a1 * r(N-1)

import math

def gp(x, y, N):
  return(x*(int)(math.pow(y, N-1)))

x = 2 #1st term
y = 7 #common ratio
N = 8 #Nth term

print("The", N , "th term in the series is : " , gp(x, y, N))



  