from random import randint
import time
import Library
a=[]
b=int(input())
for i in range(b):
    a.append(randint(-1000, 1000))
t1=time.time()
print(Library.quick_sort(a))
t2=time.time()
print(t2-t1)
print(Library.merge_sort(a))
t3=time.time()
print(t3-t2)
Library.insertion_sort(a)
t4=time.time()
print(t4-t3)
Library.bubble_sort(a)
t5=time.time()
print(t5-t4)
Library.bogo_sort(a)
t6=time.time()
print(t6-t5)