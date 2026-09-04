# function to reverse the string

def reverse(s):

    n = len(s)

    # converting string to list

    li = list(s)

    for i in range(n//2):

    # swapping first and last, second and

    # second last, and so on.

        li[i], li[n-i-1] = li[n-i-1], li[i]

        return "".join(li)

# driver code

inp = input("Enter String: ")

print(reverse(inp))

"""----------------------------------------------------------------"""

# Python program to demonstrate string slicing

# Input string

inp = 'CODINGAL'

# string slicing using indexing sequence

print(inp[:3])

print(inp[3:])

print(inp[1:5:2])

# print the string in reverse order using slicing

print(inp[::-1])

print(inp[-1:-9:-2])

print(inp[-2:-9:-2])