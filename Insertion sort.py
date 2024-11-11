from random import randint
import time
a=[]
b=int(input())
for i in range(b):
    a.append(randint(-100, 100))
print(a)
def insertion_sort(a):
    for i in range(b):
        for j in range(i+1,b):
            if a[j]<a[i]:
                c=a[j]
                a[j]=a[i]
                a[i]=c
    print(a)
t1=time.time()
insertion_sort(a)
t2=time.time()
print(t2-t1)
