# Program to rotate an array 'n' times

# Input array, length and 'n'
def rotations(a, n, a_size):
    for i in range(n):
        rotate(a, a_size)

# Rotate array to the left by 1 place
def rotate(a, a_size):
    temp = a[0]
    for i in range(a_size-1):
        a[i] = a[i + 1]
    a[a_size-1] = temp

def printArray(a, a_size):
    for i in range(a_size):
        print("% d" % a[i], end = " ")
    print("\n")

a = [12,1,31,85,2,3,53,56323]
printArray(a,len(a))
rotations(a, 2, len(a))
printArray(a, len(a))

"""--------------------------------------------------------------------"""

# Program to check the array is rotated and sorted
arr = [3, 4, 5, 1, 2]
n = len(arr)
count = 0

# interating loop from 1 to length of array
for i in range(1, n):
    # comparing items of array
    if(arr[i-1]>arr[i]):
        count+=1

# special case- comparing last element to the first element
if(arr[n-1]>arr[0]):
    count+=1

# driver code
print(count<=1)