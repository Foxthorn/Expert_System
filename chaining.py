class Node:
    def __init__(self, data=None, bool=False, equat=[]):
        self.data = data
        self.bool = bool
        self.equat = equat
        self.next_node = None

    def set_next(self, n):
        self.next_node = n

    def set_data(self, d):
        self.data = d


class Chain:
    def __init__(self):
        self.head = Node()
        self.size = 0

    def reset_equat(self, data):
        cur = self.head
        while cur.next_node is not None:
            if cur.data == data:
                cur.equat = []
                break
            cur = cur.next_node

    def add_rules(self, lines):
        cur = self.head
        while cur.next_node is not None:
            cur = cur.next_node
            self.reset_equat(cur.data)
            for str in lines:
                if cur.data in str:
                    cur.equat.append(str)

    def add(self, data):
        new_node = Node(data)
        cur = self.head
        while cur.next_node is not None:
            cur = cur.next_node
        cur.next_node = new_node
        self.size += 1

    def find(self, data):
        cur = self.head
        while cur.next_node is not None:
            if cur.data == data:
                return True
            cur = cur.next_node
        return False

    def display_rules(self):
        cur_node = self.head
        while cur_node.next_node is not None:
            cur_node = cur_node.next_node
            print(cur_node.data + '->' + str(cur_node.equat))

    def display_bool(self):
        elems = []
        cur_node = self.head
        while cur_node.next_node is not None:
            cur_node = cur_node.next_node
            elems.append(cur_node.data + '->' + str(cur_node.bool))
        print elems

    def display(self):
        elems = []
        cur_node = self.head
        while cur_node.next_node is not None:
            cur_node = cur_node.next_node
            elems.append(cur_node.data)
        print elems

    def set_true(self, data):
        cur = self.head
        while cur.next_node is not None:
            if cur.data == data:
                cur.bool = True
            cur = cur.next_node
