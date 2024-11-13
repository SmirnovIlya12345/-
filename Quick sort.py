from random import randint
import time
a=[]
b=int(input())
for i in range(b):
    a.append(randint(-100, 100))
print(a)
from random import randint
def quick_sort(a, b):
    if len(a)<=1:
        return a
    else:
        big = []
        middle = []
        small = []
        if len(a)>2:
            d=max(min(a[0],a[1]),min(a[1],a[2]),min(a[0],a[2]))
        else:
            d=a[0]
        for i in range(b):
            if a[i]>d:
                big.append(a[i])
            elif a[i]<d:
                small.append(a[i])
            else:
                middle.append(a[i])
        return quick_sort(small, len(small))+[middle[0]]*len(middle)+quick_sort(big, len(big))
t1=time.time()
print(quick_sort(a, b))
t2=time.time()
print(t2-t1)



