from random import randint


def quick_sort(a):
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
        for i in range(len(a)):
            if a[i]>d:
                big.append(a[i])
            elif a[i]<d:
                small.append(a[i])
            else:
                middle.append(a[i])
        return quick_sort(small)+[middle[0]]*len(middle)+quick_sort(big)
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
def insertion_sort(a):
    for i in range(len(a)):
        for j in range(i+1,len(a)):
            if a[j]<a[i]:
                c=a[j]
                a[j]=a[i]
                a[i]=c
    print(a)
def bubble_sort(a):
    d=0
    for k in range(len(a)-d-1):
        for j in range(len(a)-1):
            if a[j]>a[j+1]:
                c=a[j]
                a[j]=a[j+1]
                a[j+1]=c
        d+=1
    print(a)
def bogo_sort(a):
    q=0
    while True:
        c=0
        for j in range(len(a)-1):
            if a[j]>a[j+1]:
                c=1
                break
        if c==0:
            break
        else:
            r1=randint(0, len(a)-1)
            r2=randint(0, len(a)-1)
            c=a[r1]
            a[r1]=a[r2]
            a[r2]=c
            q+=1
    print(a,q)