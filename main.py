class Queue:
    def __init__(self):
        self.items = []

    def show(self):
        print(self.items)

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        return self.pop()

    def size(self):
        return len(self.items)

    def is_empty(self):
        return self.items == []

    def peek(self):
        return self.items[-1]

class BoardState:
    #i definitely can't find the banter section in PEP8
    def __init__(self, q):
        self.board  = [q.items[i : i+3] for i in range(0, len(q.items), 3)]

    def show(self):
        print(self.board)

    def manhattan_distance():
        pass




q = Queue()

q.show()
for i in range(9):
    q.enqueue(i + 1)

q.show()

b = BoardState(q)
b.show()
