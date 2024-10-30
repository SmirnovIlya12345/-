from random import randint
import time
a=[]
b=int(input())
for i in range(b):
    a.append(randint(-100, 100))
print(a)
def merge_sort(a, b):
    if b<=1:
        return(b)
    else:
        def part(a):
            while len(a)>2:
                a1=a[0:len(a)//2:1]
                a2=a[len(a)//2:len(a):1]
                return part(a1), part(a2)
        for i in range(b):
            part(a)
    A=[]
    if a1[1]<a2[1]:
        A.append(a1[1])
    else:
        A.append(a2[1])
t1=time.time()
print(merge_sort(a, b))
t2=time.time()
print(t2-t1)