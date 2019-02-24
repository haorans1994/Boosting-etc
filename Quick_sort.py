# This is quick sort

def quicksort(arr):
    if len(arr) <= 1:
        return arr
    left = []
    right = []
    pivot = arr.pop()
    for element in arr:
        if pivot > element:
            left.append(element)
        else:
            right.append(element)
    new_arr = quicksort(left)+[pivot]+quicksort(right)
    return new_arr




print("Please input array with space:")
line = input()
array = list(map(int, line.split()))
print("Origin array:")
print(array)
array = quicksort(array)
print("Sorted:")
print(array)