s = input()
seen = set()
answer = ""

for char in s:
    if char not in seen:
        seen.add(char)
        answer += char

print(answer)