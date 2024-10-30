from random import randint
import time
a=[]
b=int(input())
for i in range(b):
    a.append(randint(-100, 100))
print(a)
def quick_sort ( A, nStart, nEnd ):
  if nStart >= nEnd: return
  L = nStart; R = nEnd
  X = A[(L+R)//2]
  while L <= R:
    while A[L] < X: L += 1
    while A[R] > X: R -= 1
    if L <= R:
      A[L], A[R] = A[R], A[L]
      L += 1; R -= 1
  quick_sort ( A, nStart, R )
  quick_sort ( A, L, nEnd )
t1=time.time()
quick_sort(a, 0, b-1)
print(a)
t2=time.time()
print(t2-t1)