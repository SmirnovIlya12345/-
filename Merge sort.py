from random import randint
import time
a=[]
b=int(input())
for i in range(b):
    a.append(randint(-1000, 1000))
print(a)
print(b)
def merge_sort(a):
    if len(a)<=1:
        return(a)
    else:
        a1=merge_sort(a[:len(a)//2])
        a2=merge_sort(a[len(a)//2:])
        return glue(a1, a2)
def glue(a1, a2):
    a3=[]
    i=0
    j=0
    while i<len(a1) and j<len(a2):
        if a2[j]<a1[i]:
            a3.append(a1[i])
            i=i+1
        else:
            a3.append(a2[j])
            j=j+1
    a3.extend(a1[i:])
    a3.extend(a2[j:])
    return a3
t1=time.time()
print(merge_sort(a))
t2=time.time()
print(t2-t1)