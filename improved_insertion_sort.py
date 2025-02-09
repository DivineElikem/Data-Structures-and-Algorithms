arr_num = int(input("Number of array elements: "))

n = 1
arr = []
while n <= arr_num:
    arr.append(int(input("> ")))
    n += 1


def insertion_sort(arr):
    n = len(arr)
    for i in range(1, n):
        insert_index = i
        current_num = arr.pop(i)
        for j in range(i-1, -1, -1):
            if current_num < arr[j]:
                insert_index = j
        arr.insert(insert_index, current_num)

    return arr


#Reduce number of shifts
def improved_insertion_sort(arr):
    n = len(arr)
    for i in range(1, n):
        insert_index = i
        current_num = arr[i]
        for j in range(i-1, -1, -1):
            if current_num < arr[j]:
                arr[j+1] = arr[j]
                insert_index = j
            else:
                break
        arr[insert_index] = current_num

    return arr

print("Unsorted array: ", arr)
print("Insertion sort: ", insertion_sort(arr=arr))
print("Improved insertion sort: ", improved_insertion_sort(arr=arr))

