def itemPrice(barcode):
    # list to append the ASCII codes.
    li = []

    for i in barcode:
        n = ord(i)

        # finding the maximum digit of the ASCII code
        if n // 10:
            maxi = 0
            while n > 0:
                if n % 10 > maxi:
                    maxi = n % 10
                n = n // 10
            li.append(maxi)
        else:
            li.append(n)

    # returning the sum of list items
    return sum(li)

barcode = input("Enter barcode: ")
print(itemPrice(barcode))

"""----------------------------------------------------------------"""

# Program to find lexicographically next string

def nextWord(s):

    # If the string is empty,
    if (s == ""):
        return "a"

    # Find the first character from the right
    # which is not z.
    i = len(s) - 1
    while (s[i] == 'z' and i >= 0):
        i -= 1

    # If all characters are 'z', append
    # an 'a' at the end.
    if (i == -1):
        s = s + 'a'

    # If there are some non-z characters
    # else:
    s = s.replace(s[i], chr(ord(s[i]) + 1), 1)

    return s

inp = input("Enter string: ")
print(nextWord(inp))