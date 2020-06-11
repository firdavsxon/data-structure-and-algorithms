class Node:

    def __init__(self, value):
        self.data = value
        self.next = None


class SingleLinkedList:

    def __init__(self):
        self.head = None

    def display_list(self):
        if self.head is None:
            print("List is empty")
            return
        else:
            print("List is: ")
            a = self.head
            while a is not None:
                print(a.data, " ", end='')
                a = a.next
            print()

    def count_node(self):
        a = self.head
        n=0
        while a is not None:
            n += 1
            a = a.next
        print("Number of nodes in the list = ", n)
        return n

    def search(self, x):
        position = 1
        a = self.head
        while a is not None:
            if a.data == x:
                print(x, " is at position ", position)
                return True
            position += 1
            a = a.next
        else:
            print(x, "not found in list")
            return False

    def insert_in_beginning(self, data):
        if not isinstance(data, Node):
            data = Node(data)
        data.next = self.head
        self.head = data

    def insert_at_end(self, data):
        temp = Node(data)

        if self.head is None:
            self.head = temp
            return

        a= self.head
        while a.next is not None:
            a=a.next
        a.next = temp

    def create_list(self):
        n = int(input("Enter the number of nodes: "))
        if n == 0:
            return
        for i in range(n):
            data = int(input("Enter the element to be inserted: "))
            self.insert_at_end(data)

    def insert_after(self, data, x):
        pass

    def insert_before(self, data, x):
        pass

    def insert_at_position(self, data, k):
        pass

    def delete_node(self, x):
        pass

    def delete_fisrt_node(self):
        pass

    def delete_last_node(self):
        pass

    def reverse_list(self):
        pass

    def bubble_sort_exdata(self):
        pass

    def buble_sort_exlink(self):
        pass

    def has_cycle(self):
        pass

    def find_cycle(self):
        pass

    def remove_cycle(self):
        pass

    def insert_cycle(self, x):
        pass

    def merge2(self, list2):
        pass

    def _merge2(self, p1, p2):
        pass

    def merge_sort(self):
        pass

    def _merge_sort_rec(self, listStart):
        pass

    def _divide_list(self, p):
        pass














