# merge sort



def merge(left,right):
    s_arr = []
    i = 0
    j = 0
    while i < len(left) and j < len(right):
        if left[i]< right[j]:
            s_arr.append(left[i])
            i += 1
        else:
            s_arr.append(right[j])
            j += 1
    while i < len(left):
        s_arr.append(left[i])
        i += 1
    while j < len(right):
        s_arr.append(right[j])
        j += 1
    return s_arr



def mergesort(arr):
    if len(arr) == 1:
        return arr

    mid_index = int(len(arr)/2)
    left_arr = arr[:mid_index]
    right_arr = arr[mid_index:]
    sorted_left = mergesort(left_arr)
    sorted_right = mergesort(right_arr)
    sorted_arr = merge(sorted_left,sorted_right)
    return sorted_arr




print("Please input array with space:")
line = input()
array = list(map(int, line.split()))
print("Origin array:")
print(array)
array = mergesort(array)
print("Sorted:")
print(array)

