from random import randint
import time
a=[]
b=int(input())
for i in range(b):
    a.append(randint(-100, 100))
print(a)
def merge_sort(arr):
    if len(arr) <= 1:
        return arr  # Базовый случай: массив из 0 или 1 элемента уже отсортирован
    # Делим массив на две части
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)
def merge(left, right):
    sorted_list = []
    i = j = 0
    # Сравниваем элементы левой и правой части и сливаем их в один массив
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            sorted_list.append(left[i])
            i += 1
        else:
            sorted_list.append(right[j])
            j += 1
    sorted_list.extend(left[i:])
    sorted_list.extend(right[j:])
    return sorted_list
# Пример использования
array = [12, 11, 13, 5, 6, 7]
sorted_array = merge_sort(array)
print("Отсортированный массив:", sorted_array)
t1=time.time()
print(merge_sort(a))
t2=time.time()
print(t2-t1)