class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None #address of the previous node
        self.next = None #address of the next node

class DoublyLL:
    def __init__(self):
        self.head = None

    def insert_beg(self, data):
        nb = Node(data)
        nb.next = self.head
        self.head = nb

    def insert_end(self, data):
        ne = Node(data)
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = ne
        ne.prev = temp

    def display(self):
        if self.head == None:
            print("List is empty")
        else:
            temp = self.head
            while temp:
                print(temp.data, "--->", end = " ")
                temp = temp.next

# driver code
l = DoublyLL()
n = Node(10)
l.head = n
n1 = Node(20)
n.next = n1
n2 = Node(30)
n1.prev = n
n1.next = n2
l.display()
print(end='\n')
l.insert_beg(100)
l.display()
print(end='\n')
l.insert_end(100)
l.display()

"""----------------------------------------------------------------"""

class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None  # address of the previous node
        self.next = None  # address of the next node

class DoublyLL:
    def __init__(self):
        self.head = None

    def delete_beg(self):
        if self.head != None:
            temp = self.head
            self.head = self.head.next
            self.head.prev = None
            temp = None

    def delete_end(self):
        if self.head != None:
            if self.head.next == None:
                self.head = None
            else:
                temp = self.head
                while temp.next.next:
                    temp = temp.next
                temp.next = None

    def display(self):
        if self.head == None:
            print("List is empty")
        else:
            temp = self.head
            while temp:
                print(temp.data, "--->", end = " ")
                temp = temp.next

# driver code
l = DoublyLL()
n = Node(10)
l.head = n
n1 = Node(20)
n.next = n1
n2 = Node(30)
n2.prev = n1
n1.next = n2
l.display()
print(end='\n')
l.delete_beg()
l.display()
print(end='\n')
l.delete_end()
l.display()