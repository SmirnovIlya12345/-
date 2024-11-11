from random import randint
import time
a=[]
b=int(input())
for i in range(b):
    a.append(randint(-100, 100))
print(a)
def insertion_sort(a):
    for i in range(b):
        for j in range(i):
            if a[i-j]<a[i-j-1]:
                c=a[i-j-1]
                a[i-j-1]=a[i-j]
                a[i-j]=c
            else:
                break
    print(a)
t1=time.time()
insertion_sort(a)
t2=time.time()
print(t2-t1)