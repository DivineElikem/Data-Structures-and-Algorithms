arr_num = int(input("Number of array elements: "))

n = 1
arr = []
while n <= arr_num:
    arr.append(int(input("> ")))
    n += 1

#Shifting problem
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

#Use swaps instead
def improved_selection_sort(arr):
    n = len(arr)
    for i in range(n):
        s_index = i
        for j in range(i+1, n):
            if arr[j] < arr[s_index]:
                s_index = j

        arr[s_index], arr[i] = arr[i], arr[s_index]

    return arr


print("Unsorted array: ", arr)
print("Selection sort: ", selection_sort(arr=arr))
print("Improved selection sort: ", improved_selection_sort(arr=arr))
