class ListNode:
    def __init__(self, val = None, prev = None, next = None):
        self.val = val
        self.prev = prev
        self.next = next

class MyCircularDeque:

    def __init__(self, k: int):
        self.size = k
        self.count = 0
        self.head = None
        self.tail = None

    def insertFront(self, value: int) -> bool:
        if self.count < self.size:
            if not self.head:
                self.head = ListNode(value)
                self.tail = self.head
            else:
                newnode = ListNode(value, self.tail, self.head)
                self.head.prev = newnode
                self.head = newnode
            self.count += 1
            self.tail.next = self.head
            return True
        else:
            return False

    def insertLast(self, value: int) -> bool:
        if self.count < self.size:
            if not self.tail:
                self.tail = ListNode(value)
                self.head = self.tail
            else:
                newnode = ListNode(value, self.tail, self.head)
                self.head.prev = newnode
                self.tail.next = newnode
                self.tail = newnode
            self.count += 1
            return True
        else:
            return False

    def deleteFront(self) -> bool:
        if not self.count:
            return False
        if self.head == self.tail:
            self.head = self.tail = None
        else:
            node = self.head
            self.tail.next = self.head.next
            self.head.prev = self.tail
            self.head = node.next
        self.count -= 1
        return True
        
    def deleteLast(self) -> bool:
        if not self.count:
            return False
        if self.head == self.tail:
            self.head = self.tail = None
        else:
            node = self.tail
            self.tail.prev.next = self.head
            self.head.prev = self.tail.prev
            self.tail = node.prev
        self.count -= 1
        return True

    def getFront(self) -> int:
        if not self.count:
            return -1
        return self.head.val

    def getRear(self) -> int:
        if not self.count:
            return -1
        return self.tail.val

    def isEmpty(self) -> bool:
        return self.count == 0

    def isFull(self) -> bool:
        return self.count == self.size

obj = MyCircularDeque(77)

inputs = ["MyCircularDeque","insertFront","getRear","deleteLast","getRear","insertFront","insertFront","insertFront","insertFront","isFull","insertFront","isFull","getRear","deleteLast","getFront","getFront","insertLast","deleteFront","getFront","insertLast","getRear","insertLast","getRear","getFront","getFront","getFront","getRear","getRear","insertFront","getFront","getFront","getFront","getFront","deleteFront","insertFront","getFront","deleteLast","insertLast","insertLast","getRear","getRear","getRear","isEmpty","insertFront","deleteLast","getFront","deleteLast","getRear","getFront","isFull","isFull","deleteFront","getFront","deleteLast","getRear","insertFront","getFront","insertFront","insertFront","getRear","isFull","getFront","getFront","insertFront","insertLast","getRear","getRear","deleteLast","insertFront","getRear","insertLast","getFront","getFront","getFront","getRear","insertFront","isEmpty","getFront","getFront","insertFront","deleteFront","insertFront","deleteLast","getFront","getRear","getFront","insertFront","getFront","deleteFront","insertFront","isEmpty","getRear","getRear","getRear","getRear","deleteFront","getRear","isEmpty","deleteFront","insertFront","insertLast","deleteLast"]
parameters = [[77],[89],[],[],[],[19],[23],[23],[82],[],[45],[],[],[],[],[],[74],[],[],[98],[],[99],[],[],[],[],[],[],[8],[],[],[],[],[],[75],[],[],[35],[59],[],[],[],[],[22],[],[],[],[],[],[],[],[],[],[],[],[21],[],[26],[63],[],[],[],[],[87],[76],[],[],[],[26],[],[67],[],[],[],[],[36],[],[],[],[72],[],[87],[],[],[],[],[85],[],[],[91],[],[],[],[],[],[],[],[],[],[34],[44],[]]


for i in range(1, len(inputs)):
    func = getattr(obj, inputs[i])
    if not parameters[i]:
        print(func())
    else:
        print(func(parameters[i][0]))