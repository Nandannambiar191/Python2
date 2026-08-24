# Program to sort 0s and 1s in an array

def sortZeroOne(A, n) :

    # Count the no of zeros in an array
    count = 0

    for i in range(0, n) :
        if (A[i] == 0) :
            count = count + 1

    # Filling the A with 0 until count
    for i in range(0, count) :
        A[i] = 0

    # Filling remaining space with 1
    for i in range(count, n) :
        A[i] = 1

# Driver code
A = [ 0, 1, 0, 1, 1, 1 ]
n = len(A)

sortZeroOne(A, n)
print("Sorted Array is ", end = "")
for i in range(0, n) :
    print(A[i], end = " ")

"""--------------------------------------------------------------------"""

def unionOfArrays(A1, A2, m, n):
    i, j = 0, 0
    while i < m and j < n:
        if A1[i] < A2[j]:
            print(A1[i], end=" ")
            i += 1
        elif A2[j] < A1[i]:
            print(A2[j], end=" ")
            j += 1
        else:
            print(A2[j], end=" ")
            j += 1
            i += 1

    # Remaining elements of the greater sized array
    while i < m:
        print(A1[i], end=" ")
        i += 1

    while j < n:
        print(A2[j], end=" ")
        j += 1

# Driver code
A1 = [1, 2, 8, 9]
A2 = [2, 3, 5, 7]
m = len(A1)
n = len(A2)
unionOfArrays(A1, A2, m, n)