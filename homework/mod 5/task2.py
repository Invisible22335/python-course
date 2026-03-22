class Node:
    def __init__(self, data):
        self.data = data
        self.nref = None
        self.pref = None

class Queue:
    def __init__(self):
        self.start = None
        self.end = None

    def pop(self):
        if self.start is None:
            return None
        val = self.start.data
        self.start = self.start.nref
        if self.start is None:
            self.end = None
        else:
            self.start.pref = None
        return val

    def push(self, val):
        node = Node(val)
        if self.start is None:
            self.start = node
            self.end = node
        else:
            self.end.nref = node
            node.pref = self.end
            self.end = node

    def insert(self, n, val):
        node = Node(val)
        if n == 0:
            node.nref = self.start
            if self.start is not None:
                self.start.pref = node
            else:
                self.end = node
            self.start = node
            return

        cur = self.start
        i = 0
        while cur is not None and i < n - 1:
            cur = cur.nref
            i += 1

        if cur is None:
            return

        node.nref = cur.nref
        node.pref = cur
        if cur.nref is not None:
            cur.nref.pref = node
        else:
            self.end = node
        cur.nref = node

    def print(self):
        cur = self.start
        while cur is not None:
            print(cur.data, end=' ')
            cur = cur.nref
        print()