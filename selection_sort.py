arr_num = int(input("Number of array elements: "))

n = 1
arr = []
while n <= arr_num:
    arr.append(int(input("> ")))
    n += 1


def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        s_index = i
        for j in range(i+1, n):
            if arr[j] < arr[s_index]:
                s_index = j
        s_value = arr.pop(s_index)
        arr.insert(i, s_value)

    return arr
print("Unsorted array: ", arr)
print("Sorted array: ", selection_sort(arr=arr))
