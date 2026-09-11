from sys import maxsize

def createStack():
    stack = []
    return stack

def isEmpty(stack):
    return len(stack) == 0

def push(stack, item):
    stack.append(item)
    print(item + " pushed to stack ")

def pop(stack):
    if isEmpty(stack):
        return str(-maxsize - 1)
    return stack.pop()

def peek(stack):
    if isEmpty(stack):
        return str(-maxsize - 1)
    return stack[len(stack) - 1]

stack = createStack()
push(stack, str(10))
push(stack, str(20))
push(stack, str(30))
print(pop(stack) + " popped from stack")

"""----------------------------------------------------------------"""

# Python linear time solution for stock span problem
def calculateSpan(price, S):

    n = len(price)
    st = []
    st.append(0)

    S[0] = 1

    for i in range(1, n):
        while(len(st) > 0 and price[st[-1]] <= price[i]):
            st.pop()
        S[i] = i + 1 if len(st) == 0 else (i - st[-1])
        st.append(i)

def printArray(arr, n):
    for i in range(0, n):
        print(arr[i], end=" ")

price = [10, 4, 5, 90, 120, 80]
S = [0 for i in range(len(price)+1)]

calculateSpan(price, S)

printArray(S, len(price))