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
        a = self.head
        while a.next is not None:
            a = a.next
        a.next = temp

    def create_list(self):

        n = int(input("Enter the number of nodes: "))
        if n == 0:
            return
        for i in range(n):
            data = int(input("Enter the element to be inserted: "))
            self.insert_at_end(data)

    def insert_after(self, data, x):

        a = self.head
        while a is not None:
            if a.data == x:
                break
            a = a.next
        if a is None:
            print(x, "not present in the list")
        else:
            temp = Node(data)
            temp.next = a.next
            a.next = temp

    def insert_before(self, data, x):
        # if list is empty
        if self.head is None:
            print("List is empty")
            return
        # x is in first node, new node is to be inserted before first node
        if x == self.head.data:
            temp = Node(data)
            temp.next = self.head
            self.head = temp
            return
        # Find reference to predecessor of node containing x
        a = self.head
        while a.next is not None:
            if a.next.data == x:
                break
            a = a.next
        if a.next is None:
            print(x, " not present in the list")
        else:
            temp = Node(data)
            temp.next = a.next
            a.next = temp

    def insert_at_position(self, data, k):

        if k == 1:
            temp = Node(data)
            temp.next = self.head
            self.head = temp
            return

        a = self.head
        i = 1
        while i < k-1 and a is not None:   # find a reference (link) to k-1 node
            a = a.next
            i += 1

        if a is None:
            print("You can insert only up to position ", i)
        else:
            temp = Node(data)
            temp.next = a.next
            a.next = temp

    def delete_node(self, x):

        if self.head is None:
            print("List is empty")
        # deletion of first node
        if self.head.data == x:
            self.head = self.head.next.next

        # deletion in between or at the end
        a = self.head
        while a.next is not None:
            if a.next.data == x:
                break
            a = a.next

        if a.next is None:
            print("Element ", x, " not in the list")
        else:
            a.next = a.next.next

    def delete_fisrt_node(self):

        if self.head is None:
            return
        self.head = self.head.next

    def delete_last_node(self):
        if self.head is None:
            return

        if self.head.next is None:
            self.head = None
            return
        a = self.head
        while a.next.next is not None:
            a = a.next
        a.next = None

    def reverse_list(self):
        prev = None
        a = self.head
        while a is not None:
            next_node = a.next
            a.next = prev
            prev = a
            a = next_node
        self.head = prev

    def bubble_sort_exdata(self):
        end = None

        while end != self.head.next:
            a = self.head
            while a.next != end:
                q = a.next
                if a.data > q.data:
                    a.data, q.data = q.data, a.data
                a = a.next
            end = a

    def buble_sort_exlink(self):
        end =None
        while end != self.head.next:
            r = a = self.head
            while a.next!= end:
                q = a.next
                if a.data> q.data:
                    a.next = q.next
                    q.next = a
                    if a != self.head:
                        r.next = q
                    else:
                        self.head = q
                    a, q = q, a
                r = a
                a = a.next
            end = a

    def has_cycle(self):
        pass

    def find_cycle(self):
        pass

    def remove_cycle(self):
        pass

    def insert_cycle(self, x):
        pass

    def merge2(self, list2):
        merge_list = SingleLinkedList()
        merge_list.head = self._merge2(self.head, list2.head)
        return merge_list

    def _merge2(self, p1, p2):
        if p1.data <= p2.data:
            startM = p1
            p1 = p1.next
        else:
            startM = p2
            p2 = p2.next
        pM = startM

        while p1 is not None and p2 is not None:
            if p1.data <= p2.data:
                pM.next = p1
                pM = pM.next
                p1 = p1.next
            else:
                pM.next = p2
                pM = pM.next
                p2 = p2.next

        if p1 is None:
            pM.next = p2
        else:
            pM.next = p2

        return startM

    def merge_sort(self):
        self.head = self._merge_sort_rec(self.head)

    def _merge_sort_rec(self, listStart):
        # if list empty or has one element
        if listStart is None or listStart.next is None:
            return listStart

        # if more than one element
        start1 = listStart
        start2 = self._divide_list(listStart)
        start1 = self._merge_sort_rec(start1)
        start2 = self._merge_sort_rec(start2)
        startM = self._merge2(start1, start2)
        return startM

    def _divide_list(self, a):
        q = a.next.next
        while q is not None and q.next is not None:
            a = q.next
            q = q.next.next
        start2 = a.next
        a.next = None
        return start2














