from ImpArrays import Stack
class Queue:
    def __init__(self):
        self.s1 = Stack()
        self.s2 = Stack()

    def enque(self, x):
        while self.s1.length() > 0:
            self.s2.push(self.s1.pop())

        self.s1.push(x)

        while self.s2.length() > 0:
            self.s1.push(self.s2.pop())

    def dequeue(self):
        if self.s1.length() == 0:
            return "Nothing to pop"
        return self.s1.pop()

    def peek(self):
        if self.s1.length() == 0:
            return "Nothing to peek"
        return self.s1.peek()

    def length(self):
        return self.s1.length()


que = Queue()

print(que.peek())
print(que.dequeue())
que.enque(10)
que.enque(30)
que.enque(45)
print(que.dequeue())
print(que.peek())


