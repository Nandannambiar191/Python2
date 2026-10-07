def heapify(arr, n, i):
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2

    if l < n and arr[largest] < arr[l]:
        largest = l

    if r < n and arr[largest] < arr[r]:
        largest = r

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)

def insert(array, newNum):
    array.append(newNum)
    # Rebuild heap from bottom-up
    for i in range(len(array)//2 - 1, -1, -1):
        heapify(array, len(array), i)

def deleteNode(array, num):
    size = len(array)
    if size == 0:
        return

    # Find the element
    for i in range(size):
        if num == array[i]:
            break
    else:
        return  # num not found

    # Swap with last and remove
    array[i], array[size - 1] = array[size - 1], array[i]
    array.pop()

    # Rebuild heap
    for i in range(len(array)//2 - 1, -1, -1):
        heapify(array, len(array), i)

arr = []

insert(arr, 3)
insert(arr, 4)
insert(arr, 9)
insert(arr, 5)
insert(arr, 2)

print("Max-Heap array: " + str(arr))

deleteNode(arr, 4)
print("After deleting an element: " + str(arr))

"""---------------------------------------------------------------------"""

def heapify(arr, n, i):
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2
    if l < n and arr[i] < arr[l]:
        largest = l
    if r < n and arr[largest] < arr[r]:
        largest = r
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)

arr = [4, 10, 3, 5, 1]
n = len(arr)
for i in range(n, -1, -1):
    heapify(arr, n, i)
print(arr)