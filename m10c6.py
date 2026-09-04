def smallest_largest_words(str1):
    word = ""
    all_words = []
    str1 = str1 + " "

    for i in range(0, len(str1)):
        if str1[i] != ' ':
            word = word + str1[i]
        else:
            if word != "":
                all_words.append(word)
            word = ""

    small = large = all_words[0]

    # Find the smallest and largest word in the str1
    for k in range(0, len(all_words)):
        if len(small) > len(all_words[k]):
            small = all_words[k]
        if len(large) < len(all_words[k]):
            large = all_words[k]

    return small, large


# Driver code
s = input("Enter a sentence: ")
small, large = smallest_largest_words(s)
print("Smallest word:", small)
print("Largest word:", large)

"""----------------------------------------------------------------"""

# Checks if s1 is a substring of s2
def isSubstring(s1, s2):
    if s1 in s2:
        return s2.index(s1)
    return -1

# Driver Code
if __name__ == "__main__":
    s1 = "welcome"
    s2 = "welcome to codingal"
    result = isSubstring(s1, s2)
    if result == -1 :
        print("Not present")
    else:
        print("Present at index " + str(result))


"""----------------------------------------------------------------"""

def sort(s):
    # code here
    li = []
    ans = ""
    for i in range(26):
        li.append(0)
    for i in range(len(s)):
        ind = ord(s[i]) - ord('a')
        li[ind] += 1
    for i in range(26):
        if li[i] >= 1:
            for j in range(li[i]):
                ans = ans + chr(ord('a') + i)
    return ans

print(sort("edba"))