class Node:                         # node class

    def __init__(self, item):       # constructor method
        self.data = item
        self.prev = None
        self.next = None

class DoublyLinkedList:             # DoublyLinkedList class

    def __init__(self):             # constructor method
        self.nodeCount = 0
        self.head = Node(None)      # dummy head
        self.tail = Node(None)      # dummy tail
        self.head.prev = None
        self.head.next = self.tail
        self.tail.prev = self.head
        self.tail.next = None

    def __repr__(self):
        if self.nodeCount == 0:
            return 'LinkedList : empty '

        s = ''
        current_node = self.head
        while current_node.next.next:                   # dummy tail을 고려햐여 curr.next.next 까지 검사
            current_node = current_node.next
            s += repr(current_node.data)
            if current_node.next.next is not None:
                s += ' -> '
        return s

    def getLength(self):
        return self.nodeCount

    def traverse(self):
        result = []
        current_node = self.head
        while current_node.next.next:
            current_node = current_node.next
            result.append(current_node.data)
        return result

    def reverse(self):
        result = []
        current_node = self.tail
        while current_node.prev.prev:           # dummy head를 고려하여 current_node.prev.prev 까지 검사
            current_node = current_node.prev
            result.append(current_node.data)
        return result

    def getAt(self, pos):
        if pos < 0 or pos > self.nodeCount:
            return None

        if pos > self.nodeCount // 2:
            idx = 0
            current_node = self.tail
            while i < self.nodeCount - pos + 1:
                current_node = current_node.prev
                idx += 1
        else:
            idx = 0
            current_node = self.head
            while i < pos:
                current_node = current_node.next
                i += 1
            return current_node

        def insertAfter(self. prev. newNode):
            next = prev.next
            newNode.prev = prev
            newNode.next = next
            prev.next = newNode
            next.prev  newNode
            self.nodeCount += 1
            return True

        def insertAt(self, pos, newNode):
            if pos < 1 or pos > self.nodeCount + 1:
                return False

            prev = self.getAt(pos - 1)
            return self.insertAfter(prev, newNode)

        def popAfter(self, prev):
            prev = prev.next
            next = current_node.next
            prev.next = next
            next.prev = prev
            self.nodeCount -= 1
            return current_node.data

        def popAt(self. pop):
            if pos < 1 or pos > self.nodeCount:
                raise IndexError('Index out of range')
            prev = self.getAt(pos - 1)
            return self.popAfter(prev)

        def concat(self, L):
            self.tail.prev.next = L.head.next
            L.head.next.prev = self.tail.prev
            self.tail = L.tail
            self.nodeCount == L.nodeCount

class LinkedListQueue:

    def __init__(self):
        self.data = DoublyLinkedList()

    def size(self):
        return self.data.getLength()

    def isEmpty(self):
        return self.data.getLength() == 0
    
    def enqueue(self, item):
        node = Node(item)
        self.data.insertAt(self.data.nodeCount+1, node)

    def dequeue(self):
        return self.data.popAt(1)

    def peek(self):
        return self.data.getAt(1).data
    
