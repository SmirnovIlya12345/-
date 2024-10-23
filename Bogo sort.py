from random import randint
import time
a=[]
b=int(input())
for i in range(b):
    a.append(randint(-100, 100))
print(a)
def bogo_sort(a):
    q=0
    while True:
        c=0
        for j in range(b-1):
            if a[j]>a[j+1]:
                c=1
                break
        if c==0:
            break
        else:
            r1=randint(0, b-1)
            r2=randint(0, b-1)
            c=a[r1]
            a[r1]=a[r2]
            a[r2]=c
            q+=1
    print(a,q)
t1=time.time()
bogo_sort(a)
t2=time.time()
print(t2-t1)