from random import randint
import time
a=[]
b=int(input())
for i in range(b):
    a.append(randint(-100, 100))
print(a)
def insertion_sort(a):
    d=0
    for k in range(b-d-1):
        for j in range(b-1):
            while True:
                if a[j]<a[k]:
                    break
                else:
                    c=a[j]
                    a[j]=a[k]
                    a[k]=c
                    print(a)
        d+=1
    print(a)
t1=time.time()
insertion_sort(a)
t2=time.time()
print(t2-t1)