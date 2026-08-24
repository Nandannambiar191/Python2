# Program for Insertion Sort
A = [10, 5, 13, 8, 2]
# traverse through the array
for i in range(1, len(A)):

    value = A[i]

    # Move elements of A[0..i-1], that are
    # greater than value, to one position ahead
    # of their current position
    j = i - 1
    while j >= 0 and value < A[j]:
        A[j + 1] = A[j]
        j -= 1
    A[j + 1] = value

# Driver code

print("Sorted array")
for i in range(len(A)):
    print("%d" %A[i],end=" ")

"""--------------------------------------------------------------------"""

# Program to reverse the same array
A = [1, 2, 3, 4, 5, 6]

# initialising start and end
start = 0
end = len(A) - 1

# reverse A from start to end
while start < end:
    # swapping the elements of an array to reverse it in
    # same array
    A[start], A[end] = A[end], A[start]
    start += 1
    end -= 1

# Driver Code
print("Reversed array is")
print(A)