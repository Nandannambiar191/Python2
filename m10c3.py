# function to count the frequency of each
# character in a string
def frequency(s):
    # creating a dictionary to store the frequency
    # of each character
    s = s.lower()  # ignoring case
    d = {}
    for i in range(len(s)):
        # checking if the character is already
        # in the dictionary
        if s[i] in d.keys():
            d[s[i]] += 1
        else:
            d[s[i]] = 1
    return d

# driver code
inp = input("Enter String: ")
print(frequency(inp))

"""----------------------------------------------------------------"""

# Count how many times each letter comes in a word
def frequency(word):
    word = word.replace(" ", "").lower()  # remove spaces + make all letters small
    counts = {}

    for letter in word:
        if letter in counts:
            counts[letter] += 1
        else:
            counts[letter] = 1

    return counts

# Check if two words are anagrams (same letters, same count)
def checkAnagrams(word1, word2):
    if frequency(word1) == frequency(word2):
        return True
    else:
        return False

# Driver code
word1 = input("Enter first word: ")
word2 = input("Enter second word: ")

print(checkAnagrams(word1, word2))

"""----------------------------------------------------------------"""

# function to count the number of words in a string

def countWords(s):
    count = 0
    # removing leading and trailing spaces from the string
    s = s.strip()
    for i in range(len(s)):
        if s[i] == " ":
            count += 1

    return count + 1 # +1 id for last word

# driver code
inp = input("Enter String: ")
print("Number of words: ", countWords(inp))