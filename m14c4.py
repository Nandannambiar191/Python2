def heapsort(arr):
    n = len(arr)

    # Build max heap
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    # Extract the elements one by one
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)

# Heapify function
def heapify(arr, n, i):
    largest = i  # Initialize largest as root
    l = 2 * i + 1  # Left = 2*i + 1
    r = 2 * i + 2  # Right = 2*i + 2

    # See if left child of root exists and is greater than root
    if l < n and arr[l] > arr[largest]:
        largest = l

    # See if right child of root exists and is greater than root
    if r < n and arr[r] > arr[largest]:
        largest = r

    # Change root, if needed
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        # Heapify the root
        heapify(arr, n, largest)

if __name__ == '__main__':
    arr = [12, 11, 13, 5, 6, 7]

    # Function call
    heapsort(arr)
    N = len(arr)

    print("Sorted array is")
    for i in range(N):
        print("%d" % arr[i], end=" ")


"""---------------------------------------------------------------------"""

import heapq

def sortArrayInDescendingOrder(arr):
    minHeap = []
    for num in arr:
        heapq.heappush(minHeap, num)

    result = []
    while minHeap:
        top = heapq.heappop(minHeap)
        result.insert(0, top)

    return result

if __name__ == '__main__':
    arr = [4, 6, 3, 2, 9]
    result = sortArrayInDescendingOrder(arr)

    for num in result:
        print(num, end=' ')
    print()