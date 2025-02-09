arr_num = int(input("Number of array elements: "))

n = 1
arr = []
while n <= arr_num:
    arr.append(int(input("> ")))
    n += 1

#Unnecessary comparisons
def bubble_sort(arr):
    num_iter = 0
    n = len(arr)
    for i in range(n-1):
        num_iter += 1
        for j in range(n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr, num_iter

#Use swap check for comparisons
def improved_bubble_sort(arr):
    num_iter = 0
    n = len(arr)
    for i in range(n-1):
        swapped = False
        num_iter += 1
        for j in range(n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        if not swapped:
            break
    return arr, num_iter

print("Unsorted array: ", arr)
print("Bubble sort: ", bubble_sort(arr=arr))
print("Improved bubble sort: ", improved_bubble_sort(arr=arr))
