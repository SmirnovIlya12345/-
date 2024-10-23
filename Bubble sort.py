from random import randint
import time
a=[]
b=int(input())
for i in range(b):
    a.append(randint(-100, 100))
print(a)
def bubble_sort(a):
    d=0
    for k in range(b-d-1):
        for j in range(b-1):
            if a[j]>a[j+1]:
                c=a[j]
                a[j]=a[j+1]
                a[j+1]=c
        d+=1
    print(a)
t1=time.time()
bubble_sort(a)
t2=time.time()
print(t2-t1)