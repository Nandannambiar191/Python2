# Program to implement two stacks in an array/list
import math

class twoStacks:
    def __init__(self, n):
        self.size = n
        self.ar = [None] * n
        self.top1 = math.floor(n/2) + 1
        self.top2 = math.floor(n/2)

    def push1(self, x):
        if self.top1 > 0:
            self.top1 = self.top1 - 1
            self.ar[self.top1] = x
        else:
            print("Stack Overflow by element : ", x)

    def push2(self, x):
        if self.top2 < self.size - 1:
            self.top2 = self.top2 + 1
            self.ar[self.top2] = x
        else:
            print("Stack Overflow by element : ", x)

    def pop1(self):
        if self.top1 <= self.size/2:
            x = self.ar[self.top1]
            self.top1 = self.top1 + 1
            return x
        else:
            print("Stack Underflow ")
            exit(1)

    def pop2(self):
        if self.top2 >= math.floor(self.size/2) + 1:
            x = self.ar[self.top2]
            self.top2 = self.top2 - 1
            return x
        else:
            print("Stack Underflow ")
            exit(1)

# Main program
ts = twoStacks(5)
ts.push1(5)
ts.push2(10)
ts.push2(10)
ts.push1(13)
ts.push2(6)

print("Popped element from stack1 is : " + str(ts.pop1()))
ts.push2(12)
print("Popped element from stack2 is : " + str(ts.pop2()))

"""----------------------------------------------------------------"""


# Python Script to Implement two stacks in a list
class twoStacks:
    def __init__(self, n):
        self.size = n
        self.arr = [None] * n
        self.top1 = -1
        self.top2 = self.size

    def push1(self, x):
        if self.top1 < self.top2 - 1:
            self.top1 = self.top1 + 1
            self.arr[self.top1] = x

        else:
            print("Stack Overflow ")
            exit(1)

    def push2(self, x):
        if self.top1 < self.top2 - 1:
            self.top2 = self.top2 - 1
            self.arr[self.top2] = x

        else :
            print("Stack Overflow ")
            exit(1)

    def pop1(self):
        if self.top1 >= 0:
            x = self.arr[self.top1]
            self.top1 = self.top1 - 1
            return x
        else:
            print("Stack Underflow ")
            exit(1)

    def pop2(self):
        if self.top2 < self.size:
            x = self.arr[self.top2]
            self.top2 = self.top2 + 1
            return x

        else:
            print("Stack Underflow ")
            exit()

# Main program
ts = twoStacks(5)
ts.push1(5)
ts.push2(10)
ts.push1(16)
ts.push2(13)
ts.push1(26)

print("Popped element from stack1 is " + str(ts.pop1()))
ts.push2(12)
print("Popped element from stack2 is " + str(ts.pop2()))