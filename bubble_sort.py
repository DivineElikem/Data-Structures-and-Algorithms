arr_num = int(input("Number of array elements: "))

n = 1
arr = []
while n <= arr_num:
    arr.append(int(input("> ")))
    n += 1



def bubble_sort(arr):
    n = len(arr)
    for i in range(n-1):
        for j in range(n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

print("Unsorted array: ", arr)
print("Sorted array: ", bubble_sort(arr=arr))
