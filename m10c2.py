# python program to change the cases of letters
# in a string
def changeTheCase(s):
    result = ""
    for i in s:
        # changing lower case to upper case
        if i.islower():
            result = result + i.upper()
        # upper case to lower case
        if i.isupper():
            result = result + i.lower()
    return result

# driver code
inp = input("Enter String: ")
print("String after change lower case to upper and vice versa-")
print(changeTheCase(inp))

"""----------------------------------------------------------------"""

# function to reverse a string
def reverse(s):
    return s[::-1]

# function to check the string is a palindrome
def checkPalindrome(s):

    # ignoring case
    s = s.lower()

    rev_string = reverse(s)

    if s == rev_string:
        return True
    else:
        return False

# driver code
inp = input("Enter String: ")
print(checkPalindrome(inp))

"""----------------------------------------------------------------"""

def removeVowels(s):
    result = ""
    # list containing vowels
    li = ['a', 'e', 'i', 'o', 'u']
    for i in range(len(s)):
        # checking the presence of vowels in the string
        if s[i] in li:
            # removing vowels
            result = result + " "
        else:
            result = result + s[i]
    return result

# driver code
inp = input("Enter String: ")
print("Result:", removeVowels(inp))